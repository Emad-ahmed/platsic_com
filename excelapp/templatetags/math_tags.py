from django import template

register = template.Library()

@register.filter(name='add')
def add(value, arg):
    try:
        number = float(value) + float(arg)
        formated_number = format(number, ".2f")
        return formated_number
    except (ValueError, TypeError):
        return ""

@register.filter(name='mul')
def mul(value, arg):
    try:
        number = float(value) * float(arg)
        formated_number = format(number, ".2f")
        return formated_number
    except (ValueError, TypeError):
        return ""
    
@register.filter(name='multiply_and_add_vat')
def multiply_and_add_vat(value1, value2):
    product = value1 * value2
    vat_percentage = 20
    vat_amount = (product * vat_percentage) / 100
    total_with_vat = product + vat_amount
    return total_with_vat

@register.filter(name='vat_amount_show')
def vat_amount_show(value1, value2):
    product = value1 * value2
    vat_percentage = 20
    vat_amount = (product * vat_percentage) / 100
    
    return vat_amount

