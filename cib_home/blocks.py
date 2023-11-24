from django import forms
from django.forms import widgets
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


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
                ("button_url", blocks.URLBlock(required=False,)),
                ("button_text", blocks.CharBlock(required=True)),
                ("left_border_color", ColorChooserBlock(required=True))
            ]
        )
    )

    class Meta:  # noqa
        template = "patterns/blocks/cards/callout.html"
        icon = "placeholder"
        label = "Call out"
