from django.urls import path
from . import views

app_name = 'locate'
urlpatterns = [
    path('ground/',views.ground,name='ground'),

]