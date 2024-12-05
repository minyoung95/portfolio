
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('test/',views.index2,name='index2'),
    path('test2/',views.index3,name='index3'),
]
