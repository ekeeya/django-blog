from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='trim')
@stringfilter
def trim(value, arg):
    return value[:arg]
    