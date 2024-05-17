import random
from django.http import HttpResponseRedirect
from django.shortcuts import render , get_object_or_404 
from django.urls import reverse
from .models import Project ,Category
from django.views.generic import CreateView
from django.utils.text import slugify

def project_list(request):
    return render(request , 'budget/project_list.html')



def project_detail(request , project_slug):
    project = get_object_or_404(Project , slug = project_slug)
    catogery_list = 
    expense_list = project.expenses.all()
    return render(request , 'budget/project_detail.html', {'project': project , 'expense_list':expense_list })



class ProjectCreateView(CreateView):
    model = Project
    template_name = 'budget/add_project.html'
    fields = ('name', 'budget')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        
        # Generate a unique slug based on the project name
        slug = slugify(self.object.name)
        # Check if a project with the same slug already exists
        while Project.objects.filter(slug=slug).exists():
            # If a project with the same slug exists, append a random suffix
            slug += str(random.randint(1, 1000))
        self.object.slug = slug
        
        self.object.save()

        # Process categories
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