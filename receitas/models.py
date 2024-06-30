from django.db import models
# Elemento User presente na base de dados
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

# os atributos vão virar colunas
class Receitas(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    
    # auto_now_add chamado na criação na depois
    created_at = models.DateTimeField(auto_now_add=True)
    
    # chamado em alterações
    updated_at = models.DateTimeField(auto_now=True) 
    
    is_published =  models.BooleanField(default=False)
    
    # blank para permitir que não seja obrigatório a importação de uma imagem
    cover = models.ImageField(upload_to='receitas/covers/%Y/%m/%d/', blank=True, default='')
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    
    
    def __str__(self):
        return self.title