from faker import Faker
import random

faker = Faker('pt_BR')
def rand_ratio():
    return random.randint(840,900),random.randint(473,574)
def make_recipe():
    return {
        'id':faker.random_number(digits=2,fix_len=True),
        'title':faker.sentence(nb_words=5),
        'date':faker.date_time(),
        'first_name':faker.first_name(),
        'last_name':faker.last_name(),
        'description':faker.sentence(nb_words=30),
        'serving_util':'Porção',
        'category':faker.word(),
        'preparation_time':f'{random.randint(10,200)} Minutos',
        'preparation_serving':f'{random.randint(1,20)} Porções',
        'preparation_step':faker.text(3000),
        'cover':{
            'url':'https://loremflickr.com/%s/%s/food,cook' % rand_ratio()
        }
    }
