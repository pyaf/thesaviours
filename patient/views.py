from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import PatientForm

def formpage(request):
    if (request.method == "POST"): #and ("submit" in request):
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('THANKS')
    else:
        form = PatientForm()
        return render(request,'formpage.html',{'form': form})