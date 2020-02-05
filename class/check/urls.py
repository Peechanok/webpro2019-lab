
from django.urls import path
from . import views

urlpatterns = [
 path('list_sub/<str:username>',views.check_list, name = 'list_sub_page'),
    path('course/<int:stu_not>',views.Details, name = 'Details_page'),
    path('chackname/<str:subject>',views.Qr_code, name = 'Qr_code_page'),
     path('error404/',views.show_error_404, name = 'show_error_404_page'),
     path('home/',views.home, name = 'home_page'),
]