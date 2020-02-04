from xml.etree.ElementTree import SubElement

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Stu_all(request,NumberAll):
    return HttpResponse( 'All student list screen %s people' % NumberAll)
def Add(request,Adds):
    return HttpResponse( 'Add student  = + %s' % Adds)
def Modify(request,Adds):
     return HttpResponse( 'The student information editing screen')
def Sub_details(request,Adds):
    return HttpResponse( 'Screen showing all subjects')
def Sub_Add(request,Adds):
    return HttpResponse( 'Add subject screen')
def Sub_Modify(request,Adds):
    return HttpResponse( 'The screen for editing course information')


