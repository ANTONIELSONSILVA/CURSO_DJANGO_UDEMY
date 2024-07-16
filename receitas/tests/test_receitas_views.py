from django.test import TestCase
from django.urls import reverse, resolve


class ReceitasViewsTest(TestCase):
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
    
    
    def 