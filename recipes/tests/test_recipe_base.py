from django.test import TestCase
from recipes.models import Category,Recipe,User


class RecipeTestBase(TestCase):
    def setUp(self) ->None:
       return super().setUp()
    def make_category(self,name='janta'):
       return Category.objects.create(name=name)
    def make_author(self,
                   username='mariajoana',
                   email='Maria@gmail.com',
                   password='1234maria',
                   first_name= 'Maria',
                   last_name='Joana',):
        return User.objects.create_user(
           username=username,
           email=email,
           password=password,
           first_name=first_name,
           last_name=last_name,
       )
    def make_recipe(self,
                    category_data = None,
                    author_data = None,
                    title ='Recipe title',
                    description = 'Recipe description',
                    slug = 'Recipe-title',
                    preparation_time = 10,
                    preparation_time_unit ='Minutos',
                    servings = 15,
                    servings_unit = 'Pessoas',
                    preparation_steps = 20,
                    preparation_steps_is_html = False,
                    is_published = True,
                    cover='teste.png'):
        if category_data is None:
            category_data = {}
        if author_data is None:
            author_data = {}
        return Recipe.objects.create(
                    category=self.make_category(**category_data),
                    author = self.make_author(**author_data),
                    title = title,
                    description = description,
                    slug = slug,
                    preparation_time = preparation_time,
                    preparation_time_unit = preparation_time_unit,
                    servings = servings,
                    servings_unit = servings_unit,
                    preparation_steps = preparation_steps,
                    preparation_steps_is_html = preparation_steps_is_html,
                    is_published = is_published,
                    cover=cover
        )
                    