from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

#from .models import WockaJokes, StupidStuffJokes, UploadJokes
from django.template import loader

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
#from .models import WockaJokes,Comments,ShortedList
from user.models import User
#from user.views import categoriesView
#from .forms import Up

def chamber(requests):
    return render(requests, 'cos/chamber.html')
    #return HttpResponse('<center><B><strong>I want her</center>')

def secrets(requests):
    return render(requests, 'cos/secrets.html')
