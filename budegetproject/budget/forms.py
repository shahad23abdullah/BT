from django import forms
from .models import Category

class ExpensesForm(forms.Form):
    title = forms.CharField()
    amount = forms.IntegerField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())