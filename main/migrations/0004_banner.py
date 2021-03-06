# Generated by Django 3.1.5 on 2021-01-31 17:57

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to=main.models.Banner.get_file_name_banners)),
                ('text', models.TextField(null=True)),
            ],
        ),
    ]
