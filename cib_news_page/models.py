
from django.utils.translation import gettext_lazy as _
from django.utils.functional import cached_property
from django.db.models.functions import TruncYear
from django.db.models import Count

from cib_utils.models import BasePage
from cib_news_content_page.models import NewsContentPage, NewsTag


class News(BasePage):
    "Main whats new page"
    template = "patterns/pages/news.html"
    # parent_page_types = ["cib_home.HomePage"]

    @cached_property
    def all_news_page(self):
        return NewsContentPage.objects.all()

    @property
    def years(self):
        years = []
        try:
            all_years = self.all_news_page.annotate(
                year=TruncYear('last_published_custom')
                ).values('year').annotate(count=Count('id')).order_by('-year')

            for year in all_years:
                if year['year']:
                    years.append(year['year'].strftime('%Y'))
            return years
        except: # noqa
            return

    def childs(self, req=None):
        """Get all child based on the filter"""
        childs = self.all_news_page.\
            descendant_of(self).live().order_by("-last_published_custom")
        try:
            if req and childs:
                if req.get('news_tags', None):
                    childs = childs.filter(
                        news_tags__slug=req.get('news_tags', None))

                if req.get('news_year', None):
                    childs = childs.filter(last_published_custom__year=req.get('news_year', None))
                return childs
        except: # noqa
            return childs
        return childs

    class Meta:
        verbose_name = _("news page")
        verbose_name_plural = _("news pages")

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["child_with_tags"] = self.childs(request.GET)
        context['all_tags'] = NewsTag.objects.all()
        context['selected_year'] = request.GET.get('news_year')
        context['selected_tag'] = request.GET.get('news_tags')
        return context
