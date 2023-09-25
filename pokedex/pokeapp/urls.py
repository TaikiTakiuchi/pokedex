from django.urls import path
from .views import homepage,summary_page,manufacturinghistory_page,updateinfo_page
from django.views.generic import RedirectView # インポート
from .views import search_func
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('home/',homepage.as_view(),name='home'),
    path('', homepage.as_view(),name='home'),
    path('summary/',summary_page.as_view(),name='summary'),
    path('history/',manufacturinghistory_page.as_view(),name='history'),
    path('updateinfo/',updateinfo_page.as_view(),name='updateinfo'),
    path('pokedexsearch/', search_func,name='search')
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
