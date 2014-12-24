from django.shortcuts import render, redirect

# Create your views here.
from courses.models import Courses, CoursesForms
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView

class CoursesListView(ListView):
    template_name = 'courses/list.html'
    model = Courses

class CoursesView(DetailView):
    template_name = 'courses/item.html'
    model = Courses

class CoursesCreate(CreateView):
    model = Courses
    template_name = 'courses/edit.html'
    success_url="/courses"

class CoursesUpdate(UpdateView):
    model = Courses
    template_name = 'courses/edit.html'
    success_url="/courses"

class CoursesDelete(DeleteView):
    model = Courses
    template_name = 'courses/del.html'
    success_url="/courses"
