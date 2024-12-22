from django.shortcuts import render,get_list_or_404,get_object_or_404
from utils.recipe.functio import make_recipe
from recipes.models import Recipe

def home(requests):
    recipes = Recipe.objects.filter(is_published=True)
    return render(request=requests, template_name='recipes/pages/home.html', context={'recipes':recipes})
def category(requests,category_id):
   # recipes = Recipe.objects.filter(category__id = category_id,is_published=True)
    recipes = get_list_or_404( Recipe.objects.filter(category__id = category_id,is_published=True).order_by('-id'))
    return render(request=requests, template_name='recipes/pages/category.html', context={'recipes':recipes,'title':f'{ recipes[0].category.name} - Category|'})

def recipe(requests,id):
    #recipe = Recipe.objects.filter(id=id).first()
    recipe = get_object_or_404(Recipe,pk=id,is_published=True)
    return render(requests,template_name='recipes/pages/recipe-view.html',context={'recipe':recipe,'is_detail_page':True})