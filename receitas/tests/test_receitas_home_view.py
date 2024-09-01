from django.urls import reverse, resolve
from receitas.models import Category, Receitas, User
from receitas import views
from .test_receitas_base import ReceitasTEstBase
from unittest import skip
from unittest.mock import patch

# usado para pular um teste
# @skip('Mensagem informando o desativação do teste')
class ReceitasHomeViewTest(ReceitasTEstBase):
           
    def test_receita_home_views_function_is_correct(self):
        view = resolve('/')
        self.assertTrue(True)
        
    # verifica se o view esta retornando código 200
    def  test_receita_home_view_returns_status_code_200_OK(self):
        #cliente disponibilizado pelo Django
        response = self.client.get(reverse('receitas:home'))
        self.assertEqual(response.status_code, 200)


    # verifica se a view esta retornando o template correto
    def  test_receita_view_loads_correct_template(self):
        #cliente disponibilizado pelo Django
        response = self.client.get(reverse('receitas:home'))
        self.assertTemplateUsed(response, 'receitas/pages/home.html')
    
    
    # @skip('WIP = Work in progress')
    # Verifica se esta retornando um valor do html
    skip('WIP = Work in progress')
    def test_receitas_home_shows_no_receitas_found_if_on_receitas(self):
        
        # todos os teste são isolados. posso deletar a receita gerada para esse teste
        # sem afetar os outros teste
        
        #self.make_receita()
        Receitas.objects.get(pk=1).delete()
        
        response = self.client.get(reverse('receitas:home'))
        self.assertIn(
            '<h1>Receitas não encontradas</h1>',
            response.content.decode('utf-8')
        ) 
        
        # Usado para fazer o teste falha e colocar uma mensagem 
        # self.fail('mensagem de aviso')
    
    # verifica se o view esta retornando código 200
    def  test_receita_category_view_returns_status_code_404_NOT_FOUND(self):
        #self.make_receita()
               
        #cliente disponibilizado pelo Django
        response = self.client.get(
            reverse('receitas:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)
        
        
    def test_receita_home_loads_receitas(self):
        
        response = self.client.get(reverse('receitas:home'))
        response_receitas = response.context['receitasGerada']
        
        #verificando se tem uma receita gravada
        self.assertEqual(len(response_receitas), 1)
        
        self.assertEqual(response_receitas.first().title, 'Receita Título')
        
        
        
    # para verificar o conteúdo
    skip('WIP = Work in progress')
    def test_receita_home_loads_receitas_content(self):
        
        self.make_receita()
        
        response = self.client.get(reverse('receitas:home'))
        content = response.content.decode('utf-8')
        response_context_receita = response.context[Receitas]
        
        #mais de um conteúdo
        self.assertIn('Receita Título', content)
        self.assertIn('10 Minutos', content)
        
        
        # verificando se tem uma receita cadastrada
        self.assertEqual(len(response_context_receita), 1)
        
        
    skip('WIP = Work in progress')
    def test_receita_home_template_dont_load_receitas_not_published(self):
        
        self.make_receita(is_published=False)
        
        response = self.client.get(reverse('receitas:home'))
        
        self.assertIn(
            '<h1>Receitas não encontradas</h1>',
            response.content.decode('utf-8')
        ) 
        
        
    #skip('WIP = Work in progress')
    # verificar aula 124
    def test_receita_home_is_pagination(self):
        
        # trazendo o valor de global de receitas por página
        import receitas
        
        num_receitas = receitas.views.receitas_pagina
        
        
        for i  in range(16):
            kwargs = {'slug': f'r{i}', 'author_data':{'username': f'U{i}'}, }
            self.make_receita(**kwargs)
        
        response = self.client.get(reverse('receitas:home'))
        receitas = response.context['receitasGerada']
        paginator = receitas.paginator
        
        # verificar quais são os métodos de paginator
        self.assertEqual(paginator.num_pages,9)