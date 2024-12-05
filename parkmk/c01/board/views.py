from django.shortcuts import render, get_object_or_404
from board.models import Board

# 게시판 삭제
def bdelete(request,bno):
  qs = Board.objects.get(bno=bno)
  qs.delete()
  context = {"dmsg":bno}
  return render(request,"blist.html",context)


# 게시판 수정
def bupdate(request):
  return render(request,'bupdate.html')


# 게시판 상세 보기
def bview(request):
  return render(request,'bview.html')


# 게시판
def blist(request):
  return render(request,'blist.html')


def bwrite(request):
  if request.method =="GET":
    return render(request,'bwrite.html')
  else:
    # id = request.session['session_id']
    # member =Member.objects.get(id=id)
    b_title=request.POST.get("b_title")
    b_content=request.POST.get("b_content")
    b_file=request.FILES.get("b_file","")
    print("파일정보 : ",b_file)
    qs = Board.objects.create(b_title=b_title,b_content=b_content,b_file=b_file)
    
    qs.save()

    context={'wmsg':"1"}
    return render(request, 'bwrite.html',context)