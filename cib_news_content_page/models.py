from django.db import models

from cib_content_page.models import ContentPage
from cib_content_page.blocks.custom_image import AltImageBlock

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TagBase, ItemBase

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail import blocks

from django import forms


class NewsTag(TagBase):
    free_tagging = False

    class Meta:
        verbose_name = "news tag"
        verbose_name_plural = "news tags"


class TaggedNews(ItemBase):
    tag = models.ForeignKey(
        NewsTag, related_name="tagged_blogs", on_delete=models.CASCADE,
        help_text="news tags"
    )
    content_object = ParentalKey(
        to='NewsContentPage',
        on_delete=models.CASCADE,
        related_name='tagged_items'
    )


class NewsContentPage(ContentPage):
    template = "patterns/pages/news_content_page.html"
    parent_page_types = ["cib_news_page.News"]

    banner_image = StreamField(blocks.StreamBlock(
        [
            ("banner_image", AltImageBlock(
                help_text="The optimal size is 400x267 pixels or a 3:2 aspect ratio."
            ))
        ], max_num=1),
        use_json_field=True,
        null=True,
        blank=False)

    show_on_page = models.BooleanField(blank=False, null=True)

    whatsnew_tags = ParentalManyToManyField("NewsTag", blank=True)

    content_panels = ContentPage.content_panels + [
        FieldPanel("banner_image"),
        FieldPanel("show_on_page", widget=forms.CheckboxInput),
        MultiFieldPanel(
            [
                FieldPanel("whatsnew_tags", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Tags"
        ),

    ]

    @property
    def current_tag(self):
        return NewsTag.objects.filter(
                whatsnewcontentpage__id=self.id).first()