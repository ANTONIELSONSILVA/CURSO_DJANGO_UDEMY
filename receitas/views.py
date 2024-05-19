from django.shortcuts import render
from receitas.utils.receitas.factory import make_receitas

def home(resquest):
    #return HttpResponse('<h1>HOME </h1>')
    return render(resquest, 'receitas/pages/home.html', context={
        'receitasGerada': [make_receitas() for _ in range(6)],
    })


def receitas(resquest, id):
    #return HttpResponse('<h1>HOME </h1>')
    return render(resquest, 'receitas/pages/receitas-detail.html', context={
        'receitaGerada': make_receitas(),
        'is_detail_page': True,
    })