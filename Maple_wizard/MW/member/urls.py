from django.urls import path,include
from . import views

app_name = "member"
urlpatterns = [
    path('login/', views.login,name="login"),
    path('logout/', views.logout,name="logout"),
    path('loginChk/', views.loginChk,name="loginChk"),
    path('sigup01/', views.sigup01,name="signup01"),
    path('sigup02/', views.sigup02,name="signup02"),
    path('idchk/', views.idchk,name="idchk"),
    path('signcp/', views.signcp,name="signcp"),
    path('sigcomp/', views.sigcomp,name="sigcomp"),
]