from .test_recipe_base import RecipeTestBase,Recipe
from django.urls import reverse,resolve
from django.core.exceptions import ValidationError
from parameterized import parameterized

class RecipeModelsTest(RecipeTestBase):
    
    def setUp(self):
        
        self.recipe = self.make_recipe()
        return super().setUp()
    def make_recipe_no_default(self):
        recipe = Recipe(
            category=self.make_category(name='churrasco'),
            author =self.make_author(username='newuser'),
            title ='Recipe title',
            description = 'Recipe description',
            slug = 'Recipe-title',
            preparation_time = 10,
            preparation_time_unit ='Minutos',
            servings = 15,
            servings_unit = 'Pessoas',
            preparation_steps = 20,
        )
        recipe.full_clean()
        recipe.save()
        return recipe
    @parameterized.expand(
        [
            ('title',65),
            ('description',165),
            ('preparation_time_unit',65),
            ('servings_unit',65),
        ]
    )
    def test_recipe_fields_max_length(self,field,max_length):
        
        setattr(self.recipe,field,'a'*(max_length+1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_default()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='Recipe preparation_steps_is_html is not False',)

    def test_recipe_published_is_false_by_default(self):
        recipe = self.make_recipe_no_default()
        self.assertFalse(
            recipe.is_published,
            msg='Recipe published is not False',)
    def test_recipe_string_representation(self):
        needed = 'Testing Representation'
        self.recipe.title = needed
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe),
            needed,
            msg=f'Recipe string representation must be'
            f'"{needed}" but "{self.recipe.title}"')