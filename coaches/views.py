from django.shortcuts import render, redirect

# Create your views here.
from coaches.models import Coaches
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

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

class CoachesUpdate(UpdateView):
    model = Coaches
    template_name = 'coaches/edit.html'
    success_url=reverse_lazy('Coach_list')

class CoachesDelete(DeleteView):
    model = Coaches
    template_name = 'coaches/del.html'
    success_url=reverse_lazy('Coach_list')
