from django.db import models
from django.utils.translation import gettext_lazy as _, pgettext_lazy

from wagtail.admin.panels import FieldPanel

from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

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

    description = models.CharField(
        verbose_name=pgettext_lazy("A tag description", "description"), max_length=255, default='', unique=False
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
        FieldPanel("body"),
    ]
