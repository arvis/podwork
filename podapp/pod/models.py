from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.core.validators import *

# Create your models here.
class Podcast(models.Model):
    title = models.CharField(blank=False,max_length=50)
    podcast = models.FileField(upload_to='podcasts')
    rss_url=models.CharField(max_length=255,unique=True,validators=[validate_slug] )
    pub_date = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return str(rss_url)
        #return ('pod.views.detail', [str(self.id)])    

class PodcastForm(ModelForm):

    class Meta:
        model = Podcast