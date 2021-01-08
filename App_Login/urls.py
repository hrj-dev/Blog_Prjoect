from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup', views.sign_up, name='signup'),
    path('signin', views.login_page, name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_profile/', views.user_change, name='change_profile'),
    path('password/', views.pass_change, name='pass_change'),
    path('change-profile-image/', views.add_pro_pic, name='add_pro_pic'),
    path('change-image/', views.change_pro_pic, name='change_pro_pic')

]
