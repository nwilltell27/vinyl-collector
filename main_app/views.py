from django.shortcuts import render

class Record:
    def __init__(self, artist, album_name, genre, release_year):
        self.artist = artist
        self.album_name = album_name
        self.genre = genre
        self.release_year = release_year

vinyl = [
    Record('Lettuce', 'Resonate', 'Funk', 2020),
    Record('Vulfpeck', 'Live at Madison Square Garden', 'Funk', 2019),
    Record('Pigeons Playing Ping Pong', 'Pizazz', 'Funk', 2017),
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def vinyl_index(request):
    return render(request, 'vinyl/index.html', { 'vinyl': vinyl })