from . import views
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^messenger/$', views.messenger),
    url(r'^issue_bot/$', views.issue_bot),
    url(r'^vr_game/$', views.vr_game),
    url(r'^vr_tracking/$', views.vr_tracking),
    url(r'^django_fs/$', views.django_fs),
    url(r'^send_message/*', views.send_message, name='send_message'),

] 