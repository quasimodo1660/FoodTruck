from django import template

register = template.Library()
@register.filter
def count_true(value):
    return value.filter(display=True).count()

@register.simple_tag
def blank_star(value):
    return range(5 - value)
    
@register.simple_tag
def full_star(value):
    return range(value)

@register.simple_tag
def avg_rate(value):
    total=0
    for i in value:
        total+=i.score
    if value.count()==0:
        return 0
    else:
        return round(total/value.count(),2)