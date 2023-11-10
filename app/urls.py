# -*- coding: utf-8 -*-
from django.conf import settings as dj_settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import RedirectView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap

from wagtail.api.v2.router import WagtailAPIRouter

from cib_utils.views import PagesAPIEndpoint, set_language_wagtail
from cib_search import views as search_views

PREFIX_DEFAULT_LANGUAGE = getattr(
    dj_settings,
    'PREFIX_DEFAULT_LANGUAGE',
    True
)

# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')
api_router.register_endpoint('pages', PagesAPIEndpoint)

urlpatterns = [
    path('', include('health_check.urls')),
    path('django-admin/', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),
    path("search/", search_views.search, name="search"),
    path('sitemap.xml', sitemap),
    path('', include(wagtaildocs_urls)),
    path("api/v2/", api_router.urls),
]

#if dj_settings.DEBUG_TOOLBAR is True:
#    import debug_toolbar

#    urlpatterns += [
#        path('__debug__/', include(debug_toolbar.urls)),
#    ]

if dj_settings.USE_S3 is True:
    urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(
    dj_settings.MEDIA_URL,
    document_root=dj_settings.MEDIA_ROOT
)

urlpatterns += i18n_patterns(
    # set up set language redirect view
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include(wagtail_urls)),
    path('i18n/set_language_wagtail', set_language_wagtail, name="set_language_wagtail"),
    prefix_default_language=PREFIX_DEFAULT_LANGUAGE,
)

urlpatterns += [
    path(
        '',
        RedirectView.as_view(url=f'/{dj_settings.LANGUAGE_CODE}/'),
        name='no-language-home'
    ),
]


handler404 = 'cib_utils.views.page_not_found'
handler500 = 'cib_utils.views.server_error'
