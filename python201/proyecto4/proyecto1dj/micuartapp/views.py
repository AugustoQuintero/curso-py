from django.shortcuts import render

# Create your views here.
def mi_vista(request):
    lista_car = [
        {'title': 'BMW'},
        {'title': 'Mazda'},
    ]
    con = {
        'lista': lista_car
    }
    return render(request, 'micuartapp/lista_carros.html', context=con)


