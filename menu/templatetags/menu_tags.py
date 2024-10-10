from django import template
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe
from menu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_item = get_object_or_404(MenuItem, name=menu_name)
    request_url = context['request'].path

    def find_all_parents(item):
        if item.parent:
            return [item.parent] + find_all_parents(item.parent)
        return []

    parents = find_all_parents(menu_item)

    def render(parents, item, url):
        html = '<ul>'
        if parents:
            curr_parent = parents.pop()
            html += '<li>'
            if curr_parent.get_url():
                css_class = 'active' if curr_parent.get_url() == url else ''
                html += (f'<a class="{css_class}" '
                         f'href="/{curr_parent.get_url()}">{curr_parent.name}')
            else:
                html += f'{curr_parent.name}'
            html += render(parents, item, url)
            html += '</li>'
        else:
            html += '<li>'
            if item.get_url():
                css_class = 'active' if item.get_url() == url else ''
                html += (f'<a class="{css_class}" '
                         f'href="/{item.get_url()}">{item.name}')
            else:
                html += f'{item.name}'
            if item.children.exists():
                html += '<ul>'
                for child in item.children.all():
                    html += '<li>'
                    if child.get_url():
                        css_class = 'active' if child.get_url() == url else ''
                        html += (f'<a class="{css_class}" '
                                 f'href="/{child.get_url()}">{child.name}')
                    else:
                        html += f'{child.name}'
                    html += '</li>'
                html += '</ul>'
            html += '</li>'
        html += '</ul>'
        return html

    return mark_safe(render(parents, menu_item, request_url))
