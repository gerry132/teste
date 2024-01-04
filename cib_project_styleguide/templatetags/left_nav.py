from django import template

register = template.Library()


@register.inclusion_tag('patterns/organisms/left_nav.html', takes_context=True)
def left_nav(context, current_page):
    depth = current_page.depth
    sub_child_pages = None
    parent_page = None
    children_pages = None
    grandchild_pages = None

    if depth == 3:
        children_pages = current_page.get_children().filter(depth=depth + 1)
    elif depth == 4:
        parent_page = current_page.get_parent()
        children_pages = parent_page.get_children().filter(depth=depth)
        sub_child_pages = current_page.get_children().filter(depth=depth + 1)
    elif depth == 5:
        parent_page = current_page.get_ancestors(inclusive=True).filter(depth=depth - 2)
        children_pages = parent_page.first().get_children().filter(depth=depth - 1)
        sub_child_pages = current_page.get_siblings().filter(depth=depth)
        grandchild_pages = current_page.get_children().filter(depth=depth + 1)

    return {
        'current_page': current_page,
        'parent_page': parent_page,
        'children_pages': children_pages,
        'sub_child_pages': sub_child_pages,
        'grandchild_pages': grandchild_pages if depth == 5 else None,
    }
