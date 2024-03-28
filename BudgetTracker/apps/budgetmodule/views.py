from django.shortcuts import render

def index(request):
    #study the request 
    return render(request ,'budgetmodule/index.html') # rendering a template 



def budget(request):
   return render(request ,'budgetmodule/userBudget.html') # rendering a template 


def task1(request):
   return render(request ,'budgetmodule/task1.html') # rendering a template 