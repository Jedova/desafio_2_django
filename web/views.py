from django.shortcuts import render

# Create your views here.

def lista_empleados(request):
    empleados = [
        "Alejandra Faundez",
        "Nubia Ruiz",
        "Eduardo Jimenez",
        "Cristian Ovalle",
        "Andrés Aguilera",
        "Denisse Andreia",
    ]
    return render(request, "web/lista.html", {"empleados": empleados})