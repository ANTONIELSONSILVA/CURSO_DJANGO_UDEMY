from django.shortcuts import render, get_list_or_404, get_object_or_404

from receitas.utils.receitas.factory import make_receitas
from receitas.models import Receitas
from django.http import HttpResponse,HttpRequest
from django.http import Http404

def home(resquest):
    
    # Objeto herdado em Receitas
    #receitas = Receitas.objects.all().order_by('-id')
    
    # filtra somente pela publicadas
    receitas = Receitas.objects.filter(
        is_published=True
    ).order_by('-id')
    
    #return HttpResponse('<h1>HOME </h1>')
    return render(resquest, 'receitas/pages/home.html', context={
        #'receitasGerada': [make_receitas() for _ in range(6)],
        'receitasGerada': receitas,
    })


def category(request, category_id):
    # Objeto herdado em Receitas
    # Usar category__id dentro de filter para acessar o id de category dentro de models
    #receitas = Receitas.objects.filter(
    #    category__id=category_id,
    #    is_published=True
    #).order_by('-id')  # id decrescente
    
    
    #if not receitas:
        #return HttpResponse(content='Not Found', status='404')
        # ou um ou outro
    #    raise Http404('Not found')
    
    
    
    
    # Passar o model e os filtros
    receitas = get_list_or_404(
        #passando a queryset
        Receitas.objects.filter(
        category__id=category_id,
        is_published=True
        ).order_by('-id')
    )
    
    # Obtendo o primeiro objeto do queryset
    #primeira_receita = receitas.first()
    primeira_receita = receitas[0]
    categoria_nome = primeira_receita.category.name if primeira_receita else 'Categoria Desconhecida'
    
    
    return render(request, 'receitas/pages/category.html', context={
        # Variáveis de contexto que podem ser chamadas dentro do HTML
        'receitasGerada': receitas,
        
        # f de tipo String
        'title': f'{categoria_nome} - Category | '
    })

    
    
    

# viewer de quando clica na receita
def receitas(request, id):
    #return HttpResponse('<h1>HOME </h1>')
    
    # usando objects para informar páginas não encontradas
    receitaDetalhes = Receitas.objects.filter(
        pk=id,
        is_published=True,
    ).order_by('-id').first()
    
    return render(request, 'receitas/pages/receitas-detail.html', context={
        'receitaGerada': receitaDetalhes,
        'is_detail_page': True,
    })