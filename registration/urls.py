from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'registration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^reglog/', include('reglog.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
        
if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
