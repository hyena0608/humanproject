from django.contrib import admin
from django.urls import path
from . import views
from account.views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('signup/', register_view, name="signup"),
    path('logout/', logout_view, name="logout"),
    path('mypage/', mypage, name="mypage"),
]