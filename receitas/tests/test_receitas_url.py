from django.test import TestCase
from django.urls import reverse, resolve

class ReceitasURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        print('teste Receitas')
        assert 1 == 1, 'Um é igual a um'
        
        
    # colocar nomes bem explicativos
    def test_receitas_home_url_is_correct(self):
        home_url = reverse('receitas:home')
        self.assertEqual(home_url, '/')
        
        
    def test_receitas_category_url_is_correct(self):
        url = reverse('receitas:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/receitas/category/1/')
        
        
    def test_receitas_details_url_is_correct(self):
        url = reverse('receitas:receita', kwargs={'id': 1})
        self.assertEqual(url, '/receitas/1/')