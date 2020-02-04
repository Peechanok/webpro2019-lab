from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Dashbord(request):
    return HttpResponse( 'The dashboard screen can see an overview of the system on how many subjects were enrolled on that day, how many people were absent and how many were displayed here.')
def Export(request):
    return HttpResponse( 'Screen to search and export classroom attendance information Both in the current and past semester')