from django.shortcuts import render

# Create your views here.
from address.models import Address


def address_list(request):
    address = Address.objects.all()
    return render(request, 'address/list.html', {'address': address})


def address_item(request, address_id):
    address = Address.objects.get(id=address_id)
    return render(request, 'address/item.html', {'address': address})
