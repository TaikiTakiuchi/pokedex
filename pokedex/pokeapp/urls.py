from django.urls import path
from .views import homepage,summary_page,manufacturinghistory_page,updateinfo_page,test_index
from django.views.generic import RedirectView # インポート
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('home/',homepage.as_view(),name='home'),
    path('', homepage.as_view(),name='home'),
    path('summary/',summary_page.as_view(),name='summary'),
    path('history/',manufacturinghistory_page.as_view(),name='history'),
    path('updateinfo/',updateinfo_page.as_view(),name='updateinfo'),
    path('pokedexsearch/',test_index,name='search')
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

