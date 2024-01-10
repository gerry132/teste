from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.models import TranslatableMixin, PreviewableMixin

from wagtail.snippets.models import register_snippet

from .blocks import (
    LinkBlockWithURL, LinkColumnWithHeader
)

from wagtail.models import DraftStateMixin, RevisionMixin
from django.contrib.contenttypes.fields import GenericRelation
from wagtail.admin.panels import PublishingPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager
from wagtail.images import get_image_model_string
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

IMAGE_MODEL = get_image_model_string()

# TODO: make a const.py file
ALT_HELP_TEXT = """A short one-sentence literal description
                    of the %s is
                    required to make the page accessible to the
                    visually impaired. Details: https://axesslab.com/alt-texts/"""

IMAGE_HELP_TEXT = """The image size should be 255x71 pixels"""

ALT_IMAGE = ALT_HELP_TEXT % 'image'


@register_setting(icon="list-ul")
class SiteSettings(BaseSiteSetting, ClusterableModel):
    # The settings here are currently unused.
    pagination_count = models.IntegerField(default=10)
    favicon = models.ForeignKey(
        IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    site_english_logo = models.ForeignKey(
        IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=IMAGE_HELP_TEXT
    )
    mobile_logo = models.ForeignKey(
        IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    site_english_logo_alt = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_("Logo Alt text"),
        help_text=_(ALT_IMAGE),
    )
    site_irish_logo = models.ForeignKey(
        IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=IMAGE_HELP_TEXT
    )
    site_irish_logo_alt = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_("Logo Alt text"),
        help_text=_(ALT_IMAGE),
    )

    panels = [
        MultiFieldPanel([
            FieldPanel("favicon"),
            FieldPanel("site_english_logo"),
            FieldPanel("site_english_logo_alt"),
            FieldPanel("site_irish_logo"),
            FieldPanel("site_irish_logo_alt"),
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
        use_json_field=True
    )
    popular_links = StreamField(
        [("popular_link", LinkBlockWithURL())],
        blank=True,
        help_text="Popular links for search",
        verbose_name=_("Popular Links"),
        use_json_field=True
    )
    _revisions = GenericRelation("wagtailcore.Revision", related_query_name="primarynavigation")

    panels = [
        FieldPanel("title"),
        MultiFieldPanel(
            [
                FieldPanel("lang"),
                FieldPanel("navigation"),
                FieldPanel("popular_links"),
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

    def clean(self):
        if PrimaryNavigation.objects.exclude(id=self.id).filter(lang=self.lang).exists():
            raise ValidationError('Only one instance of PrimaryNavigation snippet is allowed for each language.')

    class Meta:
        verbose_name = _("Primary Navigation")
        verbose_name_plural = _("Primary Navigation")
        unique_together = ("translation_key", "locale")


class FooterNavigationTag(TaggedItemBase):
    content_object = ParentalKey('cib_navigation.FooterNavigation', on_delete=models.CASCADE,
                                 related_name='tagged_items')


@register_snippet
class FooterNavigation(PreviewableMixin, DraftStateMixin, RevisionMixin, index.Indexed, ClusterableModel,
                       TranslatableMixin):
    # Snippets model is used so the navigation can be localised with TranslatableMixin.
    tags = TaggableManager(through=FooterNavigationTag, blank=True)
    title = models.CharField(max_length=255, blank=True)
    lang = models.CharField(
        max_length=255,
        unique=True,
        help_text="Internal name for this navigation, it's not displayed to a site user.",
        verbose_name=_("Language"),
    )
    logo = models.ForeignKey(
        IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    logo_alt = models.CharField(
        max_length=255,
        blank=False,
        verbose_name=_("Logo Alt text"),
        help_text=_(ALT_IMAGE),
    )
    navigation = StreamField(
        [("two_colum_list", LinkColumnWithHeader()),
         ("single_colum_list", LinkColumnWithHeader()),
         ("single_column_address", blocks.StructBlock(
             [("heading", blocks.CharBlock()), ("address", blocks.RichTextBlock())],
             icon="link",
         ))],
        block_counts={
            'two_colum_list': {'max_num': 1},
            'single_colum_list': {'max_num': 1},
            'single_column_address': {'max_num': 1},
        },
        blank=True,
        max_num=2,
        help_text="Multiple columns of footer links with optional header.",
        verbose_name=_("Columns"),
    )
    links = StreamField(
        [("link", LinkBlockWithURL())],
        blank=True,
        help_text=_("Single list of elements at the base of the page."),
    )

    _revisions = GenericRelation("wagtailcore.Revision", related_query_name="footernavigation")

    panels = [
        FieldPanel("title"),
        MultiFieldPanel(
            [
                FieldPanel("lang"),
                FieldPanel("logo"),
                FieldPanel("logo_alt"),
                FieldPanel("navigation"),
                FieldPanel("links"),
            ],
            heading=_("Footer Navigation"),
        ),
        FieldPanel('tags'),
        PublishingPanel(),
    ]

    search_fields = [
        index.FilterField('locale_id'),
        index.SearchField("title", partial_match=True),
    ]

    def get_preview_template(self, request, mode_name):
        return "patterns/snippets/customfootersnippet.html"

    @property
    def revisions(self):
        return self._revisions

    def __str__(self):
        return self.lang

    def clean(self):
        if FooterNavigation.objects.exclude(id=self.id).filter(lang=self.lang).exists():
            raise ValidationError('Only one instance of FooterNavigation snippet is allowed for each language.')

    class Meta:
        verbose_name = _("Footer Navigation")
        verbose_name_plural = _("Footer Navigation")
        unique_together = ("translation_key", "locale")
