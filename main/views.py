from django.shortcuts import render

from .models import Category, MenuItem


def main(request):
    categories = Category.objects.filter(is_visible=True).order_by("category_order")
    page_title = "Restaurant — Index"
    for item in categories:
        item.items = MenuItem.objects.filter(category=item.pk)
    # В {} передаём переменные (контекст) в разметку
    return render(request, 'index.html', {'page_title': page_title, 'categories': categories})
