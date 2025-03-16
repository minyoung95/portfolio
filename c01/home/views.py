from django.shortcuts import render
from member.models import Member
from board.models import Board
from location.models import Location_inform
from food.models import Food_inform
from django.db.models import Count
from itertools import chain

# Create your views here.
def index(request):
  qs = Board.objects.annotate(like_count=Count('b_like_members')).order_by('-like_count')[:6]
  qx = Board.objects.all().order_by('-b_date')[:6]
  
  location_qs = Location_inform.objects.annotate(like_count=Count('l_like_members'))
  food_qs = Food_inform.objects.annotate(like_count=Count('f_like_members'))
  
  l_f_qs = sorted(chain(location_qs,food_qs),
                  key=lambda x: x.like_count,
                  reverse=True)[:10]
  
  context = {'likes':qs, 'recents' : qx, 'popularity': l_f_qs}
  return render(request,'index.html',context)