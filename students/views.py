from django.shortcuts import render
from django.http import HttpResponse


# Views for Students

def students_list(request):
    return render(request, 'students/students_list.html', {})


def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Student %s Edit Form</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Student %s Delete Form</h1>' % sid)


# Views for Groups

def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Group %s Edit Form</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Group %s Delete Form</h1>' % gid)