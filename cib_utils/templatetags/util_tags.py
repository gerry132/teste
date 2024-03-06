from django import template
from django.db.models import Count
from django.db.models.functions import TruncYear

from cib_news_content_page.models import NewsContentPage

register = template.Library()


@register.filter
def get_first_richtext(blocks):
    for block in blocks:
        if block.block_type == 'richtext':
            return block.value
    return ''


@register.simple_tag
def define_document_language(language_code, val=None):
    for link in val:
        if language_code == 'en' and link['heading'] == 'English':
            return link
        elif language_code == 'ga' and link['heading'] == 'Gaeilge':
            return link

    return False


@register.simple_tag
def get_news_years():
    try:
        all_years = NewsContentPage.objects.annotate(
            year=TruncYear('last_published_custom')
        ).values('year').annotate(count=Count('id')).order_by('-year')

        years = [year['year'].strftime('%Y') for year in all_years if year['year']]
        return years
    except:  # noqa
        return []
