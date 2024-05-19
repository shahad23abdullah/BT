from django.db import models # type: ignore
from django.utils.text import slugify # type: ignore

class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.IntegerField()

    def save(self, *args, **kwargs):
        # If the slug is not provided or empty, generate it from the project name
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def budget_left(self):  
        expense_list = Expense.objects.filter(project = self)
        total_expense_amount = sum(expense.amount for expense in expense_list)
        return self.budget - total_expense_amount
    def total_expense(self):
        expense_list = Expense.objects.filter(project = self)
        return len (expense_list)
class Category(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE , related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    class Meta:
        ordering = ('-amount',)