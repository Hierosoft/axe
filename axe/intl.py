"""Provide Internationalization support.

Normally we would do:
import gettext
_ = gettext.gettext

But for now, since there is no language selection implemented in axe,
do:
from axe.intl import _
"""
translated_en = {
    "Geef naam (tag) voor het root element op": (
        "Enter a name (tag) for the root element"
    ),
    "parsing ging fout": "parsing went wrong",
    "geen well-formed xml": "not well-formed xml",
    "zetzeronder voor node {node} met data {data}": (
        "typewriter at the bottom for node {node} with data {data}"
    ),
    "Niks (meer) gevonden": "No more matches",  # "Nothing (anymore) found"
    "Helaas...": "Unfortunately...",
    "root element kan niet aangepast worden": "root element cannot be edited",
}


def _(value):
    prefix = "[intl._] "
    if value is None:
        return None
    if not value:
        # blank
        return value
    # TODO: choose a language (for now, show both)
    value_en = translated_en.get(value)
    if value_en is None:
        print(prefix + 'Warning: There is no translation for "{}"'
              ''.format(value))
        return value
    return "{} ({})".format(value, value_en)
