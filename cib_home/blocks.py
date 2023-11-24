from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


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
            ]
        )
    )

    class Meta:  # noqa
        template = "patterns/blocks/cards/callout.html"
        icon = "placeholder"
        label = "Call out"