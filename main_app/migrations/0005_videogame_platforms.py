# Generated by Django 4.2.3 on 2023-07-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogame',
            name='platforms',
            field=models.ManyToManyField(to='main_app.platform'),
        ),
    ]