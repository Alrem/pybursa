from django.shortcuts import render

# Create your views here.
from courses.models import Courses


def courses_list(request):
    courses = Courses.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})


def courses_item(request, courses_id):
    courses = Courses.objects.get(id=courses_id)
    return render(request, 'courses/item.html', {'courses': courses})