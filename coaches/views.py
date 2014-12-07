from django.shortcuts import render

# Create your views here.
from coaches.models import Coaches


def coaches_list(request):
    coaches = Coaches.objects.all()
    return render(request, 'coaches/list.html', {'coaches': coaches})


def coaches_item(request, coaches_id):
    coache = Coaches.objects.get(id=coaches_id)
    return render(request, 'coaches/item.html', {'coache': coache})