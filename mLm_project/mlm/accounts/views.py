from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
##############
# Create your views here.

# def home(request):
#     return render(request,'accounts/home.html')

def register_request(request):
    if request.method == "POST":
        # import pdb
        # pdb.set_trace
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            group = Group.objects.get(name="UPA")
            user.save()
            user.groups.add(group)
            login(request,user)
            messages.success(request,'Registration Successful.')
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request,form.errors)
        messages.error(request,'Unsuccessful registration. Invalid information')

    form = NewUserForm()
    context = {'register_form':form}
    return render(request,'accounts/registration.html',context)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,'Invalid username or password')

    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request,'accounts/login.html',context)

def logout_request(request):
    logout(request)
    messages.info(request,'You have Successfully logged out.')
    return redirect('login')
