# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator

from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
)

from wagtail.search import index
from wagtail.models import Page
from cib_utils.cache import get_default_cache_control_decorator


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
