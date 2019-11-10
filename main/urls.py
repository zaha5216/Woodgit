from django.urls import path

from .views import index
from .views import doska_page
from .views import brus_page
from .views import brusok_page
from .views import vagonka_page
from .views import imitacia_page
from .views import terasnaya_page
from .views import shpuntovanaya_page





app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('<str:page>/', doska_page, name='doska'),
    path('<str:page>/', brus_page, name='brus'),
    path('<str:page>/', brusok_page, name='brusok'),
    path('<str:page>/', vagonka_page, name='vagonka'),
    path('<str:page>/', imitacia_page, name='imitacia_brusa'),
    path('<str:page>/', terasnaya_page, name='terasnaya_doska'),
    path('<str:page>/', shpuntovanaya_page, name='shpuntovanaya_doska'),

]
