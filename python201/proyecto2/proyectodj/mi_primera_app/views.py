from django.shortcuts import render

# Create your views here.
def mi_vista(request):
    return render(request, 'mi_primera_app\car_list.html')
    