
from django.urls import path
from . import views

urlpatterns = [
 path('list_sub/<str:username>',views.check_list, name = 'list_sub'),
    path('course/<int:stu_not>',views.Details, name = 'Details'),
    path('chackname/<str:subject>',views.Qr_code, name = 'Qr_code'),
]