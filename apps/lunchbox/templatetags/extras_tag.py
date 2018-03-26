from django import template

register = template.Library()
@register.filter
def count_true(value):
    return value.filter(display=True).count()

@register.simple_tag
def blank_star(value):
    return range(5 - value)