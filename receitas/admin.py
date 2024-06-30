from django.contrib import admin

from .models import Category, Receitas
# Register your models here.



# classe vazia
class CategoryAdmin(admin.ModelAdmin):
    ...
    
@admin.register(Receitas)
class ReceitasAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)