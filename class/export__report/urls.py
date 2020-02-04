from django.urls import path
from . import views

urlpatterns = [
path('dashbord/', views.Dashbord, name = 'Dashbord'),
    path('export/', views.Export, name = 'Export')
]