from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json타입
from member.models import Member
from board.models import Board
from comment.models import Comment

def cwrite(request):
  m_id = request.session['session_m_id']
  member = Member.objects.get(m_id=m_id)
  b_no = request.POST.get('b_no',1)
  board = Board.objects.get(b_no=b_no)
  c_pw = request.POST.get('c_pw','')
  c_content = request.POST.get('c_content','')
  print('확인 : ',c_pw,c_content)
  
  qs = Comment.objects.create(member=member,board=board,c_pw=c_pw,c_content=c_content)
  list_qs = list(Comment.objects.filter(c_no=qs.c_no).values())
  print('확인2 : ',list_qs)
  context = {'result':'success','comment':list_qs}
  return JsonResponse(context)