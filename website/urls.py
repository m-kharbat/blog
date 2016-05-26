""" URL Configuration """

from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', 
            admin.site.urls),
    url(r'^$', 
            views.home), 
    url(r'^blog/$', 
            views.index), 
    url(r'^blog/articles/(?P<slug>[^\.]+)', 
            views.view_post, 
            name='view_blog_post'),
    url(r'^blog/categories/(?P<slug>[^\.]+)',
            views.view_category, 
            name='view_category'),
]
