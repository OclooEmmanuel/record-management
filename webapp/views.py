from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from .models import Records

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


#-- homepage 
def home(request):
    return render(request,'webapp/index.html')


#-- Register view

def register(request):
    
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
        
    context = {'form':form}
    return render (request, 'webapp/register.html', context=context)

# ---------- Authentication starts
#-- Login
def my_login(request):
    form = LoginForm()
    if request.method =='POST':
        LoginForm(request, data=request.POST)
        
        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                
                return redirect("dashboard")
    
    context = {'loginform':form}
    return render(request, 'webapp/my-login.html',context=context)     

#-- User logout
def user_logout(request):
    auth.logout(request)
    
    return redirect("my-login")    

#------------- Authentication ends    


#-- Dashboard
@login_required(login_url='my-login')
def dashboard(request):
    my_records = Records.objects.all()
    
    context = {'records': my_records}
    
    return render(request, 'webapp/dashboard.html', context=context)


#-- Create record
@login_required(login_url='my-login')
def create_record(reqeust):
    
    form = CreateRecordForm()
    
    if reqeust.method == 'POST':    
        
        form = CreateRecordForm(reqeust.POST)
        if form.is_valid:
            form.save()
            return redirect("dashboard")
    
    context = {'createrecordform': form}
    
    return render(reqeust, 'webapp/create-record.html', context) 


#-- update record
@login_required(login_url='my-login')
def update_record(request, pk):
    
    record = Records.objects.get(id=pk)
    
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        
        if form.is_valid():
            form.save()
            
            return redirect('dashboard')
        
    context = {'updaterecordform':form}    
    return render(request, 'webapp/update-record.html', context)
    
 
    
        
#-- view single record
@login_required(login_url="my-login")
def view_record(request, pk):
    all_records = Records.objects.get(id=pk)
    context = {"record": all_records}
    
    return render(request, 'webapp/view-record.html', context)



# -- delete record
@login_required(login_url="my-login")
def delete_record(reqeust,pk):
    
    record = Records.objects.get(id=pk)
    record.delete()
    
    return redirect("dashboard")
    
    





