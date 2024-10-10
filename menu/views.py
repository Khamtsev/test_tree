from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from menu.models import MenuItem


class IndexView(TemplateView):
    template_name = 'menu/index.html'


def draw_menu(request, menu_name):
    menu_item = get_object_or_404(MenuItem, name=menu_name)
    context = {
        'menu_item': menu_item,
    }
    return render(request, 'menu/menu.html', context)
