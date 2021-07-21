from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vinyl
from .forms import TouringForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def vinyl_index(request):
    vinyls = Vinyl.objects.all().order_by('artist')
    return render(request, 'vinyl/index.html', { 'vinyls': vinyls })

def vinyls_detail(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    touring_form = TouringForm()
    return render(request, 'vinyl/detail.html', { 
        'vinyl': vinyl, 'touring_form': touring_form
    })

class VinylCreate(CreateView):
    model = Vinyl
    fields = ['artist', 'album_name', 'genre', 'release_year'] # can also use '__all__'
    success_url = '/vinyls/'

class VinylUpdate(UpdateView):
    model = Vinyl
    fields = ['artist', 'album_name', 'genre', 'release_year']

class VinylDelete(DeleteView):
    model = Vinyl
    success_url = '/vinyls/'
