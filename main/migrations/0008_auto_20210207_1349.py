# Generated by Django 3.1.5 on 2021-02-07 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_usersmessages_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmessages',
            name='message',
            field=models.CharField(max_length=300),
        ),
    ]
