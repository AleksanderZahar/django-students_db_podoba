# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Views for Groups

def groups_list(request):
    groups = (
        {'id': 1,
         'group_name': u"МтМ-21",
         'group_lead': u'Ячнев Ярік',
         },
        {'id': 2,
         'group_name': u"МтМ-22",
         'group_lead': u'Подоба Віталій',
         },
        {'id': 3,
         'group_name': u"ЛН-71",
         'group_lead': u'Захаров Олександр',
         }
    )
    return render(request, 'students/group_list.html', {'groups': groups})
    # return HttpResponse('<h1>Groups Listing</h1>')


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Group %s Edit Form</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Group %s Delete Form</h1>' % gid)