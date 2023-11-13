from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.models import TranslatableMixin, PreviewableMixin

from wagtail.snippets.models import register_snippet

from .blocks import (
    LinkBlockWithURL
)


from wagtail.models import DraftStateMixin, RevisionMixin
from django.contrib.contenttypes.fields import GenericRelation
from wagtail.admin.panels import PublishingPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager
from wagtail.images import get_image_model_string
from wagtail.contrib.settings.models import BaseSetting, register_setting


IMAGE_MODEL = get_image_model_string()


ALT_HELP_TEXT = """A short one-sentence literal description
                    of the %s is
                    required to make the page accessible to the
                    visually impaired. Details: https://axesslab.com/alt-texts/"""

ALT_IMAGE = ALT_HELP_TEXT % 'image'


@register_setting(icon="list-ul")
class SiteSettings(BaseSetting, ClusterableModel):
    # The settings here are currently unused.
    favicon = models.ForeignKey(
        IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    site_logo = models.ForeignKey(
        IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    mobile_logo = models.ForeignKey(
        IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    site_logo_alt = models.CharField(
        max_length=255,
        blank=False,
        verbose_name=_("Logo Alt text"),
        help_text=_(ALT_IMAGE),
    )

    panels = [
        MultiFieldPanel([
            FieldPanel("favicon"),
            FieldPanel("site_logo"),
            FieldPanel("site_logo_alt"),
        ], heading="Site Logo"),
    ]


class PrimaryNavigationTag(TaggedItemBase):
    content_object = ParentalKey('cib_navigation.PrimaryNavigation', on_delete=models.CASCADE,
                                 related_name='tagged_items')


@register_snippet
class PrimaryNavigation(PreviewableMixin, DraftStateMixin, RevisionMixin, index.Indexed, ClusterableModel,
                        TranslatableMixin):
    # Snippets model is used so the navigation can be localised with TranslatableMixin.
    tags = TaggableManager(through=PrimaryNavigationTag, blank=True)
    title = models.CharField(max_length=255, blank=True)

    lang = models.CharField(
        max_length=255,
        unique=True,
        help_text="Internal name for this navigation, it's not displayed to a site user.",
        verbose_name=_("Language"),
    )
    navigation = StreamField(
        [("link", LinkBlockWithURL())],
        blank=True,
        help_text="Main site navigation",
        verbose_name=_("Links"),
    )
    _revisions = GenericRelation("wagtailcore.Revision", related_query_name="primarynavigation")

    panels = [
        FieldPanel("title"),
        MultiFieldPanel(
            [
                FieldPanel("lang"),
                FieldPanel("navigation"),
            ],
            heading=_("Primary Navigation"),
        ),
        FieldPanel('tags'),
        PublishingPanel(),
    ]

    search_fields = [
        index.FilterField('locale_id'),
        index.SearchField("title", partial_match=True),
    ]

    def get_preview_template(self, request, mode_name):
        return "patterns/snippets/customheadersnippet.html"

    @property
    def revisions(self):
        return self._revisions

    def __str__(self):
        return self.lang

    class Meta:
        verbose_name = _("Primary Navigation")
        verbose_name_plural = _("Primary Navigation")
        unique_together = ("translation_key", "locale")
