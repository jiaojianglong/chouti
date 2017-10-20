from django.db import models
import datetime
# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,db_index=True)
    phone = models.BigIntegerField()
    pwd = models.CharField(max_length=64)
    sex = models.IntegerField(choices=[(0,'男'),(1,'女'),],default=1)
    address_country = models.IntegerField(choices=[(0,'中国'),(1,'外国'),],default= 0 )
    address_city = models.ForeignKey('City')
    content = models.CharField(max_length=128,null=True)
    photo = models.ImageField(upload_to='/static/images/',null=True,default='/static/images/2016-10-03 152643(1).jpg')
    score = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    sicang = models.ManyToManyField('Massage')
    guanzhu = models.ManyToManyField('User')

class Massage(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    href = models.TextField()
    picture = models.CharField(max_length=128)
    auther = models.ForeignKey('User')
    time = models.DateTimeField(auto_now_add=True)
    dianzan = models.IntegerField(default=0)
    dianzan_user = models.TextField()

class Province(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=128)

class City(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=128)
    province = models.ForeignKey('Province')


class Phone(models.Model):
    phone = models.BigIntegerField(unique=True)
    pwd = models.CharField(max_length=64)
class content(models.Model):
    img = models.CharField(max_length=256)
    content = models.TextField()
    url = models.CharField(max_length=256)
    source = models.CharField(max_length=256)

