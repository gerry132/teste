# -*- coding: utf-8 -*-
from taggit.models import TagBase
from django.db import models
from wagtail.documents.models import AbstractDocument
from wagtail.documents.models import Document as WagtailDocument
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _, pgettext_lazy
from cib_utils.models import BasePage

from cib_navigation.models import ALT_HELP_TEXT

ALT_IMAGE = ALT_HELP_TEXT % 'image'


class CustomDocument(AbstractDocument):
    admin_form_fields = WagtailDocument.admin_form_fields


class Tag(TagBase):
    free_tagging = False

    class Meta:
        abstract = True


class YearTag(Tag):
    description = models.CharField(
        verbose_name=pgettext_lazy("A tag description", "description"), max_length=255, default='', unique=False
    )

    class Meta:
        abstract = False
        verbose_name = "Year Tag"
        verbose_name_plural = "Year Tags"


class DocumentTypeTag(Tag):
    description = models.CharField(
        verbose_name=pgettext_lazy("A tag description", "description"), max_length=255, default='', unique=False
    )

    class Meta:
        abstract = False
        verbose_name = "Publication Type Tag"
        verbose_name_plural = "Publication Type Tags"


def get_year_tag_choices():
    return [(tag.slug, tag.name) for tag in YearTag.objects.all()]


def get_document_type_tag_choices():
    return [(tag.slug, tag.name) for tag in DocumentTypeTag.objects.all()]


class DocumentBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    image_alt = blocks.CharBlock(required=True, help_text=_(ALT_IMAGE))
    title = blocks.CharBlock(required=True)
    description = blocks.RichTextBlock(required=True)
    language = blocks.ListBlock(
        blocks.StructBlock([
            ('heading', blocks.CharBlock(required=True)),
            ('document', DocumentChooserBlock(required=True)),
        ]),
        label='Languages',
        required=True,
    )
    year_tags = blocks.ChoiceBlock(
        choices=get_year_tag_choices(),
        label='Year Tags',
        required=False,
    )
    publication_type_tags = blocks.ChoiceBlock(
        choices=get_document_type_tag_choices(),
        label='Publication Type Tags',
        required=False,
    )


class DocumentPage(BasePage):
    template = "patterns/pages/document_page.html"
    body = StreamField([
        ('document', DocumentBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        all_year_tags = YearTag.objects.all()
        all_document_type_tags = DocumentTypeTag.objects.all()

        context['all_year_tags'] = all_year_tags
        context['all_document_type_tags'] = all_document_type_tags

        selected_year = request.GET.get('year')
        selected_document_type = request.GET.get('document_type')

        documents = []
        for block in self.body:
            if block.block_type == 'document':
                block_year_tags = block.value['year_tags']
                block_document_type_tags = block.value['publication_type_tags']

                if (
                        (not selected_year or selected_year in block_year_tags)
                        and (not selected_document_type or selected_document_type in block_document_type_tags)
                ):
                    documents.append(block.value)

        context['documents'] = documents
        context['selected_year'] = selected_year
        context['selected_document_type'] = selected_document_type

        return context
