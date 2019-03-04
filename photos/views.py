from django.shortcuts import render,redirect
from .models import Photo, Topic, Location
from django.http import HttpResponse, Http404

def index(request):
    photos = Photo.objects.all()
    location = Location.objects.all()
    return render(request,'index.html', {'photos':photos, 'location':location})

def search_results(request):

    if 'topic' in request.GET and request.GET["topic"]:
        search_term = request.GET.get("topic")
        searched_photos = Photo.search_by_topic(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def show_location(request):
    location = location.objects.all()
    location = location.objects.get(id = location_id)
    photo = photo.objects.filter(location = location.id)

    return render(request,'location.html',{'location':location,'photo':photo})
