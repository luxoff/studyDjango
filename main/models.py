import os
from uuid import uuid4
from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=40)
    category_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} : {self.category_order}'


class MenuItem(models.Model):

    def get_file_name_menuItem(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join('images/menu_items/', filename)

    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_file_name_menuItem)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Event(models.Model):
    def get_file_name_events(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join('images/events/', filename)

    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_file_name_events)
    description = models.TextField(null=True)
    event_date = models.DateTimeField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.title} @ {self.event_date}'


class Banner(models.Model):
    def get_file_name_banners(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join('images/banners/', filename)

    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_file_name_banners)
    text = models.TextField(null=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class UsersMessages(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    message = models.CharField(max_length=300)

    is_processed = models.BooleanField(default=False)
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name}, {self.user_email} написав: {self.message[:15]}...'
