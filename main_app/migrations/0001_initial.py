# Generated by Django 4.2.3 on 2023-07-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('release_year', models.IntegerField()),
            ],
        ),
    ]
