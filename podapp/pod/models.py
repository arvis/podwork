from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse

# Create your models here.
class Podcast(models.Model):
    title = models.CharField(max_length=50)
    podcast = models.FileField(upload_to='podcasts')
    rss_url=models.URLField()
    pub_date = models.DateTimeField(auto_now=True, blank=True)

    def get_absolute_url(self):
        return reverse('podcast-detail', kwargs={'pk': self.pk})


class PodcastForm(ModelForm):

    class Meta:
        model = Podcast