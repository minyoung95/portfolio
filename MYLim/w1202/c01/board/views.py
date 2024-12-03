from django.shortcuts import render
from board.models import Board
from member.models import Member
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

def bwrite(request):
  if request.method =="GET":
    return render(request,'bwrite.html')
  else:
    # id = 'aaa'
    # member = Member.objects.filter(id=id)
    b_title=request.POST.get("b_title")
    b_content=request.POST.get("b_content")
    b_file=request.FILES.get("b_file","")
    print("파일정보 : ",b_file)
    qs = Board.objects.create(b_title=b_title,b_content=b_content,b_file=b_file)
  
    context={'wmsg':"1"}
    return render(request, 'bwrite.html',context)
  
def bview(request,b_no):
  return render(request,'bview.html')