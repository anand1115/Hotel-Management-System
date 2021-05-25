from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from Accounts.decorators import admin_required

# Create your views here.
class HomeView(View):
    @method_decorator(admin_required())
    def get(self,request):
        context={}
        return render(request,"Home/Home.html",context)

class ContactView(View):
    def get(self,request):
        context={}
        return render(request,"Home/Contact.html",context)

class AboutView(View):
    def get(self,request):
        context={}
        return render(request,"Home/About.html",context)