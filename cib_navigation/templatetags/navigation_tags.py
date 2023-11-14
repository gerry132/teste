from wagtail.models import Locale
from django import template
from functools import lru_cache

from cib_navigation.models import (
    PrimaryNavigation,
    SiteSettings
)


register = template.Library()


@lru_cache(maxsize=None)
def default_language():
    return Locale.objects.get(language_code="en")


def get_nav_for_locale(cls, locale):
    navigation = None

    try:
        navigation = cls.objects.get(locale=locale).navigation
        print(navigation)
        print(1)
    except cls.DoesNotExist:
        pass

    if not navigation:
        try:
            navigation = cls.objects.get(locale=default_language()).navigation
            print(navigation)
            print(2)
        except cls.DoesNotExist:
            pass

    return navigation


@register.simple_tag(takes_context=True)
def primarynav(context):

    request = context["request"]
    locale = Locale.objects.get(language_code=request.LANGUAGE_CODE)
    site_settings = SiteSettings.for_request(request)
    navigation = get_nav_for_locale(PrimaryNavigation, locale)
    return {
        "primarynav": navigation,
        "request": request,
        "site_settings": site_settings
    }
