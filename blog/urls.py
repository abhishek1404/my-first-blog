from django.conf.urls import patterns,url
from . import views
urlpatterns = patterns('',
    url(r'^$', views.post_list, name='post_list'),
    url(r'^search/$', views.search_form,name='search_form'),
    url(r'^video_title/$', views.video_page,name='video_page'),
    url(r'^text_title/$', views.text_page,name='text_page'),


)