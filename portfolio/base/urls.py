from . import views
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home),
    url(r'^site/$', views.home_site),
    url(r'^about/$', views.home_about),

    url(r'^messenger/$', views.messenger),
    url(r'^send_message/*', views.send_message),
    url(r'^messenger/client_code/$', views.messenger_client),
    url(r'^messenger/server_code/$', views.messenger_server),

    url(r'^issue_bot/$', views.issue_bot),
    url(r'^issue_bot/bot_code/$', views.issue_bot_bot),
    url(r'^issue_bot/analyzer_code/$', views.issue_bot_analyzer),
    url(r'^issue_bot/research_paper/$', views.issue_bot_paper),
   
    url(r'^vr_game/$', views.vr_game),
    
    url(r'^vr_tracking/$', views.vr_tracking),

    url(r'^django_fs/$', views.django_fs),
    url(r'^django_fs/code/$', views.django_fs_code),

] 