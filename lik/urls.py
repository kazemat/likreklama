#!/virtualenv/lik/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/', views.about, name='about-company'),
    url(r'contacts/', views.contacts, name='company-contacts'),
    url(r'(?P<cat_id>[0-9]+)/$', views.product_from_category, name='product-cat'),
    url(r'(?P<cat_id>[0-9]+)/(?P<product_id>[0-9]+)/$', views.product_from_category, name='product-prod'),
]