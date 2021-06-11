from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def chat(request):
    return HttpResponse('<h1> Sorry for Inconvenience! <br> The site is Coming Soon! </h1>')


def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
