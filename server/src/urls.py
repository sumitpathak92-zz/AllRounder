"""AIlifesaver URL Configuration

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
from django.conf.urls import include, url, patterns
from rest_framework import routers
from django.contrib import admin
from common import api
from common.serializers import UserSerializers
# from common.models import Users


urlpatterns = [
    url(r'^users/$', api.user_list),
    # url(r'^users/(?<>P[0-9]+)/$', api.user_detail)
]

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)
# # user_urls = patterns('',
# #                     url(r'^(?P<username>[0-9a-zA-Z_-]+)/users$', UsersList.as_view(queryset=Users.objects.all(), serializer_class=UserSerializers), name='users')
# #                     )
# urlpatterns = patterns('',
#                        url(r'^admin/', include(admin.site.urls)),
#                        # url(r'^users/', include(user_urls)),
#                        )
#
# urlpatterns += [
#                 url(r'^', include(router.urls)),
#                 url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#              ]


