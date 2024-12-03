from django.shortcuts import render

# 게시판
def blist(request):
  return render(request,'blist.html')


# 글쓰기
def bwrite(request):
  return render(request,'bwrite.html')
