# Generated by Django 3.2.2 on 2021-05-28 11:44

import apps.service.upload
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
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
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('description', models.TextField(max_length=100, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.service.upload.upload_instance, verbose_name='Картинки')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.SmallIntegerField(verbose_name='Тарифы')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title', models.TextField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.service.upload.upload_instance, verbose_name='Картинки')),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='SubmitApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Почта')),
                ('comment', models.CharField(max_length=250, verbose_name='Комментарий')),
                ('phone_number', models.CharField(max_length=100, unique=True, verbose_name='Номер телефона')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to=apps.service.upload.upload_instance, verbose_name='Картинки')),
                ('link', models.CharField(max_length=100, verbose_name='Ссылка')),
                ('service_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='service.service')),
            ],
            options={
                'verbose_name': 'Наш продукт',
                'verbose_name_plural': 'Наши продукты',
            },
        ),
    ]
