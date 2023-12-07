from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from cib_documents.models import YearTag, DocumentTypeTag


class YearTagAdmin(ModelAdmin):
    model = YearTag
    menu_label = 'Year Tags'
    menu_icon = 'tag'
    menu_order = 900
    add_to_settings_menu = True
    list_display = ['name',]
    search_fields = ('name',)


modeladmin_register(YearTagAdmin)


class DocumentTypeTagAdmin(ModelAdmin):
    model = DocumentTypeTag
    menu_label = 'Publication Type Tags'
    menu_icon = 'tag'
    menu_order = 901
    add_to_settings_menu = True
    list_display = ['name',]
    search_fields = ('name',)


modeladmin_register(DocumentTypeTagAdmin)
