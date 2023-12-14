from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.admin.panels import FieldPanel
from .models import NewsTag


class TagsModelAdmin(ModelAdmin):
    NewsTag.panels = [FieldPanel("name"), FieldPanel("slug")]
    add_to_settings_menu = True
    model = NewsTag
    menu_label = "News Tags"
    menu_icon = "tag"
    menu_order = 1000
    list_display = ["name"]
    search_fields = ("name",)


modeladmin_register(TagsModelAdmin)
