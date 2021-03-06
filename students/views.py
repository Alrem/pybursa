from django.shortcuts import render, redirect

# Create your views here.

from students.models import Student, StudentForm
import logging
logger = logging.getLogger(__name__)


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def students_item(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/item.html', {'student': student})

def student_edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student.name = form.cleaned_data['student_name']
            student.surname = form.cleaned_data['student_surname']
            student.save()
            logger.info(student.name + ' ' + student.surname + ' was edit')
            return redirect('Student_list')
    else:
        form = StudentForm(initial={
            'student_name': student.name,
            'student_surname': student.surname,
            'student_email': student.email,
            'student_phone': student.phone,
            'student_package': student.package,
        })
    return render(request,'students/edit.html', {'form': form})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = Student()
            student.name = form.cleaned_data['student_name']
            student.surname = form.cleaned_data['student_surname'],
            student.email = form.cleaned_data['student_email'],
            student.phone = form.cleaned_data['student_phone'],
            student.package = form.cleaned_data['student_package']
            student.save()
            return redirect('Student_list')
    else:
        form = StudentForm(initial={
            'student_name': '',
            'student_surname': '',
            'student_email': '',
            'student_phone': '',
            'student_package': '',
        })
    return render(request,'students/edit.html', {'form': form})
