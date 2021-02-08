from django.shortcuts import render, redirect
from main.models import MenuItem
from .forms import AddCategoryForm

# Create your views here.
def menuItem_info(request, pk):
    menu_item = MenuItem.objects.get(pk=pk)
    return render(request, 'menu_item.html', context={
        'menu_item': menu_item,
    })

def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/#')

    add_category_form = AddCategoryForm()
    return render(request, 'add_category.html', {
        'form': add_category_form,
    })