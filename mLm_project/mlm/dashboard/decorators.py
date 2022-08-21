from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import Http404
def allowed_user(allowed_user = []):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_user:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("You are not authorized to view this page!")
        return wrapper_func
    return decorator



def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == "Admin":
            return view_func(request,*args,**kwargs)
        if group == "UPA":
            return redirect('/')
        else:
            return HttpResponse("you are not authorized for this page")
            # return redirect()
    return wrapper_func