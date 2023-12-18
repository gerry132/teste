from django import template

register = template.Library()


@register.filter
def get_first_richtext(blocks):
    for block in blocks:
        if block.block_type == 'richtext':
            return block.value
    return ''
