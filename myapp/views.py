from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def register(request):
    f=myregisterform()
    if request.method=="POST":
        f1=myregisterform(request.POST)
        if f1.is_valid():
            f1.save()
            return HttpResponse("registraration sucess")
    return render(request,'admin/register.html',{'f':f})

def Login(request):
    f=myloginform()
    if request.method=="POST":
        f1=myloginform(request.POST)
        if f1.is_valid():
            username=f1.cleaned_data['username']
            password=f1.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse("login error")
    return render(request,'admin/login.html',{'f':f})

@login_required(login_url='Login')
def course(request):
    f = coursesForm()
    if request.method == 'POST':
        form = coursesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            data=courses.objects.all()
            return render(request,'admin/coursemenu.html',{'data':data})
    return render(request, 'admin/course.html', {'f': f})

@login_required(login_url='Login')
def courseconcept(request):
    f = courseconceptsform()
    if request.method == 'POST':
        form = courseconceptsform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Redirect after form submission') 
    return render(request, 'admin/courseconcept.html', {'f': f})

@login_required(login_url='Login')
def admincoursemenu(request):
    data=courses.objects.all()
    return render(request,'admin/coursemenu.html',{'data':data})

@login_required(login_url='Login')
def admincoursedelete(request,id):
    data=courses.objects.get(id=id)
    data.delete()
    return redirect('coursemenu')

@login_required(login_url='Login')
def admincourseupdate(request,id):
    data=courses.objects.get(id=id)
    f=coursesForm(instance=data)
    if request.method == 'POST':
        form = courseconceptsform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('coursemenu')
    return render(request,'admin/course.html',{'f':f})


def Logout(request):
    logout(request)
    return redirect('home')

    