from django.db import models

from cib_content_page.models import ContentPage
from cib_content_page.blocks.custom_image import AltImageBlock

from modelcluster.fields import ParentalKey, ParentalManyToManyField

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
        NewsTag, related_name="tagged_news", on_delete=models.CASCADE,
        help_text="news tags"
    )
    content_object = ParentalKey(
        to='NewsContentPage',
        on_delete=models.CASCADE,
        related_name='tagged_news_items'
    )


class NewsContentPage(ContentPage):
    template = "patterns/pages/news_content_page.html"
    parent_page_types = ["cib_news_page.News"]

    lead_fields = StreamField(blocks.StreamBlock(
        [
            ("banner_image", AltImageBlock(
                help_text="The optimal size is 300x200 pixels or a 3:2 aspect ratio."
            )),
            ("lead_text", blocks.RichTextBlock(required=True, features=[
                "h2", "h3", "h4", "bold", "italic", "link", "document-link"
            ]))
        ], max_num=2),
        use_json_field=True,
        null=True,
        blank=False)

    show_on_page = models.BooleanField(blank=False, null=True)

    news_tags = ParentalManyToManyField("NewsTag", blank=True)

    content_panels = ContentPage.content_panels + [
        FieldPanel("lead_fields"),
        FieldPanel("show_on_page", widget=forms.CheckboxInput),
        MultiFieldPanel(
            [
                FieldPanel("news_tags", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Tags"
        ),

    ]

    @property
    def current_tag(self):
        return NewsTag.objects.filter(
                NewsContentPage__id=self.id).first()
