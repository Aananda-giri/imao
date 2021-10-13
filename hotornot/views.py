from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    formatt=['tif','tiff','gif','eps','raw']
    rollno = [f'{i:03}' for i in range(1,50)]
    serial=[i for i in range(3000,3100)]
    return render(request, 'hotornot/polls.html',{'rollno':rollno,'format':formatt,'serial':serial})
