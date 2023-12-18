from django import template
from django.forms.models import model_to_dict


register = template.Library()


@register.inclusion_tag(
            filename='patterns/molecules/address/address.html',
            name='address_lang_tag', takes_context=True)
def address_lang_tag(context, address):
    lang = context.request.LANGUAGE_CODE
    if lang is None or lang == 'en':
        lang = ""
    else:
        lang = "_"+lang
    address_dict = model_to_dict(address)

    return {'value':

            {
                "orgname": address_dict["orgname"+lang],
                "dept": address_dict["dept"+lang],
                "address": address_dict["address"+lang],
                "opening": address_dict["opening"+lang],
                "phone": address_dict["phone"],
                "locall": address_dict["locall"],
                "fax": address_dict["fax"],
                "homepage": address_dict["homepage"],
                "homepage2": address_dict["homepage2"],
                "contact_form": address_dict["contact_form"],
                "email": address_dict["email"],
            }}
