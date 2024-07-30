from django.urls import reverse, resolve
from receitas.models import Category, Receitas, User
from receitas import views
from .test_receitas_base import ReceitasTEstBase
from unittest import skip

# usado para pular um teste
# @skip('Mensagem informando o desativação do teste')
class ReceitasViewsTest(ReceitasTEstBase):
    
    def test_receitas_search_can_find_receita_by_title(self):
        title1 = 'receita um'
        title2 = 'receita dois'
        
        receita1 = self.make_receita(
            slug='one', title=title1, author_data={'username': 'one'}
        )
        
        receita2 = self.make_receita(
            slug='two', title=title2, author_data={'username': 'two'}
        )
        
        search_url = reverse('receitas:search')
        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        response_both = self.client.get(f'{search_url}?q=receita')
        
        self.assertIn(receita1, response1.context['receitasGerada'])
        self.assertNotIn(receita2, response1.context['receitasGerada'])
        
        self.assertIn(receita2, response1.context['receitasGerada'])
        self.assertNotIn(receita1, response2.context['receitasGerada'])
        
        self.assertIn(receita1, response_both.context['receitasGerada'])
        self.assertIn(receita2, response_both.context['receitasGerada'])