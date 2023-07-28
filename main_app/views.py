from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import VideoGame, Platform
from .forms import StreamForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def videogames_index(request):
    videogames = VideoGame.objects.all() # Retrieve all videogames
    return render(request, 'videogames/index.html', 
    { 
        'videogames': videogames 
    }
)

def videogames_detail(request, videogame_id):
  videogame = VideoGame.objects.get(id=videogame_id)
  id_list = videogame.platforms.all().values_list('id')
  platforms_videogame_doesnt_have = Platform.objects.exclude(id__in=id_list)
  stream_form = StreamForm()
  return render(request, 'videogames/detail.html', { 
    'videogame': videogame,
    'stream_form': stream_form,
    'platforms': platforms_videogame_doesnt_have
  })

def add_stream(request, videogame_id):
  # create a ModelForm instance using the data in request.POST
  form = StreamForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the videogame_id assigned
    new_stream = form.save(commit=False)
    new_stream.videogame_id = videogame_id
    new_stream.save()
  return redirect('detail', videogame_id=videogame_id)

class VideoGameCreate(CreateView):
   model = VideoGame
   fields = ['title', 'genre', 'description', 'release_year']

class VideoGameUpdate(UpdateView):
   model = VideoGame
   fields = ['genre', 'description', 'release_year']

class VideoGameDelete(DeleteView):
   model = VideoGame
   success_url = '/videogames'

class PlatformList(ListView):
  model = Platform

class PlatformDetail(DetailView):
  model = Platform

class PlatformCreate(CreateView):
  model = Platform
  fields = '__all__'

class PlatformUpdate(UpdateView):
  model = Platform
  fields = ['name', 'color']

class PlatformDelete(DeleteView):
  model = Platform
  success_url = '/platforms'

def assoc_platform(request, videogame_id, platform_id):
  VideoGame.objects.get(id=videogame_id).platforms.add(platform_id)
  return redirect('detail', videogame_id=videogame_id)

def unassoc_platform(request, videogame_id, platform_id):
  VideoGame.objects.get(id=videogame_id).platforms.remove(platform_id)
  return redirect('detail', videogame_id=videogame_id)