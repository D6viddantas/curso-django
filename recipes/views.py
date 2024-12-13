from django.shortcuts import render
from django.http import HttpResponse
from utils.recipe.functio import make_recipe

def home(requests):
    #return render(requests,template_name='recipes/pages/home.html',context={'recipes':[make_recipe() for _ in range(10)]})
    return render(request=requests, template_name='recipes/pages/home.html', context={'recipes': [make_recipe()
                                                                                                  for _ in range(10)]})

def recipe(requests,id):
    return render(requests,template_name='recipes/pages/recipe-view.html',context={'recipe':make_recipe(),'is_detail_page':True})