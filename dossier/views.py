from django.shortcuts import render

# Create your views here.
from dossier.models import Dossier


def dossier_list(request):
    dossier = Dossier.objects.all()
    return render(request, 'dossier/list.html', {'dossier': dossier})


def dossier_item(request, dossier_id):
    dossier = Dossier.objects.get(id=dossier_id)
    return render(request, 'dossier/item.html', {'dosier': dossier})

