from django.http import HttpResponse,HttpResponseRedirect,HttpResponseServerError
from pod.models import Podcast, PodcastForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
import os
from django.core.files import File

def index(request):
    podcast_list=Podcast.objects.all().order_by('-pub_date')
    return render_to_response('pod/index.html', {'podcast_list': podcast_list})

def detail(request, pod_id):
    pod = get_object_or_404(Podcast, pk=pod_id)
    if request.method == 'POST': 
        #form = PodcastForm(request.POST, request.FILES) 
        form = PodcastForm(request.POST, instance=pod ) 
        
        
        if form.is_valid(): 
            
            if request.FILES: # if sent a file
                pod.podcast=request.FILES['podcast']
                uploaded_file = request.FILES['podcast']
            else:
                pod.podcast=form.cleaned_data['podcast']
            
            
            pod.title=form.cleaned_data['title']    
            pod.rss_url=form.cleaned_data['rss_url']    
            pod.save()
            #new_podcast = Podcast(podcast = request.FILES['podcast'])
            #new_podcast.save()            
            return HttpResponseRedirect('/pods') 
    else:
        form = PodcastForm(instance=pod)

    variables = RequestContext(request, {
        'form': form
    })
    
    return render_to_response('pod/detail.html', variables)    

def download_pod(request, pod_url):
    
    pod_mp3=""
    pod_url=pod_url.lower()
    pod = get_object_or_404(Podcast, rss_url=pod_url)
    
    file_name="media/%s" % pod.podcast
    if os.path.isfile(file_name):
        f= open(file_name,'r' )
        response = HttpResponse(f,mimetype='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s.mp3' % pod_url
        response['X-Sendfile'] = file_name    
    else:
        #podcast not found returning error
        response = HttpResponseServerError ()
    
    return response
    

def delele_podcast(request, pod_id):
    pod = get_object_or_404(Podcast, pk=pod_id)
    pod.delete()
    return HttpResponseRedirect('/pods/') 

def add_podcast(request):
    if request.method == 'POST': 
        form = PodcastForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save()
            #new_podcast = Podcast(podcast = request.FILES['podcast'])
            #new_podcast.save()            
            return HttpResponseRedirect('/pods/') 
    else:
        form = PodcastForm()

    variables = RequestContext(request, {
        'form': form
    })
    
    return render_to_response('pod/detail.html', variables)    
    #return render_to_response(request, 'pod/detail.html', {'form': form,})    
    
    