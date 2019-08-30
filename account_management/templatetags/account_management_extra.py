from django.template import library
from django.template.defaultfilters import stringfilter
from django.template import Library
from datetime import datetime


register = Library()
@register.filter(is_safe=True)
@stringfilter
def get_ext(value):
    value = value.replace(value[3:7],"***")
    return value



@register.filter(is_safe=True)
def date_format(val):
    return f"{val.year}-{val.month}-{val.day} {val.hour}:{val.minute}:{val.second}"