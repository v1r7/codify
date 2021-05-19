# Generated by Django 3.2.2 on 2021-05-19 12:01

import apps.service.upload
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('mail', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Мейл')),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Номер телефона')),
                ('whatsapp_number', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Whatsapp')),
                ('instagram', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='instagram')),
                ('twitter', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='twitter')),
                ('facebook', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='facebook')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='может быть ваша новость', max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.service.upload.upload_instance, verbose_name='Картинки')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.service.upload.upload_instance, verbose_name='Картинки')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='can be your product', max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.service.upload.upload_instance, verbose_name='Картинки')),
            ],
            options={
                'verbose_name': 'Наш продукт',
                'verbose_name_plural': 'Наши продукты',
            },
        ),
        migrations.CreateModel(
            name='submit_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('mail', models.EmailField(max_length=255, unique=True, verbose_name='Мейл')),
                ('phone_number', models.CharField(max_length=100, unique=True, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Введите название услуги', max_length=255, null=True, verbose_name='Название')),
                ('title', models.TextField(blank=True, default='Введите заголовок', max_length=255, null=True, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.service.upload.upload_instance, verbose_name='Картинки')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='service.services', verbose_name='Под категория')),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
