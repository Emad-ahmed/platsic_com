from django import template

register = template.Library()

@register.filter(name='add')
def add(value, arg):
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        return ""

@register.filter(name='mul')
def mul(value, arg):
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return ""
    

