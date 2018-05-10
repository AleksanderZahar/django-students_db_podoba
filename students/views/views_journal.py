# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Views for Student Visiting


def journal_list(request):
    return render(request, 'students/stud_visiting_list.html', {})


# def groups_add(request):
#     return HttpResponse('<h1>Group Add Form</h1>')
#
#
# def groups_edit(request, gid):
#     return HttpResponse('<h1>Group %s Edit Form</h1>' % gid)
#
#
# def groups_delete(request, gid):
#     return HttpResponse('<h1>Group %s Delete Form</h1>' % gid)