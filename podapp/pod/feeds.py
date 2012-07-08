from django.contrib.syndication.views import Feed
from pod.models import Podcast
from django.shortcuts import get_object_or_404

class PodcastsFeed(Feed):
    title = "Podcasts"
    link = "/rss/"
    description = "Latest podcasts"

    def items(self):
        itms=Podcast.objects.order_by('-pub_date')
        return itms
    
    def item_title(self, item):
        return item.title

    def item_link(self, item):
        #return item.rss_url
        return "http://127.0.0.1:8000/podsdownload/%s" % item.rss_url
    
    
    def item_description(self, item):
        return item.title

