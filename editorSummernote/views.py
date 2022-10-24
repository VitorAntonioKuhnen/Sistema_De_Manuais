from django.shortcuts import render
from .models import Manuais
def principal(request):
    manuais = Manuais.objects.all()
    return render(request, 'manuais.html', {'manuais':manuais})
