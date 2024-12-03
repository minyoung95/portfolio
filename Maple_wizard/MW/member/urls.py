from django.urls import path,include
from . import views

app_name = "member"
urlpatterns = [
    path('login/', views.login,name="login"),
    path('logout/', views.logout,name="logout"),
    path('loginChk/', views.loginChk,name="loginChk"),
    path('signup01/', views.signup01,name="signup01"),
    path('signup02/', views.signup02,name="signup02"),
]