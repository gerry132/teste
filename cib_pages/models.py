
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.images import get_image_model_string

from cib_utils.models import BasePage

from cib_home.blocks import CallOutBlock, InfoPanelBlock, BoardMembersCardBlock

IMAGE_MODEL = get_image_model_string()


class FreeFormPage(BasePage):
    template = "patterns/pages/free_form_page.html"

    body = StreamField(
        [
            ("CalloutCards", CallOutBlock()),
            ("InfoPanelCards", InfoPanelBlock()),
            ("BoardMembersCards", BoardMembersCardBlock()),
        ],
        use_json_field=True,
        null=True,
        blank=True
    )
    content_panels = BasePage.content_panels + [
        FieldPanel("body")
    ]
