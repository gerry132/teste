from django.db import models

from wagtail.core.fields import StreamField
from wagtail.images import get_image_model_string
from functools import cached_property

from wagtail.admin.panels import (
    FieldPanel, TabbedInterface, ObjectList,
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail import blocks

from cib_content_page.blocks.address import AddressBlock
from cib_content_page.blocks.custom_image import CustomImageBlock
from cib_content_page.blocks.heading_block import HeadingBlock
from cib_content_page.blocks.table import TinyMCETableBlock
from cib_content_page.blocks.video import VideoBlock
from cib_news_content_page.models import NewsContentPage
from cib_utils.models import HeroPage

from .blocks import CallOutBlock, InfoPanelBlock

IMAGE_MODEL = get_image_model_string()


class HomePage(HeroPage):
    max_count = 1
    template = "patterns/pages/home/home_page.html"
    favicon = models.ForeignKey(
        IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    body = StreamField(
        [
            ("CalloutCards", CallOutBlock()),
            ("InfoPanelCards", InfoPanelBlock()),
            ('image', ImageChooserBlock()),
            ('custom_image', CustomImageBlock()),
            ('video', VideoBlock()),
            ('embed_html_widget', blocks.TextBlock(required=False)),
            ("richtext", blocks.RichTextBlock(required=False)),
            ("table", TinyMCETableBlock()),
            ("address", AddressBlock()),
            ("heading", HeadingBlock()),
        ],
        use_json_field=True,
        null=True,
        blank=True
    )
    jobvacancy_latestnews_snippet = models.ForeignKey(
        'utils.JobsVacanciesAndLatestNewsSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    news_letter_signup_cta = StreamField(
        [
            ("newslettersignupcta_snippet", SnippetChooserBlock(target_model="utils.NewsletterSignUpCTASnippet"))
        ],
        null=True,
        blank=True
    )
    content_panels = HeroPage.content_panels + [
        FieldPanel("body"),
        FieldPanel("jobvacancy_latestnews_snippet"),
        FieldPanel("news_letter_signup_cta")
    ]

    @cached_property
    def latest_news(self):
        return (
            NewsContentPage.objects
            .filter(locale=self.locale)
            .public()
            .live()
            .order_by("-last_published_custom")[:1]
            .specific()
        )

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(HeroPage.hero_panel, heading='Hero'),
        ObjectList(HeroPage.promote_panels, heading='Promote'),
        ObjectList(HeroPage.settings_panels, heading='Settings', classname="settings"),
    ])
