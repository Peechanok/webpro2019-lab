
from django.urls import path
from . import views

urlpatterns = [
     path('payment/<int:event_id>/',views.payment, name='event_tickets_Payment'),
     path('admin/add_event/',views.event_add, name='event_tickets_add_event'),
     path('event/details/<int:event_id>/',views.event_details, name='event_tickets_details'),
     path('category/details/<int:category_id>/',views.category_details, name='event_category_details'),
     path('admin/<int:user_id>/',views.sign_in_anonymous, name='sign_in_anonymous'),
     path('admin/payment_purchase/<int:event_id>/',views.payment_save, name='event_tickets_perchase'),
     path('event/event_delete/<int:event_id>/',views.event_delete, name='event_delete'),
     path('event/event_list/',views.list_event, name='eventlist'),
     path('event/search/',views.search_data, name='search_data'),
   
]


