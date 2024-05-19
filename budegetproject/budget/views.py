import json
import random
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Project, Category, Expense
from django.views.generic import CreateView
from django.utils.text import slugify
from .forms import ExpensesForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'budget/project_list.html', {'project_list': projects})

def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    
    if request.method == 'GET':
        category_list = Category.objects.filter(project=project)
        expense_list = project.expenses.all()
        return render(request, 'budget/project_detail.html', {'project': project, 'expense_list': expense_list, 'category_list': category_list})
    
    elif request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category = form.cleaned_data['category']
            
            Expense.objects.create(
                project=project, 
                title=title,
                amount=amount,
                category=category
            ).save()
            
    elif request.method == 'DELETE': 
        id = json.loads(request.body)['id']
        expense = get_object_or_404(Expense, id=id)
        expense.delete()
        
        return HttpResponse('')
    
    return HttpResponseRedirect(reverse('detail', kwargs={'project_slug': project_slug}))

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'budget/add_project.html'
    fields = ('name', 'budget')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        slug = slugify(self.object.name)

        while Project.objects.filter(slug=slug).exists():
            slug += str(random.randint(1, 1000))
        self.object.slug = slug
        
        self.object.save()

        categories = self.request.POST.get('categoriesString', '').split(',')
        for category in categories:
            if category.strip():
                Category.objects.create(
                    project=self.object,
                    name=category.strip()
                )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('detail', kwargs={'project_slug': self.object.slug})
