from django.http import request
from django.shortcuts import render,redirect
from django.views.generic import View,RedirectView
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout
from .models import User
from django.utils.decorators import method_decorator

class LoginView(View):

    def get(self,request):
        return render(request,'Accounts/login.html',{"form":LoginForm()})
    
    def post(self,request):
        context={}
        error=False
        form=LoginForm(request.POST)
        if(form.is_valid()):
            phonenumber=form.cleaned_data['phonenumber']
            password=form.cleaned_data['password']
            print(phonenumber,password)
            log=authenticate(request,phonenumber=phonenumber,password=password)
            if(log is not None):
                login(request,log,backend='django.contrib.auth.backends.ModelBackend')
                return redirect("Home:home")
            else:
                error="Enter Valid Details.!"
        else:
            try:
                error=list(form.errors.values())[0][0]
            except:
                error="Try Again with Valid Details"
        context['form']=form
        context['error']=error
        return render(request,'Accounts/login.html',context)    




class SignupView(View):

    def get(self,request):
        return render(request,'Accounts/signup.html',{"form":RegisterForm()})
    
    def post(self,request):
        context={}
        form=RegisterForm(request.POST)
        error=False
        if(form.is_valid()):
            full_name=form.cleaned_data.get('full_name')
            phonenumber=form.cleaned_data.get('phonenumber')
            email=form.cleaned_data.get('email')
            password1=form.cleaned_data.get('password1')
            password2=form.cleaned_data.get('password2')
            if(password1==password2):
                try:
                    User.objects.create_user(full_name=full_name,phonenumber=phonenumber,email=email,password=password2)
                    return redirect("Accounts:login")
                except:
                    error="Try again with Valid details"
            else:
                error="Passwords Not Matched"
        else:
            error=list(form.errors.values())[0][0]
        context['form']=form
        context['error']=error
        return render(request,'Accounts/signup.html',context)


class LogoutView(RedirectView):
    url = '/'
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


    
