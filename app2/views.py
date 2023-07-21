from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def bike(request):
    return HttpResponse('<strong><center>meteor650</center></strong>')
def car(request):
    return HttpResponse('<marquee>fortuner makes u happy</marquee>')