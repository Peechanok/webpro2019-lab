from django.urls import path
from . import views

urlpatterns = [
path('allstudent/<str:NumberAll>', views.Stu_all, name = 'Stu_all'),
path('addstudent/<int:Adds>', views.Add, name = 'Add'),
path('modifystudent/', views.Modify, name = 'Modify'),
path('allsubject/', views.Stu_all, name = 'Sub_all'),
path('addsubject/', views.Sub_Add, name = 'Sub_Add'),
path('modifysubject/', views.Sub_Modify, name = 'Sub_Modify')
]