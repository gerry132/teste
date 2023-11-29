from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _

from cib_navigation.models import ALT_HELP_TEXT

ALT_IMAGE = ALT_HELP_TEXT % 'image'


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
