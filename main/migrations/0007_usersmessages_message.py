# Generated by Django 3.1.5 on 2021-02-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_usersmessages'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersmessages',
            name='message',
            field=models.TextField(default='Nothing'),
        ),
    ]
