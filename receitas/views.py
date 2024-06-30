from django.shortcuts import render
from receitas.utils.receitas.factory import make_receitas
from receitas.models import Receitas

def home(resquest):
    
    # Objeto herdado em Receitas
    receitas = Receitas.objects.all().order_by('-id')
    
    #return HttpResponse('<h1>HOME </h1>')
    return render(resquest, 'receitas/pages/home.html', context={
        #'receitasGerada': [make_receitas() for _ in range(6)],
        'receitasGerada': receitas,
    })


def category(resquest, category_id):
    
    # Objeto herdado em Receitas
    # usasse category__id dentgro de filter para acessa o id de category dentro de models
    receitas = Receitas.objects.filter(
        category__id=category_id
    ).order_by('-id') # id decresente
    
    #return HttpResponse('<h1>HOME </h1>')
    return render(resquest, 'receitas/pages/home.html', context={
        #'receitasGerada': [make_receitas() for _ in range(6)],
        'receitasGerada': receitas,
    })
    
    
    

def receitas(resquest, id):
    #return HttpResponse('<h1>HOME </h1>')
    return render(resquest, 'receitas/pages/receitas-detail.html', context={
        'receitaGerada': make_receitas(),
        'is_detail_page': True,
    })