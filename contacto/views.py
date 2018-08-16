from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from contacto.forms import FormularioContactos

def contactos(request):
    errors=[]
    if request.method=='POST':
        form=FormularioContactos(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            send_mail(
                cd['asunto'],
                cd['mensaje'],
                cd.get('email','noreply@example.com'),['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contacto/gracias/')
    else:
        form=FormularioContactos(initial={'asunto':'¡Adoro tu sitio!'})
    return render(request,'contacto/formulario-contactos.html',{'form':form})
