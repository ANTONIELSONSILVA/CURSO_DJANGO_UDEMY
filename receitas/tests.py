from django.test import TestCase
from django import reverse


# Create your tests here.


# os teste devem ser classes que herdam de TestCase

# todo método que começa com test_ é considerado teste pelo pyteste ou Unitteste

class ReceitasURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        print('teste Receitas')
        assert 1 == 1, 'Um é igual a um'
        
    # colocar nomes bem explicativos
    def test_receitas_home_url_is_correct(self):
        home_url = reverse('receitas:home')
        self.assertEqual(home_url, '/')