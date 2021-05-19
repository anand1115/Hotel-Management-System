from django.shortcuts import redirect, render
from django.views.generic import View
from . import forms 
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.


class BookingView1(View):

    def render(self,request,context={}):
        return render(request,'Bookings/booking1.html',context)

    def get(self,request):
        context={}
        context['form']=forms.BookingForm1()
        if(self.get_session(request)):
            context['form']=forms.BookingForm1(self.get_session(request))
        return self.render(request,context)
    
    def post(self,request):
        context={}
        error=False
        form=forms.BookingForm1(request.POST)
        if(form.is_valid()):
            self.set_session(request,form.cleaned_data)
            print(form.cleaned_data)
        else:
            error=list(form.errors.values())[0][0]
        context['form']=form
        context['error']=error
        return self.render(request,context)
    
    def set_session(self,request,data):
        request.session['basic']=json.dumps(data,sort_keys=True,indent=1,cls=DjangoJSONEncoder)

    
    def get_session(self,request):
        if(request.session.get('basic',False)):
            return json.loads(request.session['basic'])
        else:
            return False



class BookingView2(View):
    def render(self,request,context={}):
        return render(request,"Bookings/booking2.html",context)
    
    def get(self,request):
        context={}
        basic=BookingView1().get_session(request)
        if(not basic):
            return redirect("Bookings:booking1")
        context["basic"]=basic 
        return self.render(request,context)
    
    def get_session(self,request):
        if(request.session.get('basic',False)):
            return json.loads(request.session.get('basic'))
        else:
            return False


class BookingView3(View):
    def render(self,request,context={}):
        return render(request,"Bookings/booking3.html",context)
    
    def get(self,request):
        context={}
        data=BookingView2().get_session(request)
        if(not data):
            return redirect("Bookings:booking2")
        context['data']=data
        return self.render(request,context)


class BookingView4(View):
    def render(self,request,context={}):
        return render(request,"Bookings/booking4.html",context)
    
    def get(self,request):
        context={}
        data=BookingView2().get_session(request)
        if(not data):
            return redirect("Bookings:booking2")
        context['data']=data
        return self.render(request,context)

