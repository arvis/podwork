from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^pods/$', 'pod.views.index'),
    url(r'^pods/(?P<pod_id>\d+)/$', 'pod.views.detail'),                       
    url(r'^pods/add/$', 'pod.views.add_podcast'),                       

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
