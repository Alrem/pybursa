from django.shortcuts import render, redirect

# Create your views here.
from coaches.models import Coaches, CoachesForms


def coaches_list(request):
    coaches = Coaches.objects.all()
    return render(request, 'coaches/list.html', {'coaches': coaches})


def coaches_item(request, coaches_id):
    coache = Coaches.objects.get(id=coaches_id)
    return render(request, 'coaches/item.html', {'coache': coache})

def coaches_edit(request, coaches_id):
    coaches = Coaches.objects.get(id=coaches_id)
    if request.method == 'POST':
        form = CoachesForms(request.POST, instance=coaches)
        if form.is_valid():
            coaches = form.save()
            return redirect('Coach_list')
    else:
        form = CoachesForms(instance=coaches)
    return render(request,'coaches/edit.html', {'form': form})

def coaches_add(request):
    if request.method == 'POST':
        form = CoachesForms(request.POST)
        if form.is_valid():
            coaches = form.save()
            return redirect('Coach_list')
    else:
        form = CoachesForms()
    return render(request,'coaches/edit.html', {'form': form})
