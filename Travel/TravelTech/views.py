from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def rules(request):
    return render(request,'rules.html')

def signs(request):
    return render(request,'signs.html')

def table(request):
    q=Register.objects.all
    return render(request,'table.html',{"data":q})
def emrgno(request):
    return render(request,'emrgno.html')

def register(request):
    if request.method=='POST':
        na=request.POST.get('name')
        add=request.POST.get('address')
        mno=request.POST.get('mobile')
        pas=request.POST.get('pwd')
        print(na,mno,add,mno,pas)

        obj=Register()
        obj.name=na
        obj.ad=add
        obj.phno=mno
        obj.pa=pas
        obj.save()
        return redirect('Index')

    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        naa=request.POST.get('nam')
        passs=request.POST.get('pwdd')
        #print(naa,passs)
        q=Register.objects.get(name=naa)
        if q.pa==passs:
            return redirect('Index')
        else:
            return HttpResponse("You not have an account, please sign up !!")
    return render(request,"login.html")