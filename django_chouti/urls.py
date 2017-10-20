"""django_chouti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^info1/', views.info1),
    url(r'^info2/', views.info2),
    url(r'^denglu2/', views.denglu2),
    url(r'^denglu1/', views.denglu1),
    url(r'^sicang/', views.sicang),
    url(r'^shezhi/', views.shezhi),
    # url(r'^delete/', views.delete),
    # url(r'^addmassage/', views.addmassage),
    # url(r'^addcontent/', views.addcontent),
    # url(r'^delete/', views.deletemassage),
    url(r'^fabu/', views.fabu),
    url(r'^ceshi/', views.ceshi),
    url(r'^add_sicang/', views.add_sicang),
    url(r'^get_content/', views.get_content),
    url(r'^page/(?P<page>\d+)/', views.page),

]
