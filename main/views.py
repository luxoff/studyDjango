from datetime import *
from django.shortcuts import render, redirect
from .models import Category, MenuItem, Event, Banner
from .forms import UserMessageForm


def main(request):
    page_title = "Restaurant — Index"

    special_categories = Category.objects.filter(is_visible=True).filter(is_special=True).order_by("category_order")
    for sp_cat in special_categories:
        sp_cat.items = MenuItem.objects.filter(category=sp_cat.pk)

    categories = Category.objects.filter(is_visible=True).filter(is_special=False).order_by("category_order")
    for item in categories:
        item.items = MenuItem.objects.filter(category=item.pk)

    events = Event.objects.filter(event_date__gte=datetime.now()).order_by("event_date")

    banners = Banner.objects.filter(is_visible=True)

    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/#')

    users_messages_form = UserMessageForm()
    # В {} передаём переменные (контекст) в разметку
    return render(request, 'index.html', {'page_title': page_title,
                                          'categories': categories,
                                          'special_categories': special_categories,
                                          'events': events,
                                          'banners': banners,
                                          'form': users_messages_form,
                                          })
