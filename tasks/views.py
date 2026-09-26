from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'task-list.html'