# Generated by Django 4.2.3 on 2023-07-26 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_streaming'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stream',
            options={'ordering': ['-date']},
        ),
    ]
