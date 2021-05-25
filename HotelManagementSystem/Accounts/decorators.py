from functools import wraps
from django.shortcuts import redirect

def admin_required():
    def decorator(func):
        @wraps(func)
        def wrapper(request,*args,**kwargs):
            if request.user.is_authenticated and request.user.admin:
                return func(request,*args,**kwargs)
            else:
                return redirect("Accounts:login")
        return wrapper
    return decorator

def staff_required():
    def decorator(func):
        @wraps(func)
        def wrapper(request,*args,**kwargs):
            if request.user.is_authenticated and request.user.staff:
                return func(request,*args,**kwargs)
            else:
                return redirect("Accounts:login")
        return wrapper
    return decorator



