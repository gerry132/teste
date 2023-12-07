from cib_utils.models import BasePage
from django.utils.translation import gettext_lazy as _

from cib_images.models import CustomImage


class News(BasePage):
    "Main whats new page"
    template = "patterns/pages/news.html"
    # parent_page_types = ["cib_home.HomePage"]

    def childs(self, req="None"):
        """Get all child based on the filter"""
        # @todo get all chils pages attributes
        pass

    class Meta:
        verbose_name = _("news page")
        verbose_name_plural = _("news pages")

    def get_context(self, request, *args, **kwargs):

        context = super().get_context(request, *args, **kwargs)
        context['sample_image'] = CustomImage.objects.filter(title="president").first()

        return context
