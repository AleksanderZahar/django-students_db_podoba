# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
    students = (
        {'id': 1,
         'first_name': u"Андрій",
         'last_name': u'Корост',
         'ticket': 257618,
         'image': 'img/me.jpeg'},
        {'id': 2,
         'first_name': u'Тарас',
         'last_name': u'Притула',
         'ticket': 255671,
         'image': 'img/piv.png'},
        {'id': 3,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'ticket': 359455,
         'image': 'img/podoba3.jpg'}
    )
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Student %s Edit Form</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Student %s Delete Form</h1>' % sid)