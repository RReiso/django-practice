from django.shortcuts import render
from .models import Student

# Create your views here.


def studentlist(request):
    students = Student.objects.all()
    data = {'students': students}
    return render(request, 'studentlist.html', data)
