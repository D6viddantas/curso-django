from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(requests):
    return render(requests,template_name='recipes/home.html',context={'name':'David Dantas'})
def sobre(requests):
    return HttpResponse('Sobre')

def contato(requests):
    return render(requests,template_name='base.html')