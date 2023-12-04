from django.utils.translation import gettext_lazy as _
from wagtail.blocks import StructBlock
from wagtail.snippets.blocks import SnippetChooserBlock


class AddressBlock(StructBlock):
    address = SnippetChooserBlock("cib_core.Address")

    class Meta:
        template = 'patterns/blocks/address.html'
        label = _("Address")
        icon = 'home'
