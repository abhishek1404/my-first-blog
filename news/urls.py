from django.conf.urls import patterns,url
from . import views
urlpatterns = patterns('',
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^article/$', views.post_article, name='post_article'),




)