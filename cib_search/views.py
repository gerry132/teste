# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.utils.cache import add_never_cache_headers, patch_cache_control
from django.core.exceptions import ObjectDoesNotExist

from .models import SearchTerm

from wagtail.models import Page, Site
from cib_utils.cache import get_default_cache_control_kwargs

from wagtail.search.backends import get_search_backend
from wagtail.search.query import Fuzzy


def search(request):
    root_page = Site.find_for_request(request).root_page.localized
    search_query = request.GET.get("q", None)
    page = request.GET.get("page", 1)

    if search_query:
        s = get_search_backend()

        if hasattr(s, 'settings'):
            search_results = (
                Page.objects.live().public()
                    .descendant_of(root_page)
                    .search(Fuzzy(search_query), partial_match=False)
            )
            try:
                search_term = SearchTerm.objects.get(search_term=search_query)
                search_term.count += 1
            except ObjectDoesNotExist:
                print("Either the blog or entry doesn't exist.")
                search_term = SearchTerm(search_term=search_query, count=1)
            search_term.save()
        else:
            search_results = (
                Page.objects.live().public()
                    .descendant_of(root_page)
                    .search(search_query)
            )
    else:
        search_results = Page.objects.none()
    # Pagination
    paginator = Paginator(search_results, settings.DEFAULT_PER_PAGE)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)
    print('paginator')
    print(paginator.page_range)
    print('paginator')
    page_range = paginator.get_elided_page_range(number=page)
    response = TemplateResponse(
        request,
        "patterns/pages/search/search.html",
        {"search_query": search_query, "search_results": search_results, "page_range": page_range "page": page, "paginator": paginator},
    )

    if search_query:
        add_never_cache_headers(response)
    else:
        patch_cache_control(response, **get_default_cache_control_kwargs())
    return response
