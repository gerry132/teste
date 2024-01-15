
from django.utils.translation import gettext_lazy as _
from django.utils.functional import cached_property
from django.db.models.functions import TruncYear
from django.db.models import Count
from django.utils.translation import get_language
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.conf import settings
from django.db import models

from cib_utils.models import BasePage
from cib_news_content_page.models import NewsContentPage, NewsTag
from cib_utils.blocks import SelectComponentBlock

from wagtail.core.fields import StreamField
from wagtail.admin.panels import FieldPanel


class News(BasePage):
    "Main whats new page"
    template = "patterns/pages/news.html"
    parent_page_types = ["cib_home.HomePage"]

    news_tag_select_component = StreamField([
        ('news_tag_select_component', SelectComponentBlock()),
    ], blank=False, null=True, max_num=1)
    year_select_component = StreamField([
        ('year_select_component', SelectComponentBlock()),
    ], blank=False, null=True, max_num=1)
    jobvacancy_latestnews_snippet = models.ForeignKey(
        'utils.JobsVacanciesAndLatestNewsSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    news_letter_signup_cta = models.ForeignKey(
        'utils.NewsletterSignUpCTASnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = BasePage.content_panels + [
        FieldPanel('news_tag_select_component'),
        FieldPanel('year_select_component'),
        FieldPanel("jobvacancy_latestnews_snippet"),
        FieldPanel("news_letter_signup_cta"),
    ]

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

    def paginate(self, request):
        paginator = Paginator(self.childs(request.GET), settings.DEFAULT_PER_NEWS_PAGE)
        page = request.GET.get("page")

        try:
            childs = paginator.page(page)
        except PageNotAnInteger:
            childs = paginator.page(1)
        except EmptyPage:
            childs = paginator.page(paginator.num_pages)
        return childs

    def get_tages(self):
        current_lang = get_language()
        all_tags = NewsTag.objects.all()
        exist_lang = all_tags.values_list('locale', flat=True).distinct()
        if current_lang in exist_lang:
            return all_tags.filter(locale=current_lang)
        return

    class Meta:
        verbose_name = _("news page")
        verbose_name_plural = _("news pages")

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["child_with_tags"] = self.paginate(request)
        context['all_tags'] = self.get_tages()
        context['selected_year'] = request.GET.get('news_year')
        context['selected_tag'] = request.GET.get('news_tags')
        return context
