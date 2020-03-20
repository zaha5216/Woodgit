from django.urls import path

from .views import index
from .views import doska_page
from .views import brus_page
from .views import brusok_page
from .views import vagonka_page
from .views import imitacia_page
from .views import terasnaya_page
from .views import shpuntovanaya_page
from .views import by_rubric
from .views import detail
from .views import barlinek_page
from .views import askania_page
from .views import almond_page
from .views import askania_grande
from .views import calvados_grande
from .views import caramel_grande
from .views import ivory_grande
from .views import porto_grande
from .views import white_truffle_grande
from .views import yasen_coffe_grande
from .views import hazelnut_grande
from .views import lemon_sorbet_grande
from .views import barlinek2
from .views import almond_piccolo
from .views import apricot_sorbet_piccolo
from .views import brown_shugar_piccolo
from .views import coconut_piccolo
from .views import espresso_piccolo
from .views import nugat_piccolo
from .views import peach_piccolo
from .views import snowflakes_piccolo
from .views import caldera_piccolo




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
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>/', barlinek_page, name='barlinek'),
    path('<str:page>/', askania_page, name='Askania-piccolo'),
    path('<str:page>/', almond_page, name='Almond_grande'),
    path('<str:page>/', askania_grande, name='Askania_grande'),
    path('<str:page>/', calvados_grande, name='Calvados_grande'),
    path('<str:page>/', caramel_grande, name='Caramel_grande'),
    path('<str:page>/', ivory_grande, name='Ivory_grande'),
    path('<str:page>/', porto_grande, name='Porto_grande'),
    path('<str:page>/', white_truffle_grande, name='White_truffle_grande'),
    path('<str:page>/', yasen_coffe_grande, name='Yasen_coffe_grande'),
    path('<str:page>/', hazelnut_grande, name='Hazelnut_grande'),
    path('<str:page>/', lemon_sorbet_grande, name='Lemon_sorbet_grande'),
    path('<str:page>/', barlinek2, name='Barlinek_piccolo'),
    path('<str:page>/', almond_piccolo, name='Almond_piccolo'),
    path('<str:page>/', apricot_sorbet_piccolo, name='Apricot_sorbet_piccolo'),
    path('<str:page>/', brown_shugar_piccolo, name='Brown_shugar_piccolo'),
    path('<str:page>/', coconut_piccolo, name='Coconut_piccolo'),
    path('<str:page>/', espresso_piccolo, name='Espresso_piccolo'),
    path('<str:page>/', nugat_piccolo, name='Nugat_piccolo'),
    path('<str:page>/', peach_piccolo, name='Peach_piccolo'),
    path('<str:page>/', snowflakes_piccolo, name='Snowflakes_piccolo'),
    path('<str:page>/', caldera_piccolo, name='Caldera_piccolo'),


]
