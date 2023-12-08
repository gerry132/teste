
from wagtail import hooks
from wagtail.log_actions import LogFormatter
from wagtail.log_actions import log
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from wagtail_localize.models import Translation, TranslationSource

from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _

from wagtail.admin.menu import MenuItem

from .views import PublicationLogReportsView

from django.utils.html import format_html

from bs4 import BeautifulSoup

from .models.main_models import PageTag, TaggedPage


class TagsModelAdmin(ModelAdmin):
    PageTag.panels = [FieldPanel("name"), FieldPanel("description")]
    model = PageTag
    add_to_settings_menu = True
    menu_label = "Add Page Tags"
    menu_icon = "tag"
    menu_order = 1000  # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ["name", "slug"]
    search_fields = ("name", "description")


class PageTagsModelAdmin(ModelAdmin):
    TaggedPage.panels = [FieldPanel("tag"), FieldPanel("content_object")]
    model = TaggedPage
    add_to_settings_menu = True
    menu_label = "Search Tagged Pages"
    menu_icon = "search"
    menu_order = 1000
    list_display = ["tag", "page", "slug", "language"]
    search_fields = ("tag__name", "content_object__slug")

    def page(self, obj):
        url = obj.content_object.url if obj.content_object else None
        if url:
            return format_html('<a href="{}" target="_blank">{}</a>',
                               url, obj.content_object.title)
        else:
            return "-"

    def slug(self, obj):
        slug = obj.content_object.slug if obj.content_object else None
        return slug

    def language(self, obj):
        lang = obj.content_object.locale if obj.content_object else None
        return lang


modeladmin_register(TagsModelAdmin)
modeladmin_register(PageTagsModelAdmin)


@hooks.register('register_reports_menu_item')
def register_publication_log_report_menu_item():
    return MenuItem(
        "Site history with publication log",
        reverse('publication_log_reports'),
        icon_name=PublicationLogReportsView.header_icon, order=700)


@hooks.register('register_admin_urls')
def register_publication_log_report_url():
    return [
        path('reports/history-with-publication-log/',
             PublicationLogReportsView.as_view(),
             name='publication_log_reports'),
    ]


@hooks.register('register_log_actions')
def additional_log_actions(actions):
    """Add a new log action with the name core.changes_review"""
    @actions.register_action('core.changes_review')
    class ChangeCustomComment(LogFormatter):
        label = _('Publication log entered')

        def format_message(self, log_entry):
            return _(f'Publication log: {log_entry.data}')


@hooks.register("after_edit_page")
@hooks.register("after_create_page")
def update_publication_log(request, page, **kwargs):
    """Signal for update publication log"""
    global last_message
    try:

        result = ""
        if page and page.publication_log\
           and page.publication_log != "":
            result = BeautifulSoup(
                page.publication_log, 'lxml').text

            if result:
                log(
                    instance=page,
                    action="core.changes_review",
                    user=request.user,
                    data=str(result),
                )
                last_message = result

                page.publication_log = ""
                page.save(update_fields=["publication_log"])

    except RuntimeError:
        print("Revision already saved.")


@hooks.register('after_publish_page')
def after_publish_page_update_translations(request, page):
    """Update translations when original page is saved."""
    print(11111111111)
    print(11111111111)
    print(11111111111)
    print(11111111111)
    print(11111111111)
    print(11111111111)
    print(11111111111)
    if hasattr(page, "translation_key"):
        print('aaaaa')
        # Update translation source (this stores synched fields, e.g. tags and coordinates)
        TranslationSource.update_or_create_from_instance(page)

        translated_pages = Page.objects.filter(
            translation_key=page.translation_key).exclude(id=page.id)
        print(translated_pages)
        for translated_page in translated_pages:
            # Update each translation with the new synched field values
            translation = Translation.objects.filter(
                source__object_id=page.translation_key,
                target_locale_id=translated_page.locale_id,
                enabled=True,
            ).first()
            if translation:
                translation.save_target(request.user)
