from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def check_list(request,username):
    return HttpResponse( 'welcome to %s Today is Thursday.\n You have subjects that are taught are ENGLISH , MATH , WEB PROGRAMING ' % username)
def Details(request,stu_not):
    return HttpResponse( 'This course teaches englist there are 100 students, there are come 20 students and %s lack.' % stu_not)
def Qr_code(request,subject):
    return HttpResponse( 'Name Subject : %s   Page name check system with qr code ' % subject)