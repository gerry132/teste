from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.admin.panels import FieldPanel
from .models import JobVacanciesTag


class TagsModelAdmin(ModelAdmin):
    JobVacanciesTag.panels = [FieldPanel("name"), FieldPanel("slug"), FieldPanel("description"),
                              FieldPanel("locale")]
    add_to_settings_menu = True
    model = JobVacanciesTag
    menu_label = "Job Company Tags"
    menu_icon = "tag"
    menu_order = 1000
    list_display = ['name', 'description', 'locale']
    search_fields = ('name', 'description')


modeladmin_register(TagsModelAdmin)
