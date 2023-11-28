from django import forms
from django.forms import widgets
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _

from cib_navigation.models import ALT_HELP_TEXT

ALT_IMAGE = ALT_HELP_TEXT % 'image'


class ColorChooserBlock(blocks.FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = forms.CharField(
            required=required,
            help_text=help_text,
            widget=widgets.TextInput(attrs={'type': 'color'}))
        super().__init__(**kwargs)

    class Meta:
        icon = "color_lens"
        template = "patterns/blocks/cards/color_chooser_block.html"


class CallOutBlock(blocks.StructBlock):
    calloutcards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("icon", ImageChooserBlock(required=False,
                                           help_text="The Icon size should be 55x55 pixels")),
                ("title", blocks.CharBlock(required=True)),
                ("text", blocks.RichTextBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False,
                                                        help_text="This button has higher priority than button_url")),
                ("button_url", blocks.URLBlock(required=False, )),
                ("button_text", blocks.CharBlock(required=True)),
                ("left_border_color", ColorChooserBlock(required=True))
            ]
        )
    )

    class Meta:  # noqa
        template = "patterns/blocks/cards/callout.html"
        icon = "placeholder"
        label = "Call out"


class InfoPanelBlock(blocks.StructBlock):
    infocards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("icon", ImageChooserBlock(required=False,
                                           help_text="The Icon size should be 60x60 pixels")),
                ("title", blocks.CharBlock(required=True)),
                ("text", blocks.RichTextBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False,
                                                        help_text="This button has higher priority than button_url")),
                ("button_url", blocks.URLBlock(required=False, )),
                ("button_text", blocks.CharBlock(required=True)),
            ]
        )
    )

    class Meta:  # noqa
        template = "patterns/blocks/cards/infopanel.html"
        icon = "placeholder"
        label = "Info Panel"


class JobsVacanciesBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("icon", ImageChooserBlock(required=False,
                                           help_text="The Icon size should be 60x60 pixels")),
                ("title", blocks.CharBlock(required=True)),
                ("text", blocks.RichTextBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False,
                                                        help_text="This button has higher priority than button_url")),
                ("button_url", blocks.URLBlock(required=False, )),
                ("button_text", blocks.CharBlock(required=True)),
                ("Job_vacancies_Background_color", ColorChooserBlock(
                    required=True,
                    help_text="Set the Job vacancies background color"
                )),

                ("news_button_text", blocks.CharBlock(required=True,
                                                      help_text="News card button text")),
                ("news_Background_color", ColorChooserBlock(required=True,
                                                            help_text="Set the News background color"))

            ]
        )
    )

    class Meta:  # noqa
        template = "patterns/blocks/cards/jobvacancies.html"
        icon = "placeholder"
        label = "Job Vacancies"


class BoardMembersCardBlock(blocks.StructBlock):
    boardmemberscards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("image_alt", blocks.CharBlock(required=True, help_text=_(ALT_IMAGE))),
                ("title", blocks.CharBlock(required=True)),
                ("description", blocks.RichTextBlock(required=False)),
            ]
        )
    )

    class Meta:
        icon = "image"
        label = "Board Member Card Block"
        template = "patterns/blocks/cards/board_member_card.html"
