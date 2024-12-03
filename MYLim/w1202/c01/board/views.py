from django.shortcuts import render
from board.models import Board
from django.db.models import Q
from django.core.paginator import Paginator # 페이지 넘버링

# Create your views here.
def blist(request):
  npage = int(request.GET.get('npage',1))
  qs = Board.objects.all().order_by('-b_no')
  cl = request.GET.get('cl','')
  searchType = request.GET.get('type','b_title')
  
  if cl:
    if searchType == 'b_title':
      qs = Board.objects.filter(b_title__icontains=cl)
    elif searchType == 'b_content':
      qs = Board.objects.filter(b_content__icontains=cl)
    elif searchType == 'b_title_content':
      qs = Board.objects.filter(Q(b_title__icontains=cl)|Q(b_content__icontains=cl))
  
  paginator = Paginator(qs,2)
  blist = paginator.get_page(npage)
  context = {'blist':blist,'npage':npage,'cl':cl,'searchType':searchType}
  return render(request,'blist.html',context)