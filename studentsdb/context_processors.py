# from settings import PORTAL_URL


def students_proc(request):
    # print request
    # return {'PORTAL_URL' : PORTAL_URL}
    return {'PORTAL_URL' : request.META['wsgi.url_scheme']+'://'+request.META['SERVER_NAME']+':'+request.META['SERVER_PORT']}