from settings import PORTAL_URL


def students_proc(request):
    # print request
    # print request.META['HTTP_HOST']
    return {'PORTAL_URL': PORTAL_URL}
    # return {'PORTAL_URL': request.META['wsgi.url_scheme']+'://'+request.META['SERVER_NAME']+':'+request.META['SERVER_PORT']}
    # return {'PORTAL_URL': request.META['wsgi.url_scheme']+'://'+request.META['HTTP_HOST']}

# HTTP_HOST