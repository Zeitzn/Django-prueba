from django.http import HttpResponse
import datetime
def hola(request):
    return HttpResponse("Hola Mundo")

def raiz(request):
    return HttpResponse("Vista Principal")

def fecha_actual(request):
    ahora=datetime.datetime.now()
    html="<html><body><h1>Fecha:</h1><h3>%s</h3></body></html>" % ahora
    return HttpResponse(html)

def horas_adelante(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    # assert False
    html="<html><body><h1>En %s hora(s), serán:</h1><h3>%s</h3></body></html>" % (offset,dt)
    return HttpResponse(html)
