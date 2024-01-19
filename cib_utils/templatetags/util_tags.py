from django import template

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
