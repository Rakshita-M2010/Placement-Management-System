from django import template

register = template.Library()

@register.filter
def split(value, separator):
    """
    Split a string by a separator.
    Usage: {{ string_value|split:"," }}
    """
    if not value:
        return []
    return value.split(separator)
