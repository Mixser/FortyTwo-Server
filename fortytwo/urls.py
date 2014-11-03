from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static
from fortytwo import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_name.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('base.urls'))
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
