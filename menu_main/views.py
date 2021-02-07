from django.shortcuts import render
from main.models import MenuItem

# Create your views here.
def menuItem_info(request, pk):
    menu_item = MenuItem.objects.get(pk=pk)
    return render(request, 'menu_item.html', context={
        'menu_item': menu_item,
    })