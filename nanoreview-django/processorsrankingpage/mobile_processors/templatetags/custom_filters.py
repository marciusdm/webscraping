from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter(is_safe=True)
def comma_to_br(value):
    return mark_safe(value.replace(",","<br>"))