from django.shortcuts import render



def home(resquest):
    #return HttpResponse('<h1>HOME </h1>')
    return render(resquest, 'receitas/pages/home.html', context={
        'name': 'Teste',
    })
