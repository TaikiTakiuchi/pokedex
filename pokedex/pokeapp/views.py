from typing import Any
from django.shortcuts import render
from .models import PokeModel,UploadImage
# Create your views here.
from django.views.generic import TemplateView
from .pokeAPI import get_pokeinfo
from .recognition import recognition_poke
from . import forms

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

'''
class pokedex_serch(TemplateView):
    template_name='pokedex_search/pokedex.html'
    model=UploadImage
    def __init__(self):
        self.params = {
            "form":forms.UploadForm(),
            "pokeinfo":{}}  
    
'''
      
def test_index(request):
    params = {
        'upload_form': forms.UploadForm(),
        'url': '',
        'pred':None,
        'score':None,
        'pokeinfo':None,
        'id':None
        }
    
    if (request.method == 'POST'):
        form = forms.UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image = form.save()
            img_path=upload_image.image.url
            params['id']=upload_image.id
            pred,score=recognition_poke(img_path)
            pokeinfo=get_pokeinfo(str(pred))
            pokeinfo['score']=score
            pokeinfo['upload_form']=params['upload_form']
            pokeinfo['url']=img_path
            return render(request, 'result/result.html', pokeinfo)
        return render(request,'pokedex_search/pokedex.html', params)
    return render(request,'pokedex_search/pokedex.html', params)
    '''
    def search_func(self,request,*args, **kwargs):
        if request.method=="POST":
            print('called post')
            print(request.method)
            dex_num=request.POST['dex_num']
            pic=request.POST['input_pic']
            print(request.POST)
            try:
                dex_num=int(dex_num)
            except:
                return render(request,'pokedex_search/pokedex.html',{'error':"無効な入力です。1~151の図鑑番号を入力してください"}) #文字列が入力された
            
            if (dex_num>=1) and (dex_num<=151):#期待通りの数字
                if pic =='':
                    self.pokeinfo=get_pokeinfo(str(dex_num))
                    return render(request,'result/result.html',self.pokeinfo)
                else:
                    pred,score=recognition_poke()
                    self.pokeinfo=get_pokeinfo(str(pred))
                    return render(request,'result/result.html',self.pokeinfo)
            else:#範囲外の数字
                return render(request,'pokedex_search/pokedex.html',{'error':"1世代(図鑑番号1~151)の図鑑番号を入れてください"}) 
        return render(request,'pokedex_search/pokedex.html',self.pokeinfo)#このページが呼ばれたときに呼ばれる
    '''





    

