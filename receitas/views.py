from django.shortcuts import render, get_list_or_404, get_object_or_404
from receitas.utils.receitas.factory import make_receitas
from receitas.models import Receitas
from django.http import HttpResponse,HttpRequest
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from .tests.utils.pagination import make_pagination_range


# recebe uma view devolve uma responce 
def home(resquest):
    
    # Objeto herdado em Receitas
    #receitas = Receitas.objects.all().order_by('-id')
    
    # filtra somente pela publicadas
    receitas = Receitas.objects.filter(
        is_published=True
    ).order_by('-id')
    
    
    # divide os dados vindo do model em 3 e podemos acessar no page_obj
    # ao invés de acessarmos os dados do model acessamos a paginação
    # o número é o número de receitas na base
    try:
        current_page = int(resquest.GET.get('page', 1))
    except ValueError:
        current_page = 1
        
    paginator = Paginator(receitas, 2)
    page_obj = paginator.get_page(current_page)
    
    
    
    
    pagination_range = make_pagination_range(
        paginator.page_range,
        4,
        current_page,
    )
    
    #return HttpResponse('<h1>HOME </h1>')
    return render(resquest, 'receitas/pages/home.html', context={
        #'receitasGerada': [make_receitas() for _ in range(6)],
        'receitasGerada': page_obj,
        'pagination_range' : pagination_range,
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
    
    
def search(request):
    
    # se não receber q o padrã oé None, exitando pesquisa somente com espaço
    #search_term = request.GET.get('q', None)
    # remove espaços laterais
    search_term = request.GET.get('q', '').strip()
    
    if not search_term:
        raise Http404()
    
    
    #__contains para buscar nomes parecidos. (__icontains) maiusculas e minusculas 
    receitasPesquisa = Receitas.objects.filter(
        
        # | = or 
        # __
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),    
        ),
        is_published=True
    
    ).order_by('-id')
    
    # o return retorna variaveis para serem usadas nos templates
    return render(request, 'receitas/pages/search.html',{
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'receitasGerada': receitasPesquisa,
    })