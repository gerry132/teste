from django.db import models

from wagtail.core.fields import StreamField
from wagtail.images import get_image_model_string

from wagtail.admin.panels import (
    FieldPanel, TabbedInterface, ObjectList,
)


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
        ],
        use_json_field=True,
        null=True,
        blank=True
    )
    content_panels = HeroPage.content_panels + [
        FieldPanel("body")
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(HeroPage.hero_panel, heading='Hero'),
        ObjectList(HeroPage.promote_panels, heading='Promote'),
        ObjectList(HeroPage.settings_panels, heading='Settings', classname="settings"),
    ])
