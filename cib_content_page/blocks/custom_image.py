from django.utils.translation import gettext_lazy as _
from wagtail.core import blocks
from wagtail.core.blocks import CharBlock
from wagtail.images.blocks import ImageChooserBlock


class CustomImageBlock(blocks.StructBlock):
    """Custom image for whats new content pages"""
    help_text = ''

    def __init__(self, help_text=None, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        CustomImageBlock.help_text = help_text

    image = ImageChooserBlock(label=_("Image"), help_text=help_text)
    caption = CharBlock(required=False, label=_("Caption"))
    alt_text = CharBlock(required=False, label=_("Alt"))
    size = blocks.ChoiceBlock(
        required=False,
        choices=[('200', _("200*132")), ('400', _("400*267")), ('800', _("800*534"))],
        default='800',
        label=_("Size"),
    )
    format = blocks.ChoiceBlock(
        required=False,
        choices=[('left', _("Left")),
                 ('center', _("Centre")),
                 ('right', _("Right"))],
        default='left',
        label=_("Align"),
    )

    class Meta:
        template = 'patterns/blocks/custom_image.html'
        icon = 'image'
