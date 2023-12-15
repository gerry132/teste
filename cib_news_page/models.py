
from django.utils.translation import gettext_lazy as _

from cib_utils.models import BasePage
from cib_images.models import CustomImage
from cib_news_content_page.models import NewsContentPage


class News(BasePage):
    "Main whats new page"
    template = "patterns/pages/news.html"
    # parent_page_types = ["cib_home.HomePage"]

    def childs(self, req=None):
        """Get all child based on the filter"""
        main_childs = NewsContentPage.objects.\
            descendant_of(self).live().order_by("-last_published_custom")

        # if req and main_childs:
        #     if req.get('new_tags', None):
        #         return main_childs.filter(
        #             news_tags__slug=req.get('news_tags', None))
        #     date = req.get('news_date', None)
        #     try:
        #         if date and len(date.split('-')) > 0:
        #             return main_childs.filter(
        #                 last_published_custom__month=date.split('-')[1],
        #                 last_published_custom__year=date.split('-')[0])

        #         year = req.get('news_year', None)
        #         if year:
        #             return main_childs.filter(last_published_custom__year=year)
        #     except: # noqa
        #         return main_childs
        return main_childs

    class Meta:
        verbose_name = _("news page")
        verbose_name_plural = _("news pages")

    def get_context(self, request, *args, **kwargs):

        context = super().get_context(request, *args, **kwargs)
        context["child_with_tags"] = self.childs(request)
        context['sample_image'] = CustomImage.objects.filter(title="president").first()

        return context
