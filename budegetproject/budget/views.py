from django.shortcuts import render , get_object_or_404
from .models import Project , Expense ,Category

def project_list(request):
    return render(request , 'budget/project_list.html')



def project_detail(request , project_slug):
    project = get_object_or_404(Project , slug = project_slug)
    expense_list = project.expenses.all()
    return render(request , 'budget/project_detail.html', {'project': project , 'expense_list':expense_list })