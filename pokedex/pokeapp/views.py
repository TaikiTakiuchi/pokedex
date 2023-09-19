from typing import Any
from django.shortcuts import render
from .models import PokeModel
# Create your views here.
from django.views.generic import TemplateView
from .pokeAPI import get_pokeinfo

class homepage(TemplateView):
    template_name='home/home.html'
    model=PokeModel
 
class searchpage(TemplateView):
    template_name='pokedex_search/pokedex.html'
    model=PokeModel
        

class resultpage(TemplateView):
    template_name='result/result.html'
    model=PokeModel


def search_func(request):
    if request.method=="POST":
        dex_num=request.POST['dex_num']
        pokeinfo=get_pokeinfo(dex_num)
        return render(request,'result/result.html',pokeinfo)
    return render(request,'pokedex_search/pokedex.html',{})




    

