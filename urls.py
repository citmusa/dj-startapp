# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^1/$', views.view_sample),
    url(r'^2/$', views.ClassySample.as_view()),
]
