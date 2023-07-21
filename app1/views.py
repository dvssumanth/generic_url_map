from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def dvs(request):
    return HttpResponse('<marquee>you need to get a job</marquee>')
def sumanth(request):
    return HttpResponse('<center>python developer</center>')