from django.conf.urls import patterns, include, url
from pod.feeds import PodcastsFeed

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pod.views.index'),
    url(r'^(?P<pod_id>\d+)/$', 'pod.views.detail'),                       
    url(r'^delete/(?P<pod_id>\d+)/$', 'pod.views.delele_podcast'),                       
    url(r'^add/$', 'pod.views.add_podcast'),                       
    url(r'^podsdownload/(?P<pod_url>[A-Za-z0-9_-]+)/$', 'pod.views.download_pod'),                       
    url(r'^latest/feed/$', PodcastsFeed()),


    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
