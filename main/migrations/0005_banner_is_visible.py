# Generated by Django 3.1.5 on 2021-01-31 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
