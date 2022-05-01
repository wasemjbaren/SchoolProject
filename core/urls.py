
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [

    path('', login_page, name='login'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('logout/', logout_user, name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('account-settings/', AccountSettingsView.as_view(), name='account_settings'),
    path('donee/',ProfileView.donee,name='donee'),

    path('done/', ProfileView.done, name='done'),

]