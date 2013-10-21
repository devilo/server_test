from django.conf.urls import patterns, include, url
from api import ArticleResource
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

article_resource = ArticleResource()

urlpatterns = patterns('',
    url(r'^all/$','article.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$','article.views.article'),
    url(r'^api/',include(article_resource.urls)),
    # Examples:
    # url(r'^$', 'server_test.views.home', name='home'),
    # url(r'^server_test/', include('server_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
