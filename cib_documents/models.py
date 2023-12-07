# -*- coding: utf-8 -*-
from taggit.models import TagBase
from wagtail.documents.models import AbstractDocument
from wagtail.documents.models import Document as WagtailDocument
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _
from cib_utils.models import BasePage

from cib_navigation.models import ALT_HELP_TEXT

ALT_IMAGE = ALT_HELP_TEXT % 'image'


class CustomDocument(AbstractDocument):
    admin_form_fields = WagtailDocument.admin_form_fields


class Tag(TagBase):
    free_tagging = False

    class Meta:
        abstract = True


class YearTag(Tag):
    class Meta:
        verbose_name = "Year Tag"
        verbose_name_plural = "Year Tags"


class DocumentTypeTag(Tag):
    class Meta:
        verbose_name = "Publication Type Tag"
        verbose_name_plural = "Publication Type Tags"


def get_year_tag_choices():
    return [(tag.slug, tag.name) for tag in YearTag.objects.all()]


def get_document_type_tag_choices():
    return [(tag.slug, tag.name) for tag in DocumentTypeTag.objects.all()]


