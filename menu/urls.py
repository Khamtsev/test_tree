from django.urls import path
from menu.views import IndexView, draw_menu

app_name = 'menu'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:menu_name>/', draw_menu, name='draw_menu'),
]
