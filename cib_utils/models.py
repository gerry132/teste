# -*- coding: utf-8 -*-
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.decorators import method_decorator
from django.db import models
from modelcluster.models import ClusterableModel

from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    FieldRowPanel,
    HelpPanel, TabbedInterface, ObjectList, PublishingPanel,
)

from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page, PreviewableMixin, DraftStateMixin, RevisionMixin, TranslatableMixin
from wagtail.images import get_image_model_string
from wagtail.snippets.models import register_snippet
from django.utils.translation import gettext_lazy as _
from wagtail.search import index

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

    publication_log = RichTextField(
        features=[], blank=True, null=True,
        help_text="Put your comment for current changes",
        verbose_name=_("publication_log")
    )

    content_panels = Page.content_panels + [
        FieldPanel("publication_log"),
    ]

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
        max_num=1
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

    content_panels = BasePage.content_panels + [
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(hero_panel, heading='Hero'),
        ObjectList(BasePage.promote_panels, heading='Promote'),
        ObjectList(BasePage.settings_panels, heading='Settings', classname="settings"),
    ])


@register_snippet
class NewsletterSignUpCTASnippet(PreviewableMixin, DraftStateMixin, RevisionMixin, index.Indexed, ClusterableModel,
                                 TranslatableMixin, models.Model):
    snippet_title = models.CharField(max_length=255, blank=True)
    icon = models.ForeignKey(
        IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    icon_alt = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Icon Alt text"),
        help_text=_("The alt text shown for accessibility: https://axesslab.com/alt-texts/")
    )
    title = models.CharField(max_length=255, blank=True)
    body = RichTextField(features=["h3", "h4", "h5", "bold", "italic", "link", "document-link"],
                         blank=True, null=True)
    button_text = models.CharField(max_length=255, blank=True)
    url = models.URLField(blank=True)
    _revisions = GenericRelation("wagtailcore.Revision", related_query_name="betasnippet")
    panels = [
        FieldPanel("snippet_title"),
        FieldPanel("icon"),
        FieldPanel("icon_alt"),
        FieldPanel("title"),
        FieldPanel("body"),
        FieldPanel("button_text"),
        FieldPanel("url"),
        PublishingPanel(),
    ]

    search_fields = [
        index.SearchField("snippet_title", partial_match=True),
    ]

    def get_preview_template(self, request, mode_name):
        return "patterns/snippets/newslettersignupctasnippet.html"

    @property
    def revisions(self):
        return self._revisions

    class Meta:
        unique_together = ("translation_key", "locale")
