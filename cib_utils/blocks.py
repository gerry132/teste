from django.forms.utils import ErrorList
from django.utils.translation import gettext_lazy as _

from wagtail import blocks
from wagtail.blocks.struct_block import StructBlockValidationError
from wagtail.images.blocks import ImageChooserBlock

ALT_HELP_TEXT = """A short one-sentence literal description
                    of the %s is
                    required to make the page accessible to the
                    visually impaired. Details: https://axesslab.com/alt-texts/"""

ALT_BUTTON = ALT_HELP_TEXT % 'button'


class BaseBlockLinkContext(blocks.StructBlock):
    """
    Base block to get link context.
    """
    def get_context(self, value, parent_context=None):
        """
        Get context helper
        """
        context = super().get_context(value, parent_context=parent_context)
        try:
            # A block may not have a page or url field
            if value["url"]:
                context["link_url"] = value["url"]
            elif value["page"]:
                context["link_url"] = value["page"].url

        except KeyError:
            context["link_url"] = None

        try:
            if value["title"]:
                context["link_title"] = value["title"]
            else:
                if value["page"]:
                    context["link_title"] = value["page"].title
                elif value["url"]:
                    context["link_title"] = value["title"]

        except KeyError:
            context["link_title"] = None

        return context


class LinkBlockWithURL(BaseBlockLinkContext):
    """
    Link block with url
    """
    page = blocks.PageChooserBlock(required=False)
    title = blocks.CharBlock(
        help_text=_("Leave blank to use the page's own title"), required=False
    )
    url = blocks.URLBlock(
        label="URL",
        required=False,
        help_text="An external link.",
    )


class LinkButtonBlock(blocks.StructBlock):
    """
    Link button block class
    """
    button_text = blocks.CharBlock(max_length=50)
    page = blocks.PageChooserBlock(required=False)
    url = blocks.URLBlock(
        label="URL",
        required=False,
        help_text="An external link.",
    )
    link_button_alt = blocks.CharBlock(
        required=False,
        help_text=_(ALT_BUTTON),
    )

    class Meta:
        icon = "image"
        label = "Link Button"
        template = "patterns/molecules/link_button/link_button.html"

    def clean(self, value):
        errors = {}
        values = [value["page"], value["url"]]
        # Set only a Page OR a URL
        if sum(value is not None and value != "" for value in values) != 1:
            message = "Please choose only a page or set a URL."

            errors["page"] = ErrorList([message])
            errors["url"] = ErrorList([message])

        # A URL must have title
        if value["url"] and not value["heading"]:
            errors["heading"] = ErrorList(["Please set a title for the URL"])

        if errors:
            raise StructBlockValidationError(errors)

        return super().clean(value)

    def get_context(self, value, parent_context=None):
        """
        Get context helper.
        """
        context = super().get_context(value, parent_context=parent_context)
        try:
            # A block may not have a page or url field
            if value["url"]:
                context["link_url"] = value["url"]
            elif value["page"]:
                context["link_url"] = value["page"].url

        except KeyError:
            context["link_url"] = None
        return context


class RichTextBlock(blocks.RichTextBlock):
    """
    Wrapper class for richtext.
    """
    class Meta:
        label = "Rich-Text"
        template = "patterns/molecules/streamfield/blocks/paragraph_block.html"


class BaseFeatureBlock(blocks.StructBlock):
    """
    Base feature block.
    """
    icon = ImageChooserBlock(required=False)
    heading = blocks.CharBlock(
        required=False,
        help_text="Text to display as feature heading",
        max_length=250
    )

    main_feature = blocks.StreamBlock(
        [
            ("rich_text", RichTextBlock()),
            ("links_list", blocks.ListBlock(
                LinkBlockWithURL(max=5),
            )
            ),
        ]
    )
    button = blocks.StreamBlock(
        [("button", LinkButtonBlock(max=1))],
        max_num=1,
        required=False
    )

    colour_palette = blocks.ChoiceBlock(
        choices=(          
            ("base-feature--green", "Green and Black"),
            ("base-feature--blue", "Blue & White"),)
    )

    class Meta:
        label = "Standard Feature Block"
        template = "patterns/molecules/streamfield/blocks/base_feature_block.html"
