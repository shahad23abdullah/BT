from django.urls import path, include
from apps.budgetmodule import views
urlpatterns = [
    path('', views.index, name='index'),
]
