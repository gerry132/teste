from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.images import get_image_model_string
from wagtail.images.blocks import ImageChooserBlock

from cib_content_page.blocks.address import AddressBlock
from cib_content_page.blocks.custom_image import CustomImageBlock
from cib_content_page.blocks.heading_block import HeadingBlock
from cib_content_page.blocks.table import TinyMCETableBlock
from cib_content_page.blocks.video import VideoBlock
from cib_utils.models import BasePage
from django.db import models
from wagtail import blocks

from .blocks import BoardMembersCardBlock

IMAGE_MODEL = get_image_model_string()


class BoardPage(BasePage):
    template = "patterns/pages/board_page.html"
    left_nav_title = models.TextField(
        blank=False,
        null=True
    )
    body = StreamField(
        [
            ("BoardMembersCards", BoardMembersCardBlock()),
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
        blank=True,
    )
    jobvacancy_latestnews_snippet = models.ForeignKey(
        'utils.JobsVacanciesAndLatestNewsSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    news_letter_signup_cta = models.ForeignKey(
        'utils.NewsletterSignUpCTASnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_panels = BasePage.content_panels + [
        FieldPanel("left_nav_title"),
        FieldPanel("body"),
        FieldPanel("jobvacancy_latestnews_snippet"),
        FieldPanel("news_letter_signup_cta")
    ]
