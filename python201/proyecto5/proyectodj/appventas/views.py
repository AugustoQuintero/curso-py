from django.shortcuts import render

# Create your views here.
def myvista(solicitud):
    elementos = [
        {'titul':"Primer elemento"},
        {'titul':'Segundo elemento'},
        {'titul':'Tercer elemento'},
        {'titul':'Cuarto elemento'},
    ]
    com = {
        'elementos':elementos        
    }
    return render(solicitud, 'index.html', context=com)