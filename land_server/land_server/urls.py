from django.conf.urls import patterns, include, url

from views import MapView
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', MapView.as_view(), name='map_display'),
    #url(r'^', views.error, name='error'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
