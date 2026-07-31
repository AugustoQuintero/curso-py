from django.shortcuts import render, redirect
from .models import Contacto
from .forms import ContactoForm

# Create your views here.
def myview(solicitud):
    if solicitud.method == 'POST':
        formul = ContactoForm(solicitud.POST)
        if formul.is_valid():
            formul.save()
            return redirect('myview')
    else:
        formul = ContactoForm()
    conts = Contacto.objects.all()
    context = {'formul':formul, 'conts':conts}
    return render(solicitud, 'app_contactos/index.html', context)
