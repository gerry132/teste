from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.images import get_image_model_string

from cib_utils.models import BasePage

from .blocks import CallOutBlock, InfoPanelBlock, JobsVacanciesBlock, BoardMembersCardBlock

IMAGE_MODEL = get_image_model_string()


class HomePage(BasePage):
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
            ("JobVacanciesAndNewsCard", JobsVacanciesBlock()),
        ],
        use_json_field=True,
        null=True,
        blank=True
    )
    content_panels = BasePage.content_panels + [
        FieldPanel("body")
    ]


class BoardPage(BasePage):
    template = "patterns/pages/board_page.html"

    body = StreamField(
        [
            ("BoardMembersCards", BoardMembersCardBlock()),
        ],
        use_json_field=True,
        null=True,
        blank=True,
        min_num=0,
        max_num=1,
    )
    content_panels = BasePage.content_panels + [
        FieldPanel("body")
    ]
