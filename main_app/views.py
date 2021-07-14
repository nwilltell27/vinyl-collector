from django.shortcuts import render
from .models import Vinyl

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def vinyl_index(request):
    vinyls = Vinyl.objects.all()
    return render(request, 'vinyl/index.html', { 'vinyls': vinyls })

def vinyls_detail(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    return render(request, 'vinyl/detail.html', { 'vinyl': vinyl })