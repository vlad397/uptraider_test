from django.shortcuts import render
from .models import Menu
from django.template import RequestContext


def show_menu(request, pk):
    current_menu = Menu.objects.get(id=pk)
    root_menu_id = current_menu.get_root().id
    return render(request, template_name="menu.html", context={
                              'nodes':Menu.objects.all(),
                              'current_menu':current_menu,
                              'root_menu_id':root_menu_id
                          })