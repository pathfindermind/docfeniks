# -*- coding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.views.generic.base import TemplateView
from feedback_app.views import ContactCreateView


urlpatterns = patterns('',
    url(r'^$', ContactCreateView.as_view(), name='contacts'),
)
