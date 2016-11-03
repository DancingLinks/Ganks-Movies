"""GankMovie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^index$', views.index, name='index'),
    url(r'^test$', views.test, name='test'),
    url(r'^day/(?P<id>[0-9]+)$', views.day_ganks, name='day_ganks'),
    url(r'^AndroidGanks/(?P<id>[0-9]+)$', views.android_ganks, name='android_ganks'),
    url(r'^iOSGanks/(?P<id>[0-9]+)$', views.ios_ganks, name='ios_ganks'),
    url(r'^FrontGanks/(?P<id>[0-9]+)$', views.front_ganks, name='front_ganks'),
    url(r'^AppGanks/(?P<id>[0-9]+)$', views.app_ganks, name='app_ganks'),
    url(r'^ReGanks/(?P<id>[0-9]+)$', views.xiatuijian_ganks, name='xiatuijian_ganks'),
    url(r'^MovieGanks$', views.movie_ganks, name='movie_ganks'),
    url(r'^SearchMovie$', views.search_movie, name='search_movie'),
    url(r'^download$', views.download, name='download')
]
