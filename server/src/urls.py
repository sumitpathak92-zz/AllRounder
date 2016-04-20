"""AllRounder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from common import api
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

from apps.users import api_views
# from apps.users.api_views import AllrounderUserDetailAPI

urlpatterns = [
    url(r'^users/$', api.UserList.as_view()),
    url(r'^users/(?P<id>[0-9]+)$', api.UserDetails.as_view()),
    url(r'^allusers/$', api_views.AllrounderUserAPI.as_view()),
    url(r'^allusers/(?P<id>[0-9]+)$', api_views.AllrounderUserDetailAPI.as_view()),
    # url(r'^users/(?<>P[0-9]+)/$', api.user_detail)
]
urlpatterns += [
    url(r'^', api.IndexView.as_view(template_name='index.html'), name='index'),
]

urlpatterns += [
    url(r'^admin/', admin.site.urls),
]


urlpatterns = format_suffix_patterns(urlpatterns)


