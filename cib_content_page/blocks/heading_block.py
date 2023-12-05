import unidecode
from django.forms.utils import ErrorList
from django.utils.text import slugify
from wagtail.blocks.struct_block import StructBlockValidationError
from wagtail.blocks import ChoiceBlock, CharBlock, StructBlock
from django.utils.translation import gettext_lazy as _
import hashlib


class HeadingSizeChoiceBlock(ChoiceBlock):
    choices = [
        ('h2', 'H2'),
    ]


class HeadingBlock(StructBlock):
    title = CharBlock(required=True)
    anchor_id = CharBlock(
        required=False,
        label=_("Anchor ID (Optional)"),
        help_text=_("Anchor target must be a compatible slug format without spaces or special characters")
    )

    def generate_hash_title(self, title):
        """
        returns a 6 length hexa hash value for each title, hash value
        will be different for different title. this value will be pre-populated
        to anchor_id field while page rendering.
        """
        title = title
        title_bytes = title.encode()
        sha1 = hashlib.sha1()  # nosec
        sha1.update(title_bytes)
        hexacode = sha1.hexdigest()
        return hexacode[:6]

    class Meta:
        template = 'patterns/blocks/heading.html'
        label = _("Heading")
        icon = 'title'

    def clean(self, value):
        errors = {}
        anchor_id = self.generate_hash_title(value.get("title"))
        value["anchor_id"] = anchor_id
        slug = slugify(unidecode.unidecode(anchor_id))

        if anchor_id != slug:
            errors['anchor_id'] = ErrorList([_(f"\
                '{anchor_id}' is not a valid slug for the anchor target. \
                '{slug}' is the suggested value for this.")])
            raise StructBlockValidationError(block_errors=errors)
        return super().clean(value)
