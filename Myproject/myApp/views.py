from django.shortcuts import render,redirect,get_object_or_404
from . forms import studentForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import *
# create your views here
from . models import * 
# define your logic here
def retrievestd(request):
    std_data = student.objects.all()
    context = {'std_data':std_data}
    return render(request,'myApp/std_detail.html',context)
def registerstudent(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        sname = request.POST['sname']
        email = request.POST['email']
        age = request.POST['age']
        reg = request.POST['regNo']
        std = student(FirstName=fname,SecondName=sname,email=email,Age=age,regNo=reg)
        std.save()
        return redirect(Home)
    else:
        return render (request,'myApp/std_form.html')
def userRegistration(request):
    if request.method == 'POST':
        form=customUser(request.POST)
        if form.is_valid():
            form.save()
        return redirect(login)
    else:
        context={'form':form}
        return render(request,'myApp/regist.html',context)

# Create your views here.
def Home(request):
    return render(request,'myApp/index.html')
def updateStd(request,pk):
    stud =get_object_or_404(student,pk=pk)
    if request.method=='POST':
        new_Firstname=request.POST.get('fname')
        new_Secondname=request.POST.get('sname')
        new_Email=request.POST.get('email')
        new_Age=request.POST.get('Age')
        new_regNo=request.POST.get('regNo')
        stud.fname=new_fname
        stud.lname=new_lname
        stud.email=new_email
        stud.age=new_age
        stud.regNo=new_regNo
        stud.save()
        return redirect('fetch_std')
    else:    
        context={'stud':stud}
    return render(request,'myApp/updateStd.html', context)
    
def deleteStd(request,pk):
    del_std=get_object_or_404(student,pk=pk)
    if request.method=='POST':
        del_std.delete()
        return redirect ('fetch_std')
    else:
        return render(request,'myApp/deleteStd.html')

           


# def stdForm(request):
#     if request.method== 'POST':
#         form = studentForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('home')
#     else:
#         form=studentForm()
#         context={'form':'form'}
#     return render(request,'MyApp/stdform.html', context)
    
            
    
        