# Generated by Django 3.0.1 on 2019-12-29 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_hero', models.CharField(max_length=250, verbose_name='Название')),
                ('services_hero', models.CharField(max_length=250, verbose_name='Название')),
                ('image_hero', models.ImageField(blank=True, default='', upload_to='mainpage/hero', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Главная',
                'verbose_name_plural': 'Главные',
            },
        ),
    ]