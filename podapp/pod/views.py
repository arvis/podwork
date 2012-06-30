from django.http import HttpResponse,HttpResponseRedirect
from pod.models import Podcast, PodcastForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
    podcast_list=Podcast.objects.all().order_by('-pub_date')
    return render_to_response('pod/index.html', {'podcast_list': podcast_list})

def detail(request, pod_id):
    pod = get_object_or_404(Podcast, pk=pod_id)
    if request.method == 'POST': 
        form = PodcastForm(request.POST, request.FILES) 
        if form.is_valid(): 
            if request.FILES:
                pod.podcast=form.cleaned_data['podcast']
                
            pod.title=form.cleaned_data['title']    
            pod.rss_url=form.cleaned_data['rss_url']    
            pod.save()
            #new_podcast = Podcast(podcast = request.FILES['podcast'])
            #new_podcast.save()            
            return HttpResponseRedirect('/') 
    else:
        form = PodcastForm(instance=pod)

    variables = RequestContext(request, {
        'form': form
    })
    
    return render_to_response('pod/detail.html', variables)    

def delele_podcast(request, pod_id):
    pod = get_object_or_404(Podcast, pk=pod_id)
    return HttpResponseRedirect('/') 

def add_podcast(request):
    if request.method == 'POST': 
        form = PodcastForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save()
            #new_podcast = Podcast(podcast = request.FILES['podcast'])
            #new_podcast.save()            
            return HttpResponseRedirect('/') 
    else:
        form = PodcastForm()

    variables = RequestContext(request, {
        'form': form
    })
    
    return render_to_response('pod/detail.html', variables)    
    #return render_to_response(request, 'pod/detail.html', {'form': form,})    
    
    