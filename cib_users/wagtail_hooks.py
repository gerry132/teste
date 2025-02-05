# -*- coding: utf-8 -*-

from django.templatetags.static import static
from django.utils.html import format_html
from wagtail.admin.menu import MenuItem
from wagtail import hooks

from wagtailcache.cache import clear_cache


@hooks.register("after_create_page")
@hooks.register("after_edit_page")
def clear_wagtailcache(request, page):
    if page.live:
        clear_cache(
            [
                page.full_url,
                page.get_parent().full_url,
                page.get_url_parts()[1],
            ]
        )


@hooks.register("insert_global_admin_css", order=99)
def global_admin_css():
    """Add /static/css/custom.css to the admin."""
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static("/irelandie_assets/css/custom.css")
    )


@hooks.register("insert_global_admin_js", order=100)
def global_admin_js():
    """Add /static/css/custom.js to the admin."""
    return format_html(
        '<script src="{}"></script>',
        static("/irelandie_assets/js/custom.js")
    )


# Register shortcut to access django-defender's
class DjangoAdminMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_superuser

# @hooks.register("register_settings_menu_item")
# def register_locked_accounts_menu_item():
#     return DjangoAdminMenuItem(
#         "Locked accounts",
#         reverse("defender_blocks_view"),
#         icon_name="lock",
#         order=601,
#     )
