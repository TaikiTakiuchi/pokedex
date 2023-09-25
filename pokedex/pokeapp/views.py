from typing import Any
from django.shortcuts import render
from .models import PokeModel
# Create your views here.
from django.views.generic import TemplateView
from .pokeAPI import get_pokeinfo

class homepage(TemplateView):
    template_name='home/home.html'
    model=PokeModel
class summary_page(TemplateView):
    template_name='home/home_summary.html'
    model=PokeModel

class manufacturinghistory_page(TemplateView):
    template_name='home\home_manufacturinghistory.html'
    model=PokeModel

class updateinfo_page(TemplateView):
    template_name='home/home_updateinfo.html'
    model=PokeModel

def search_func(request):
    if request.method=="POST":
        dex_num=request.POST['dex_num']
        try:
            dex_num=int(dex_num)
        except:
            return render(request,'pokedex_search/pokedex.html',{'error':"無効な入力です。1~151の図鑑番号を入力してください"}) #文字列が入力された
        
        if (dex_num>=1) and (dex_num<=151):#期待通りの数字
            pokeinfo=get_pokeinfo(str(dex_num))
            return render(request,'result/result.html',pokeinfo)
        
        else:#範囲外の数字
            return render(request,'pokedex_search/pokedex.html',{'error':"1世代(図鑑番号1~151)の図鑑番号を入れてください"}) 
           
    return render(request,'pokedex_search/pokedex.html',{})#このページが呼ばれたときに呼ばれる




    

