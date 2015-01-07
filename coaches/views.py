from django.shortcuts import render, redirect

# Create your views here.
from coaches.models import Coaches
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

import logging
logger = logging.getLogger(__name__)

class CoachesListView(ListView):
    template_name = 'coaches/list.html'
    model = Coaches

class CoachesView(DetailView):
    template_name = 'coaches/item.html'
    model = Coaches

class CoachesCreate(CreateView):
    model = Coaches
    template_name = 'coaches/edit.html'
    success_url=reverse_lazy('Coach_list')
    def form_valid(self, form):
        obj = form.save()
        logger.info('Create new coach' + obj.name + ' ' + obj.surname)
        return super(CoachesCreate, self).form_valid(form)

class CoachesUpdate(UpdateView):
    model = Coaches
    template_name = 'coaches/edit.html'
    success_url=reverse_lazy('Coach_list')
    def form_valid(self, form):
        obj = form.save()
        logger.info('Coach ' + obj.name + ' ' + obj.surname + ' update')
        return super(CoachesUpdate, self).form_valid(form)

class CoachesDelete(DeleteView):
    model = Coaches
    template_name = 'coaches/del.html'
    success_url=reverse_lazy('Coach_list')
