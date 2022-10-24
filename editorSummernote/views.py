from django.shortcuts import render
from .models import Manuais
def principal(request):
    manuais = Manuais.objects.all()

    busca = request.GET.get('search')
    if busca:
        print(busca)
        manuais = Manuais.objects.filter(conteudo = busca)
        print(manuais)
    return render(request, 'manuais.html', {'manuais':manuais})
