# -*- coding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.db import models

from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    FieldRowPanel,
    HelpPanel, TabbedInterface, ObjectList,
)

from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.images import get_image_model_string
from cib_home.blocks import CallOutBlock
from cib_utils.blocks import BaseFeatureBlock

from cib_utils.cache import get_default_cache_control_decorator


IMAGE_MODEL = get_image_model_string()

ALT_HELP_TEXT = """A short one-sentence literal description
                    of the %s is
                    required to make the page accessible to the
                    visually impaired. Details: https://axesslab.com/alt-texts/"""


# Apply default cache headers on this page model's serve method.
@method_decorator(get_default_cache_control_decorator(), name="serve")
class BasePage(Page):
    show_in_menus_default = True

    class Meta:
        abstract = True

    COMMON_PROMOTE_PANELS = (
        FieldPanel('slug', permission="access_admin"),
        FieldPanel('seo_title', permission="access_admin"),
        FieldPanel('search_description', permission="access_admin"),
    )

    promote_panels = (
        [
            MultiFieldPanel(COMMON_PROMOTE_PANELS, heading="For search engines"),
            FieldPanel('show_in_menus'),
        ]
    )

    settings_panels = ([
                           MultiFieldPanel(
                               [
                                   FieldPanel('go_live_at', permission="access_admin"),
                                   FieldPanel('expire_at', permission="access_admin"),
                               ],
                               "Scheduled publishing"
                           ),
                        ]
                       )


class HeroPage(BasePage):
    """
    Abstract class to enable
    hero images on specified pages.
    """
    hero_image = models.ForeignKey(
        IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    alt_text = models.CharField(blank=True,
                                null=True,
                                max_length=255,
                                help_text=ALT_HELP_TEXT)
    hero_double_feature = StreamField(
        [
            ("feature_block", BaseFeatureBlock()),
        ],
        blank=True,
        min_num=2,
        max_num=2
    )

    callout_feature = StreamField(
        [
            ("callout_cards", CallOutBlock())
        ],
        blank=True,
        max_num=3
    )

    class Meta:
        abstract = True

    hero_panel = [
        HelpPanel("For the hero to display you must set the image field below."),
        FieldRowPanel([
            FieldPanel("hero_image", classname="col6"),
        ], "Hero Media"),
        FieldPanel("alt_text"),
        FieldPanel('hero_double_feature'),
        FieldPanel('callout_feature')]

    content_panels = Page.content_panels + [
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(hero_panel, heading='Hero'),
        ObjectList(BasePage.promote_panels, heading='Promote'),
        ObjectList(BasePage.settings_panels, heading='Settings', classname="settings"),
    ])
