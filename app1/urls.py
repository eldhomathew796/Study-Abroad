from django.urls import path
from . import views 
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
        path('',views.home, name='home' ),
        path('newlyassignleads',views.newlyassignleads,name='newlyassignleads'),
        path('previousleads',views.previousleads,name="previousleads"),
        path('currentleads',views.currentleads,name='currentleads'),
        path('login',views.login,name='login'),
        path('register',views.register,name='register'),
        path('dashboard',views.dashboard,name='dashboard')

]