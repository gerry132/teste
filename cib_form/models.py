from django.db import models
from django.utils.translation import gettext_lazy as _
from django import forms

from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField,
    EmailFormMixin,
    FormMixin
)
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.contrib.forms.forms import FormBuilder
from wagtail import blocks

from modelcluster.fields import ParentalKey

from cib_content_page.models.main_models import ContentPage
from cib_content_page.blocks.table import TinyMCETableBlock
from cib_content_page.blocks.video import VideoBlock
from cib_content_page.blocks.custom_image import CustomImageBlock
from cib_content_page.blocks.address import AddressBlock
from cib_content_page.blocks.heading_block import HeadingBlock


class RichTextFieldLabelForm(AbstractFormField):
    richtext_label = RichTextField(
        verbose_name=_("Rich Text Label"),
        blank=True,
        help_text=_("This will show only in the Checkbox fields, this has higher priority than the label field")
    )
    page = ParentalKey(
        'FormPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )

    panels = AbstractFormField.panels + [
        FieldPanel('richtext_label')
    ]


class CustomFormBuilder(FormBuilder):

    def create_date_field(self, field, options):
        options['widget'] = forms.DateInput(
            attrs={'class': 'date-picker', 'autocomplete': 'off'},
            format='%Y-%m-%d'
        )
        return super().create_date_field(field, options)

    def create_datetime_field(self, field, options):
        options['widget'] = forms.DateTimeInput(
            attrs={'class': 'datetime-picker', 'autocomplete': 'off'},
            format='%Y-%m-%d %H:%M'
        )
        return super().create_datetime_field(field, options)

    def create_checkbox_with_richtext_field(self, field, options):
        """
        Override the create_field method to modify how fields are created.
        For example, add the rich text description to the options dict.
        """
        # Assume 'rich_text_description' is somehow retrieved for each field.
        rich_text_description = self.get_richtext_label_for_field(field)

        # You could add it to the options dict, but note: Django's built-in form fields
        # do not expect a 'rich_text_description' option, so you'd need to handle
        # this custom data in your form or template differently.
        options['rich_text_description'] = rich_text_description

        # Call the superclass method to actually create the field.
        return super().get_create_field_function(field.field_type, options)


class FormPage(EmailFormMixin, FormMixin, ContentPage):
    template = "patterns/pages/form_page.html"
    landing_page_template = "patterns/pages/form_landing_page.html"

    intro = RichTextField(blank=True)

    bottom_page_body = StreamField(
        [
            ('image', ImageChooserBlock()),
            ('custom_image', CustomImageBlock()),
            ('video', VideoBlock()),
            ('embed_html_widget', blocks.TextBlock(required=False)),
            ("richtext", blocks.RichTextBlock(required=False)),
            ("table", TinyMCETableBlock()),
            ("address", AddressBlock()),
            ("heading", HeadingBlock())
        ],
        use_json_field=True,
        blank=True,
    )
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("left_nav_title"),
        FieldPanel('intro'),
        FieldPanel("body"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel("bottom_page_body"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
        FieldPanel("jobvacancy_latest_news_snippet"),
        FieldPanel("news_letter_signup_cta")
    ]

    form_builder = CustomFormBuilder

    def get_context(self, request):
        context = super().get_context(request)
        form_fields_with_descriptions = self.get_form_fields_with_descriptions()
        context['fields'] = form_fields_with_descriptions
        return context

    def get_form_fields_with_descriptions(self):
        fields = []
        for field in self.form_fields.all():
            fields.append({
                'label': field.label,
                'rich_text_description': field.richtext_label,
            })
        return fields
