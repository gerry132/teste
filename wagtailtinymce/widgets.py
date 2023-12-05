from tinymce.widgets import TinyMCE
from wagtail.core.telepath import register
from wagtail.core.widget_adapters import WidgetAdapter
from wagtail.utils.widgets import WidgetWithScript


class WagtailTinyMCE(WidgetWithScript, TinyMCE):
    def __init__(
        self,
        content_language=None,
        attrs=None,
        menubar_options=None,
        toolbar_options=None,
        mce_config=None,
    ):
        mce_config = mce_config or {}
        if menubar_options is not None:
            mce_config["menubar"] = menubar_options
        if toolbar_options is not None:
            mce_config["toolbar"] = toolbar_options
        super().__init__(content_language, attrs, mce_config)


class WagtailTinyMCEAdapter(WidgetAdapter):
    js_constructor = "wagtailtinymce.widgets.WagtailTinyMCE"

    class Media:
        js = [
            # This is the JS file that will run every time an
            # TinyMCEBlock is added.
            "wagtailtinymce/js/tinymce-adapter.js",
        ]


register(WagtailTinyMCEAdapter(), WagtailTinyMCE)
