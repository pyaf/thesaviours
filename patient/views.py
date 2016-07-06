from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import PatientForm
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request,'homepage.html')

def look(request):
    return render(request, 'lookinside.html')
@login_required(login_url='login/')
def  mainpage(request):
    return render(request, 'mainpage.html')

@login_required(login_url='login/')
def formpage(request):
    if (request.method == "POST"): #and ("submit" in request):
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'post_form.html')
        else:
            return HttpResponse('Fill the form correctly')
    else:
        form = PatientForm()
        return render(request,'formpage.html',{'form': form})

@login_required(login_url='login/')
def doc(request):
    return render(request, 'severitydoc.html')
