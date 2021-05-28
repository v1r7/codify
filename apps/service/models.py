from django.db import models
from .upload import upload_instance


class Service(models.Model):
    """
    Услуги
    """
    name = models.CharField(max_length=255,
                            null=True,
                            verbose_name='Название', )
    title = models.TextField(max_length=255,
                             verbose_name='Заголовок',
                             blank=True,
                             null=True
                             )
    image = models.ImageField(upload_to=upload_instance,
                              null=True,
                              blank=True,
                              verbose_name='Картинки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'


class Product(models.Model):
    """
    Последние работы
    """
    title = models.CharField(verbose_name='Название',
                             max_length=100)
    description = models.TextField(verbose_name='Описание',
                                   null=True)
    image = models.ImageField(upload_to=upload_instance,
                              blank=True,
                              verbose_name='Картинки', )
    link = models.CharField(verbose_name='Ссылка',
                            max_length=100)
    service_id = models.ForeignKey(Service,
                                   on_delete=models.SET_NULL,
                                   related_name='products',
                                   null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Наш продукт'
        verbose_name_plural = 'Наши продукты'


class SubmitApplication(models.Model):
    """
    Заявки
    """
    name = models.CharField(verbose_name='Имя',
                            max_length=100
                            )
    surname = models.CharField(verbose_name='Фамилия',
                               max_length=100
                               )
    email = models.EmailField(max_length=255,
                              verbose_name='Почта',
                              null=False,
                              blank=False,
                              unique=True)
    comment = models.CharField(verbose_name='Комментарий',
                               max_length=250
                               )
    phone_number = models.CharField(null=False,
                                    max_length=100,
                                    verbose_name='Номер телефона',
                                    blank=False,
                                    unique=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания',
                                      blank=True
                                      )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Rate(models.Model):
    """
    Тарифы
    """
    name = models.CharField(verbose_name='Название',
                            max_length=100, )
    description = models.TextField(verbose_name='Описание',
                                   null=True, )

    price = models.SmallIntegerField(verbose_name='Тарифы')

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.name


class Contact(models.Model):
    """
    Контакты Codify
    """
    name = models.CharField(verbose_name='Название',
                            max_length=100
                            )
    mail = models.EmailField(max_length=255,
                             verbose_name='Мейл',
                             null=True,
                             blank=True,
                             unique=True)
    phone_number = models.CharField(null=True,
                                    max_length=100,
                                    verbose_name='Номер телефона',
                                    blank=True,
                                    unique=True)
    whatsapp_number = models.CharField(null=True,
                                       max_length=100,
                                       verbose_name='Whatsapp',
                                       blank=True,
                                       unique=True)
    instagram = models.CharField(null=True,
                                 max_length=100,
                                 verbose_name='instagram',
                                 blank=True,
                                 unique=True)
    twitter = models.EmailField(null=True,
                                verbose_name='twitter',
                                blank=True,
                                unique=True)
    facebook = models.EmailField(null=True,
                                 verbose_name='facebook',
                                 blank=True,
                                 unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class News(models.Model):
    """
    Новостная лента
    """
    title = models.CharField(verbose_name='Название',
                             max_length=100, )
    author = models.CharField(verbose_name='Автор',
                              max_length=100, )
    description = models.TextField(verbose_name='Описание',
                                   max_length=100, )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания'
                                      )
    image = models.ImageField(upload_to=upload_instance,
                              blank=True,
                              verbose_name='Картинки',
                              null=True,
                              )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
