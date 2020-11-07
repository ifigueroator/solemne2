from django.shortcuts import render
from mantenedor import templates
from django.http import HttpResponse

def home(request):
    template = "home.html"
    context = {}    
    return render(request, template, context)

def PlanHogar(request):    
    return render(request, "PlanHogar.html")

def PlanEmpresa(request):    
    return render(request, "PlanEmpresa.html")