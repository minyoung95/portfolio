from django.shortcuts import render
from food.models import Food_inform
from food.models import Store
from food.models import Eat
from member.models import Member
from django.http import JsonResponse

def eat(request):
  qc = Eat.objects.all()
  context={'flist':qc}
  return render(request,'eat.html',context)

def niku(request,e_name):
  m_id = request.session.get('session_m_id')
  qs = Store.objects.filter(s_foodname__f_name=e_name)
  qx = Food_inform.objects.filter(f_name=e_name)
  qv = Food_inform.objects.get(f_name=e_name)
  
  count = qv.f_like_members.count()
  
  # 좋아요 상태 확인
  if qv.f_like_members.filter(pk=m_id).exists():
    result = '1'
    count = qv.f_like_members.count()
  else:
    result = '0'
  
  context = {'informs': qs,'foods':qx, 'food2':qv,
             'result':result, 'count':count}
  return render(request,'niku.html',context)

def flike(request):
  m_id = request.session['session_m_id']
  member = Member.objects.get(m_id=m_id)
  f_no = request.POST.get('f_no')
  f_informs = Food_inform.objects.get(f_no=f_no)
  
  if f_informs.f_like_members.filter(pk=m_id).exists(): # 좋아요 클릭상태
    f_informs.f_like_members.remove(member)
    result = 'remove'
  else:
    f_informs.f_like_members.add(member)
    result = 'add'
    
  context = {'result':result, 'count':f_informs.f_like_members.count()}
  
  return JsonResponse(context)