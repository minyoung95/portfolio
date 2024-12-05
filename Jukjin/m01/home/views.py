from django.shortcuts import render

# Create your views here.
def index(reqeust):
  return render(reqeust,'index.html')

def index2(request):
  return render(request,'test4.html')
  
def index3(request):
  return render(request,'imdex2.html')