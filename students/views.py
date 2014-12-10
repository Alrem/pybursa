from django.shortcuts import render

# Create your views here.

from students.models import Student


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def students_item(request, student_id):
    student = Student.objects.get(id=student_id)
    print type(student.courses)
    return render(request, 'students/item.html', {'student': student})