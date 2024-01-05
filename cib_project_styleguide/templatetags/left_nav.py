from django import template

register = template.Library()


def get_children_pages(current_page, depth):
    return current_page.get_children().filter(
        depth=depth,
        live=True,
        locale=current_page.locale,
    ).specific()


@register.inclusion_tag('patterns/organisms/left_nav.html', takes_context=True)
def left_nav(context, current_page):
    depth = current_page.depth
    sub_child_pages = None
    parent_page = None
    children_pages = None
    grandchild_pages = None

    if depth == 3:
        children_pages = get_children_pages(current_page, depth + 1)
    elif depth == 4:
        parent_page = current_page.get_parent().specific
        children_pages = get_children_pages(parent_page, depth)
        sub_child_pages = (current_page.get_children().filter(depth=depth + 1, live=True, locale=current_page.locale)
                           .specific())
    elif depth == 5:
        parent_page = current_page.get_ancestors(inclusive=True).filter(depth=depth - 2, live=True,
                                                                        locale=current_page.locale).specific()
        children_pages = get_children_pages(parent_page.first(), depth - 1)
        sub_child_pages = (current_page.get_siblings().filter(depth=depth, live=True, locale=current_page.locale)
                           .specific())
        grandchild_pages = (current_page.get_children().filter(depth=depth + 1, live=True, locale=current_page.locale)
                            .specific())

    return {
        'current_page': current_page,
        'parent_page': parent_page,
        'children_pages': children_pages,
        'sub_child_pages': sub_child_pages,
        'grandchild_pages': grandchild_pages,
    }
