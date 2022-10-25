from django.shortcuts import render
from .models import Manuais
def principal(request):
    manuais = Manuais.objects.all()

    busca = request.GET.get('search')
    if busca:
        print(busca)
        manuais = Manuais.objects.filter(conteudo__icontains = busca) #O termo icontains serve para realizarmos uma busca com o que foi digitado
        print(manuais)
    return render(request, 'manuais.html', {'manuais':manuais})


def manual(request, id):
    manuals = Manuais.objects.get(id=id)
    return render(request, 'manual.html', {'manuals':manuals})
