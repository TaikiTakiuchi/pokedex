from django.urls import path
from .views import homepage,searchpage,resultpage
from django.views.generic import RedirectView # インポート
from .views import search_func
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('home/',homepage.as_view(),name='home'),
    path('', homepage.as_view(),name='home'),
    #path('pokedexsearch/',searchpage.as_view(),name='search'),
    path('pokedexresult/',resultpage.as_view(),name='result'),
    path('pokedexsearch/', search_func,name='search')
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
