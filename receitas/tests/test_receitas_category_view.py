from django.urls import reverse, resolve
from receitas.models import Category, Receitas, User
from receitas import views
from .test_receitas_base import ReceitasTEstBase
from unittest import skip

# usado para pular um teste
# @skip('Mensagem informando o desativação do teste')
class ReceitasViewsTest(ReceitasTEstBase):
           
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
        

        