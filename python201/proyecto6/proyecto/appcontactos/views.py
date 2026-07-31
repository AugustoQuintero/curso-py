from django.shortcuts import render, redirect
from .models import Contacto
from .forms import ContactoForm

# Create your views here.
def myvista(solicitud):
    if solicitud.method == 'POST':
        form = ContactoForm(solicitud.POST)
        if form.is_valid():
            form.save()
            return redirect('myvista')
    else:
        form = ContactoForm()        
    contactos = Contacto.objects.all()
    context = {
        'form': form,
        'contactos': contactos
    }
    return render(solicitud, 'appcontactos/pagina.html', context)
