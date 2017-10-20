#!/user/bin/env python
# -*-coding:utf-8-*-
from django import forms
from app01 import models
class UsePhone(forms.Form):
    choise = [(86,'中国(+86)'),(852,'中国香港(+852)'),(853,'中国香港(+853)'),(886,'中国台湾(+886)'),]
    address1 = forms.ChoiceField(choices = choise )
    phone1 = forms.IntegerField()
    phone1.widget.attrs['placeholder'] = '手机号'
    pwd1 = forms.CharField(max_length=64)
    pwd1.widget.attrs['placeholder'] = '密码'

class UseName(forms.Form):
    name2 = forms.CharField(max_length=64)
    name2.widget.attrs['placeholder'] = '用户名'
    pwd2 = forms.CharField(max_length=64)
    pwd2.widget.attrs['placeholder'] = '密码'

class InfoFirst(forms.Form):
    choise = [(86,'中国(+86)'),(852,'中国香港(+852)'),(853,'中国香港(+853)'),(886,'中国台湾(+886)'),]
    address3 = forms.ChoiceField(choices = choise )
    phone3 = forms.IntegerField()
    phone3.widget.attrs['placeholder'] = '手机号'
    yanzheng3 = forms.IntegerField(required=None)
    yanzheng3.widget.attrs['placeholder'] = '验证码(可跳过)'
    pwd3 = forms.CharField(max_length=64)
    pwd3.widget.attrs['placeholder'] = '密码'


class InfoSedond(forms.Form):
    name4 = forms.CharField(max_length=64)
    name4.widget.attrs['placeholder'] = '用户名'
    countrys = [(0,'中国'),(1,'外国'),]
    country4 = forms.ChoiceField(choices=countrys)
    provinces = models.Province.objects.values_list('id','province')
    province4 = forms.ChoiceField(choices=provinces)
    citys = models.City.objects.values_list('id','city')
    city4 = forms.ChoiceField(choices=citys)
    content4 = forms.CharField(max_length=256,required=None)
    content4.widget.attrs['placeholder'] = '签名(可不填)'