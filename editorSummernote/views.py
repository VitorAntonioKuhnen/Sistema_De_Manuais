from django.shortcuts import render
from .models import Manuais
from django.db.models import Q

def principal(request):
    manuais = Manuais.objects.all()

    busca = request.GET.get('search')
    if busca:
        print(busca)
        # manuais = Manuais.objects.filter(conteudo__icontains = busca) #O termo icontains serve para realizarmos uma busca com o que foi digitado
        manuais = Manuais.objects.filter(Q(titulo__icontains=busca) | Q(conteudo__icontains=busca)) #Verificar como utilizar o Q()
        print(manuais)    
    return render(request, 'manuais.html', {'manuais':manuais})


def manual(request, id):
    manuals = Manuais.objects.get(id=id)
    return render(request, 'manual.html', {'manuals':manuals})
