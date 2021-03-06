from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *

def menu_list(request):
    """ Grab all menu objects, filter them out by expiration date, return """
    all_menus = Menu.objects.all().prefetch_related('items')
    menus = all_menus.filter(
        expiration_date__gte=timezone.now()
    ).order_by('expiration_date')
    return render(request, 'menu/list_all_current_menus.html', {'menus': menus})

def menu_detail(request, pk):
    """ Pull information regarding a specific menu """
    menu = Menu.objects.get(pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})

def item_detail(request, pk):
    """ Pull information regarding a specific item """
    try: 
        item = Item.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'menu/detail_item.html', {'item': item})

def create_new_menu(request):
    """ Create a new menu object """
    if request.method == "POST":
        form = MenuForm(request.POST)
        # Check for validation
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            form.save_m2m()
            return redirect('menu_detail', pk=menu.pk)
    else:
        form = MenuForm()
    return render(request, 'menu/menu_new.html', {'form': form})



def edit_menu(request, pk):
    """ Edit a menu object """
    menu = get_object_or_404(Menu, pk=pk)
    form = MenuForm(instance=menu)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        #Check for validation
        if form.is_valid():
            menu = form.save(commit=False)
            menu.created_date = timezone.now()
            menu.save()
            form.save_m2m()
            return redirect('menu_list')
    return render(request, 'menu/change_menu.html', {
        'form': form
        })
