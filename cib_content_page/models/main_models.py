from django.db import models
from django.utils.translation import gettext_lazy as _, pgettext_lazy

from typing import Sequence, Tuple

from wagtail.admin.panels import FieldPanel

from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks.stream_block import StreamValue
from wagtail.blocks.struct_block import StructValue

from taggit.models import TagBase, ItemBase

from modelcluster.fields import ParentalKey

from ..blocks.table import TinyMCETableBlock
from ..blocks.video import VideoBlock
from ..blocks.custom_image import CustomImageBlock
from ..blocks.address import AddressBlock
from ..blocks.heading_block import HeadingBlock

from modelcluster.contrib.taggit import ClusterTaggableManager

from cib_utils.models import BasePage


class PageTag(TagBase):
    free_tagging = False

    locale = models.CharField(max_length=10, default='en', null=True, blank=True)
    description = models.CharField(
        verbose_name=pgettext_lazy("A tag description", "description"),
        max_length=255, default='', unique=False, null=True, blank=True
    )

    class Meta:
        verbose_name = "Page Tag"
        verbose_name_plural = "Page Tags"


class TaggedPage(ItemBase):
    tag = models.ForeignKey(
        PageTag, related_name="tagged_pages", on_delete=models.CASCADE
    )
    content_object = ParentalKey(
        to='ContentPage',
        on_delete=models.CASCADE,
        related_name='tagged_items'
    )


class ContentPage(BasePage):
    """Page for all content page"""
    template = "patterns/pages/content_page.html"
    parent_page_types = ["cib_home.HomePage"]
    tags = ClusterTaggableManager(through='TaggedPage', blank=True)
    left_nav_title = models.TextField(
        blank=False,
        null=True
    )
    body = StreamField(
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
        verbose_name=_("body"),
        blank=True,
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("left_nav_title"),
        FieldPanel("body"),
    ]

    promote_panels = BasePage.promote_panels + [
        FieldPanel("tags"),
    ]

    def get_section_headings(self) -> Sequence[Tuple[str]]:
        """
        Return a list of tuples in the format (menu_text, anchor_id).
        Used to generate the in-page nav at the top of pages.
        """
        section_headings = []
        for block in getattr(self, "body", []):
            if isinstance(block.value, StructValue)\
             and "anchor_id" in block.value:
                section_headings.append(
                    (block.value["title"], block.value["anchor_id"])
                )
                for val in block.value.values():
                    if isinstance(val, StreamValue):
                        for sub_val in val:
                            if isinstance(sub_val.value, StructValue):
                                section_headings.append(
                                    (
                                        sub_val.value["text"],
                                        sub_val.value["anchor_id"])
                                )
        return section_headings

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context.update(
            section_headings=self.get_section_headings(),
        )
        return context
