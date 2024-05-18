from django.shortcuts import render

def home(resquest):
    #return HttpResponse('<h1>HOME </h1>')
    return render(resquest, 'receitas/pages/home.html', context={
        'name': 'Teste',
    })


def receitas(resquest, id):
    #return HttpResponse('<h1>HOME </h1>')
    return render(resquest, 'receitas/pages/receitas-detail.html', context={
        'name': 'Teste',
    })