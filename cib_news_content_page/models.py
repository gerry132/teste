from django.db import models

from cib_content_page.models import ContentPage

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TagBase, ItemBase


class NewsTag(TagBase):
    free_tagging = False

    class Meta:
        verbose_name = "whats new tag"
        verbose_name_plural = "whats new tags"


class TaggedNews(ItemBase):
    tag = models.ForeignKey(
        NewsTag, related_name="tagged_blogs", on_delete=models.CASCADE,
        help_text="whats new tags"
    )
    content_object = ParentalKey(
        to='NewsContentPage',
        on_delete=models.CASCADE,
        related_name='tagged_items'
    )


class NewsContentPage(ContentPage):
    template = "patterns/pages/news_content_page.html"
    parent_page_types = ["cib_news_page.News"]
    tags = ClusterTaggableManager(through='TaggedPage', blank=True)

