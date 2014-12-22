from django.shortcuts import render, redirect

# Create your views here.
from courses.models import Courses, CoursesForms


def courses_list(request):
    courses = Courses.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})


def courses_item(request, courses_id):
    courses = Courses.objects.get(id=courses_id)
    return render(request, 'courses/item.html', {'courses': courses})


def courses_edit(request, courses_id):
    courses = Courses.objects.get(id=courses_id)
    if request.method == 'POST':
        form = CoursesForms(request.POST, instance=courses)
        if form.is_valid():
            courses = form.save()
            return redirect('Course_list')
    else:
        form = CoursesForms(instance=courses)
    return render(request,'courses/edit.html', {'form': form})

def courses_add(request):
    if request.method == 'POST':
        form = CoursesForms(request.POST)
        if form.is_valid():
            courses = form.save()
            return redirect('Course_list')
    else:
        form = CoursesForms()
    return render(request,'courses/edit.html', {'form': form})
