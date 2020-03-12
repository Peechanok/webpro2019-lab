
import email
import profile
from asyncio import events
from builtins import object
from fnmatch import filter
from itertools import chain
from lib2to3.fixes.fix_input import context
from urllib import request
from venv import create
from webbrowser import get

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from django.forms import models
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render

from Manage_events.models import Category, Event, Ticket

# Create your views here.

def sign_in_anonymous(request):
    """
        เพิ่มข้อมูล user / anonymous ใหม่เข้าสู่ฐานข้อมูล
    """
    msge = 'Successful payment,The system has successfully applied for membership'
    context = {}
  
    if request.method == 'POST':
        
           
        user = User.objects.create_user(
            request.POST.get('username'),
            request.POST.get('email'),
            request.POST.get('password'),
            
           
        )
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        

            

        user.save()
        msge = 'Successfully create new Account - username: %s' % (user.username)
            
    else:
        user = User.objects.none()
        
    context = {
        
        'msge': msge
    }

    return redirect(to='eventlist',context=context)



def payment_save(request ,event_id):
    event = Event.objects.get(pk=event_id,)
    
   

    if request.method == 'POST':
       
        event.ticket_amount=request.POST.get('ticket_amount')
        event.save()
        
        return render(request, 'Manage_events/payment.html') 
        
        
def payment_save_ticket(request):
    if request.method == 'POST':
        ticket = Ticket.objects.create(
        purchased_date=request.POST.get('purchased_date'),
        event_id=request.POST.get('event_id'),
        user_id=request.POST.get('user_id')
        )
        
        ticket.save()
        
    
    
    
    



def payment(request ,event_id):
        
    event = Event.objects.get(pk=event_id,)
    if request.method == 'POST':
       event.usticket_amount=request.POST.get('usticket_amount')
    x = event.usticket_amount
    y = ''.join(map(str, x ))
    user_tamount =int(y)
    print (user_tamount)
    price_amount = event.ticket_price * user_tamount
    event_payment = event.ticket_amount - user_tamount
    category=Category.objects.all()
    return render(request, 'Manage_events/payment.html',context={
        'event': event,
        'event_payment':event_payment,
        'price_amount':price_amount,
        'user_tamount':user_tamount,
        'category':category
        }
        )



def __str__(self):
        return self.name + ": " + str(self.imagefile)
@login_required
@permission_required('Manage_event.add_event')
def event_add(request):
    """
        เพิ่มข้อมูล Event ใหม่เข้าสู่ฐานข้อมูล
    """
    msg = ''
    categorys = Category.objects.all()
    if request.method == 'POST':
        event = Event.objects.create(
            
            event_name=request.POST.get('event_name'),
            description=request.POST.get('description'),
            event_date=request.POST.get('event_date'),
            event_time=request.POST.get('event_time'),
            location=request.POST.get('location'),
            ticket_price=request.POST.get('ticket_price'),
            ticket_amount=request.POST.get('ticket_amount'),
            picture=request.POST.get('picture'),
            is_popular=request.POST.get('is_popular'),
            category_id=request.POST.get('category_id'),
        )
        
        msg = 'Successfully create new event'
    else:
        event = Event.objects.none()

    context = {
       'is_populars': Event.POPPULAR,
       'categorys':categorys,
        'msg': msg
    }

    return render(request, 'Manage_events/add_event_admin.html', context=context)

@login_required
def list_event(request):
    
    query_results = Event.objects.all()
        
    return render(request, 'Manage_events/event_list_add.html',context={'query_results': query_results,})


def event_details(request, event_id):
    event = Event.objects.get(pk=event_id)
    category = Category.objects.all()
    return render(request, 'Manage_events/event_details.html',context={
        'event': event,
        'category':category})
       
def category_details(request, category_id):
    category = Category.objects.get(pk=category_id)
    event = Event.objects.all()
    
    return render(request, 'Manage_events/category_details.html',context={
        'category': category,'event': event})
@login_required
def event_delete(request, event_id):
    """
        ลบข้อมูล student โดยลบข้อมูลที่มี id = user_id
    """
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect(to='eventlist')

def search_data(request):
    """
        แสดงข้อมูล classroom ทั้งหมดในระบบ
    """
    search = request.GET.get('search', '')
    events = Event.objects.filter(Q(event_name__contains=search) | Q(location__contains=search))
  

    return render(request, 'class/tickets_home.html', context={
        'events': events,
        'search': search,
        
    })
