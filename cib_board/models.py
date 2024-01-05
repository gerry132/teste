from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.images import get_image_model_string

from cib_utils.models import BasePage
from django.db import models

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
        ],
        use_json_field=True,
        null=True,
        blank=True,
        min_num=0,
        max_num=1,
    )
    content_panels = BasePage.content_panels + [
        FieldPanel("left_nav_title"),
        FieldPanel("body")
    ]
