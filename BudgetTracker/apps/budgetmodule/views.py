from django.shortcuts import render

def index(request):
    #study the request 
    return render(request ,'budgetmodule/index.html') # rendering a template 