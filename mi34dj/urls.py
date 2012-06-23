from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mi34dj.mainapp.views.index', name='index'),
    # url(r'^mi34/', include('mi34.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

from django.views.static import serve
from django.conf import settings
_media_url = settings.MEDIA_URL
if _media_url.startswith('/'):
    _media_url = _media_url[1:]
    urlpatterns += patterns('',
                            (r'^%s(?P<path>.*)$' % _media_url,
                             serve,
                             {'document_root': settings.MEDIA_ROOT}))
    del (_media_url, serve)
    