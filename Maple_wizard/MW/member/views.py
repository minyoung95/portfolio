from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json타입
from member.models import Member


# 회원가입(약관동의)
def sigup01(request):
  return render(request, 'sigup01.html')

# 회원가입(정보입력)
def sigup02(request):
  return render(request, 'sigup02.html')

# 아이디 중복 확인
def idchk(request):
  m_id = request.POST.get("m_id","")
  qs = Member.objects.filter(m_id=m_id)

  print(m_id)
  print(qs)

  if qs:
    context = {"result":"success"}
  else:
    context = {"result":"fail"}
  return JsonResponse(context)


# 회원가입(정보 저장)
def signcp(request):
  if request.method == "POST":
    id = request.POST.get('아이디')
    pw = request.POST.get('비밀번호')
    name = request.POST.get('실명')
    nicName = request.POST.get('별명')
    gender = request.POST.get('gender')
    email = request.POST.get('이메일')
    print("변수", id, pw, name, nicName, gender, email)
    # Member.objects.create(m_id=id, m_password=pw, m_username=name, m_nickName=nicName, m_gender=gender, m_email=email)
    return redirect("member:sigcomp")
  else:  
    return render(request, 'signup02.html')

# 가입완료 
def sigcomp(request):
  return render(request, "sigcomp.html")



## 로그아웃
def logout(request):
  request.session.clear()
  return redirect("/")



## 로그인확인
def loginChk(request):
  m_id = request.POST.get("m_id","")
  m_password = request.POST.get("m_password","")
  # db확인
  qs = Member.objects.filter(m_id=m_id, m_password=m_password)
  # print("확인 : ",m_id,m_passpw)
  if qs:
    # 섹션추가
    request.session['session_m_id'] = qs[0].m_id
    request.session['session_m_nickName'] = qs[0].m_nickName
    list_qs = list(qs.values())
    context = {"result":"success","member":list_qs}  #dic,list타입
  else:
    context = {"result":"fail"}
  return JsonResponse(context)

## 로그인페이지
def login(request):
  return render(request,'login.html')
