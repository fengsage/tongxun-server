from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from shequ import api

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('',
    url(r'^api/shequ/$', api.shequ , name='shequ'),
    url(r'^api/zhibu/(?P<shequ_id>\d+)/$', api.zhibu , name='zhibu'),
    url(r'^api/mobile/(?P<zhibu_id>\d+)/$', api.mobile , name='mobile'),
)
