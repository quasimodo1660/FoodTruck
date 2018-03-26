from django import template

register = template.Library()
@register.filter
def count_true(value):
    return value.filter(display=True).count()