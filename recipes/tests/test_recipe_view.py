from django.test import TestCase
from django.urls import reverse,resolve
from recipes import views
from recipes.models import Category,Recipe,User
from .test_recipe_base import RecipeTestBase
from unittest import skip
class RecipeViewsTest(RecipeTestBase):
   def test_recipe_home_view_function_is_correct(self):
       view = resolve(reverse('recipes:home'))
       self.assertIs(view.func,views.home)
       
   def test_recipe_category_view_function_is_correct(self):
       
       view = resolve(reverse('recipes:category',kwargs={'category_id':1}))
       self.assertIs(view.func,views.category)
       
   def test_recipe_home_template_loads_recipe(self):
       
       self.make_recipe(category_data= {'name':'Café da manhã'})
       
       response = self.client.get(reverse('recipes:home'))
       
       content = response.content.decode('utf-8')
       recipe_context = response.context['recipes']
       
       self.assertIn('Recipe title',content)
       self.assertIn('Café da manhã',content)
       self.assertEqual(len(recipe_context),1)
       
   def test_recipe_category_template_loads_recipe(self):
       
       needed_title = 'This is a category test'
       self.make_recipe(title=needed_title)
       
       response = self.client.get(reverse('recipes:category',args=(1,)))
       content = response.content.decode('utf-8')
       
       self.assertIn(needed_title,content)
       
   def test_recipe_home_template_dont_load_recipe_not_pubished(self):
       self.make_recipe(is_published=False)
       
       response = self.client.get(reverse('recipes:home'))
       
       content = response.content.decode('utf-8')
       
       self.assertIn('<h1>No recipe here :(</h1>',content)
       
   def teste_recipe_home_shows_no_recipes_found_if_no_recipe(self):
       
       response = self.client.get(reverse('recipes:home',))
       
       self.assertIn('<h1>No recipe here :(</h1>',response.content.decode('utf-8'))
       
   def test_recipe_detail_view_function_is_correct(self):
       
       view = resolve(reverse('recipes:recipe',kwargs={'id':1}))
       
       self.assertIs(view.func,views.recipe)
       
   def test_recipe_home_returns_status_code_200_OK(self):
       
       response = self.client.get(reverse('recipes:home'))
       
       self.assertEqual(response.status_code,200)
       
   def test_recipe_home_loads_correct_template(self):
       
       response = self.client.get(reverse('recipes:home'))
       
       self.assertTemplateUsed(response,'recipes/pages/home.html')
       
   def test_recipe_home_no_recipes_found_if_no_recipes(self):
       response = self.client.get(reverse('recipes:home'))
       
       self.assertIn(
           'No recipe here',
           response.content.decode('utf-8'))
       
   def test_recipe_category_view_returns_404_if_no_recipes_found(self):
       response = self.client.get(reverse('recipes:category',kwargs={'category_id':100}))
       
       self.assertEqual(response.status_code,404)
   def test_recipe_category_template_dont_load_recipe_not_pubished(self):
       recipe = self.make_recipe(is_published=False)
       
       response = self.client.get(reverse('recipes:category',kwargs={'category_id':recipe.category.id}))
       
       self.assertEqual(response.status_code,404)
       
   def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
       response = self.client.get(reverse('recipes:recipe',kwargs={'id':100}))
       
       self.assertEqual(response.status_code,404)
   def test_recipe_detail_template_dont_load_recipe_not_pubished(self):
       recipe = self.make_recipe(is_published=False)
       
       response = self.client.get(reverse(
           'recipes:recipe',
           kwargs={'id':recipe.id}
           ))
       
       self.assertEqual(response.status_code,404)
       
   def test_recipe_detail_pege_template_loads_correct_recipe(self):
       needed_title = 'This is a recipe detail test -It load one recipe'
       
       self.make_recipe(title=needed_title)
       
       response = self.client.get(reverse(
           'recipes:recipe',kwargs={
               'id':1
               }
           ))
       
       content = response.content.decode('utf-8')
       
       self.assertIn(needed_title,content)