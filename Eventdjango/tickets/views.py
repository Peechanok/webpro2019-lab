import email
import profile
from builtins import object
from datetime import date, datetime
from threading import Event
from tokenize import group
from urllib import request
from webbrowser import get

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.db import IntegrityError
from django.forms import models
from django.http import HttpResponse
from django.shortcuts import redirect, render

from Manage_events.models import Category, Event


# Create your views here.
@property
def is_past_due(self):
    return date.today()>= self.Event.event_date

def poppular_check(self):
    eventgived = str(Event.is_popular)
    eventcompare = eventgived == "Y"
    print(eventgived)
    return self

def home(request):
    
    query_results = Event.objects.all()
    query_results_category = Category.objects.all()
        
    return render(request, 'tickets/home.html',context={
        'query_results': query_results,
        'query_results_category':query_results_category})


def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('tickets_home')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = "Sorry! Username and Password didn't match, Please try again !!"

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name='login.html', context=context)

@login_required

def my_logout(request):
    logout(request)
    return redirect('tickets_login')

def sign_in(request):
    """
        เพิ่มข้อมูล user / student ใหม่เข้าสู่ฐานข้อมูล
    """
    msge = ''
    context = {}
  
    if request.method == 'POST':
        
           
        user = User.objects.create_user(
            request.POST.get('username'),
            request.POST.get('email'),
            request.POST.get('password'),
            
           
        )
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        group = Group.objects.get(name='registered')
        user.groups.add(group)
            

        user.save()
        redirect('tickets_login')   
        msge = 'Successfully create new Account - username: %s' % (user.username)
         
    else:
        user = User.objects.none()
        
    context = {
        
        'msge': msge
    }

    return render(request, 'sign_in.html', context=context)

@login_required
def change_password(request):
    context = {}
    if request.method == 'POST':
        user = request.user
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # check that the passwords match
        if password1 == password2:
            user.set_password(password2)
            user.save()
            redirect('login')
        else:
           context['password1'] = password1
           context['password2'] = password2
           context['error'] = "Sorry! Password didn't match, Please try again !!"



        # reset password 

    return render(request, template_name='change_password.html', context=context)

@login_required
def update_profile(request,user_id):
    """
        Update ข้อมูลชั้นเรียนที่มี id = class_id
    """
    
    try:
        user = User.objects.get(pk=user_id)
        msg = ''
    except User.DoesNotExist:
        return redirect('tickets_home')

    if request.method == 'POST':
        user.username=request.POST.get('username')
        user.email=request.POST.get('email')
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        
        
        user.save()
        msg = 'Successfully ffupdate student - username: %s' % (user.username)
        
    context = {
        
        'msg': msg
    }

    return render(request, template_name='tickets/home.html', context=context)
    
@login_required
def profile(request):
        

    return render(request, 'update_profile.html')
