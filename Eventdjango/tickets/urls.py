
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('',views.home, name='tickets_home'),
     path('login/',views.my_login, name='tickets_login'),
     path('logout/',views.my_logout, name='tickets_logout'),
     path('signin/',views.sign_in, name='tickets_signin'),
     path('profile/changepassword/',views.change_password, name='tickets_change_password'),
     path('profile/edit/update/<int:user_id>/',views.update_profile, name='tickets_user_update'),
     path('profile/edit/',views.profile, name='tickets_user_profile'),
     path('profile/popularcheck/',views.poppular_check, name='tickets_poppular_check')
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
