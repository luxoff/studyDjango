from django.contrib import admin
from .models import Category, MenuItem, Event, Banner, UsersMessages

# Register your models here.
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Event)
admin.site.register(Banner)
admin.site.register(UsersMessages)
