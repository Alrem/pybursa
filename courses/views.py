from django.shortcuts import render, redirect

# Create your views here.
from courses.models import Courses
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

import logging
logger = logging.getLogger(__name__)


class CoursesListView(ListView):
    template_name = 'courses/list.html'
    model = Courses


class CoursesView(DetailView):
    template_name = 'courses/item.html'
    model = Courses

class CoursesCreate(CreateView):
    model = Courses
    template_name = 'courses/edit.html'
    success_url=reverse_lazy('Course_list')
    def form_valid(self, form):
        obj = form.save()
        logger.info('Create new course ' + obj.title)
        return super(CoursesCreate, self).form_valid(form)


class CoursesUpdate(UpdateView):
    model = Courses
    template_name = 'courses/edit.html'
    success_url=reverse_lazy('Course_list')
    def form_valid(self, form):
        obj = form.save()
        logger.info('Course ' + obj.title + ' was update')
        return super(CoursesUpdate, self).form_valid(form)

class CoursesDelete(DeleteView):
    model = Courses
    template_name = 'courses/del.html'
    success_url=reverse_lazy('Course_list')
