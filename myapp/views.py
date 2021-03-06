from django.shortcuts import render
from .forms import my_form
from . import task1
import json
from django.core.exceptions import ValidationError
from django.shortcuts import redirect


# Create your views here.

def index(request):
    form = my_form()
    if request.method == "POST":
        form = my_form(request.POST)
        if form.is_valid(): 
            user = form.cleaned_data["user"]
            profile = form.cleaned_data["profile"]
            sDate = form.cleaned_data["s_date"]
            eDate = form.cleaned_data["e_date"]
            if sDate > eDate:
                myerror = "EndDate must be greater than StartDate !"
                return render(request,'homepage.html',{'form':form,'myerror':myerror})
            task1.insert_profile(user,profile,sDate,eDate)
            return redirect('detail', uname=user)
        else:
            print("not valid form")
            print(form.errors)
        
        return render(request,'homepage.html',{'form':form})
    else:
        form = my_form()
        return render(request,'homepage.html',{'form':form})
    
def show_profile(request):
    print("HEREEEEEEEEEEEEEEEEEEEEEEEEEE")
    data = task1.show_all_profile()
    return render(request,'user_info.html',{'data':data})

def thank_you(request):
    return render(request,'thank_you.html')

def about(request):
    return render(request,'about.html')

def detail(request,uname):
    uName = uname
    single_user_profiles = task1.get_single_user(uName)
    return render(request,'detail.html',{'profiles':single_user_profiles,'uname':uname})