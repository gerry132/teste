from cib_utils.blocks import BaseBlockLinkContext, LinkBlockWithURL
from django.utils.translation import gettext_lazy as _

from wagtail import blocks


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


class LinkColumnWithHeader(blocks.StructBlock):
    heading = blocks.CharBlock(
        required=False, help_text=_("Leave blank if no header required.")
    )
    links = blocks.ListBlock(LinkBlockWithURL())

    class Meta:
        template = ("patterns/molecules/navigation/blocks/footer_column.html",)
