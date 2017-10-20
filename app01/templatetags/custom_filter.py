#!/user/bin/env python
# -*-coding:utf-8-*-
from django import template

register = template.Library()

@register.filter
def my_split(id,strr):
    new_str = strr.split(',')
    if str(id) in new_str:
        return '0px -20px'
    else:
        return '0px -40px'
