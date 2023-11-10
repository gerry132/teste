from cib_utils.blocks import BaseBlockLinkContext
from django.utils.translation import gettext_lazy as _

from wagtail import blocks


class LinkBlock(BaseBlockLinkContext):
    page = blocks.PageChooserBlock(required=False)
    title = blocks.CharBlock(
        help_text=_("Leave blank to use the page's own title"), required=False
    )

    class Meta:
        template = ("patterns/molecules/navigation/blocks/menu_item.html",)


class LinkBlockWithURL(BaseBlockLinkContext):
    page = blocks.PageChooserBlock(required=False)
    title = blocks.CharBlock(
        help_text=_("Leave blank to use the page's own title"), required=False
    )
    url = blocks.URLBlock(
        label="URL",
        required=False,
        help_text="An external link.",
    )


class LinkWithURLANDSubLinks(BaseBlockLinkContext):
    page = blocks.PageChooserBlock(required=False)
    title = blocks.CharBlock(
        help_text=_("Leave blank to use the page's own title"), required=False
    )
    url = blocks.URLBlock(
        label="URL",
        required=False,
        help_text="An external link.",
    )
    sub_links = blocks.StreamBlock([
        ("sub_links", LinkBlockWithURL()),
    ],
        required=False,
        blank=True,
    )
