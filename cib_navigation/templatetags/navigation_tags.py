from wagtail.models import Locale
from django import template
from functools import lru_cache

from cib_navigation.models import (
    PrimaryNavigation,
)


register = template.Library()


@lru_cache(maxsize=None)
def default_language():
    return Locale.objects.get(language_code="en")


def get_nav_for_locale(cls, locale):
    navigation = None

    try:
        navigation = cls.objects.get(locale=locale).navigation
    except cls.DoesNotExist:
        pass

    if not navigation:
        try:
            navigation = cls.objects.get(locale=default_language()).navigation
        except cls.DoesNotExist:
            pass

    return navigation



@register.simple_tag
def primarynav(context, page, override=None):
    request = context["request"]
    locale = Locale.objects.get(language_code=request.LANGUAGE_CODE)
    root_found = False

    navigation = get_nav_for_locale(PrimaryNavigation, locale)
    return {
        "primarynav": navigation,
        "request": request,
    }

