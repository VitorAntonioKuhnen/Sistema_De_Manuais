from django.shortcuts import redirect, render
from .models import Manuais
from django.db.models import Q

def principal(request):
    manuais = Manuais.objects.all()

    busca = request.GET.get('search')
    if busca:
        print(busca)
        # manuais = Manuais.objects.filter(conteudo__icontains = busca) #O termo icontains serve para realizarmos uma busca com o que foi digitado
        manuais = Manuais.objects.filter(Q(titulo__icontains=busca) | Q(conteudo__icontains=busca) | Q(tag__icontains=busca)) #Verificar como utilizar o Q() 
        print(manuais)    
    return render(request, 'manuais.html', {'manuais':manuais})


def manual(request, id):
    manuals = Manuais.objects.get(id=id)
    return render(request, 'manual.html', {'manuals':manuals})

def btAdicionar(request):
    return render(request, 'cadManual.html')

def adicionar_manual(request):
    titulo = request.POST.get('titulo').strip()
    conteudo = request.POST.get('conteudo').strip()
    tag = request.POST.get('tag').strip()

    if titulo == "":
        print("Titulo não pode ser vazio!!")

    elif conteudo == "":
        print("Conteúdo do manual não pode ser Vazil!!")

    elif tag == "":
        print("É preciso informar uma TAG para salvar o Manual") 

    else:      
        Manuais.objects.create(titulo=titulo, conteudo=conteudo, tag=tag)
        return redirect('principal')
        
    return render(request, 'cadManual.html')   