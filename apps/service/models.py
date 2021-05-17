from django.db import models
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from phonenumber_field.modelfields import PhoneNumberField


class Products(models.Model):
#Последние работы#
  title = models.CharField(verbose_name='Название',
                           max_length=100,
                           default="can be your product")
  # slug = models.SlugField(max_length=100)
  description = models.TextField(verbose_name='Описание',
                                 null=True,
                                 blank=True)

  image = models.ImageField(upload_to='products/',
                                 blank=True,
                                 verbose_name='Картинки',
                                 null=True,
                                 )

  def __str__(self):
      return self.title




  class Meta:
    verbose_name = 'Наш продукт'
    verbose_name_plural = 'Наши продукты'

# class Category(models.Model):
#   name = models.CharField(max_length=255)
#   category = models.CharField(max_length=255)
#
#   def __str__(self):
#     return self.name
#
#   class Meta:
#     verbose_name = 'Категория'
#     verbose_name_plural = 'Категории'

class Services(MPTTModel):
#Услуги#
  name = models.CharField(max_length=255,
                          null=True,
                          verbose_name='Название',
                          default="Введите название услуги",
                          )
  title = models.TextField(max_length=255,
                           verbose_name='Заголовок',
                           default='Введите заголовок',
                           blank=True,
                           null=True
                           )
  #category_id = models.CharField(max_length=255,
   #                             null=True
    #                            )
  parent = TreeForeignKey('self',
                          verbose_name='Под категория',
                          related_name="children",
                          on_delete=models.SET_NULL,
                          null=True,
                          blank=True)
  image = models.ImageField(upload_to='services/',
                            null=True,
                            blank=True,
                            verbose_name='Картинки')


  class MPTTMeta:
    order_insertion_by = ['title']

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Услуги'
    verbose_name_plural = 'Услуги'


##################################################################
            #**Таблицы без связей**#
############################################################



class submit_application(models.Model):
#Заявки#
  name = models.CharField(verbose_name='Имя',
                           max_length=100
                          )
  # slug = models.SlugField(max_length=100)
  mail = models.EmailField(max_length=255,
                           verbose_name='Мейл',
                           null=False,
                           blank=False,
                           unique=True)
  phone_number = PhoneNumberField(null=False,
                                  verbose_name='Номер телефона',
                                  blank=False,
                                  unique=True)

  def __str__(self):
      return self.name

  class Meta:
    verbose_name = 'Заявка'
    verbose_name_plural = 'Заявки'


class contacts(models.Model):
#Контакты Codify#
  name = models.CharField(verbose_name='Название',
                           max_length=100
                          )
  # slug = models.SlugField(max_length=100)
  mail = models.EmailField(max_length=255,
                           verbose_name='Мейл',
                           null=True,
                           blank=True,
                           unique=True)
  phone_number = PhoneNumberField(null=True,
                                  verbose_name='Номер телефона',
                                  blank=True,
                                  unique=True)
  whatsapp_number = PhoneNumberField(null=True,
                                     verbose_name='Whatsapp',
                                     blank=True,
                                     unique=True)
  instagram = PhoneNumberField(null=True,
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


class news(models.Model):
#Новостная лента#
  title = models.CharField(verbose_name='Название',
                           max_length=100,
                           default="может быть ваша новость")
  # slug = models.SlugField(max_length=100)
  description = models.TextField(verbose_name='Описание',)
  created_at = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата создания'
                                    )

  image= models.ImageField(blank=True,
                                 verbose_name='Картинки',
                                 null=True,
                                 )

  def __str__(self):
      return self.title

  class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'


class Picture(models.Model):
#Картинки#
  image = models.ImageField(upload_to='media/',
                                 verbose_name='Картинки',
                                 null=True,
                                 blank=True)


  # def image_tag(self):
  #   return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))
  #   image_tag.short_description = 'Image'


  # def image_img(self):
  #   if self.img_poster:
  #     from django.utils.safestring import mark_safe
  #     return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.img_poster.url))
  #   else:
  #     return '(Нет изображения)'
  #
  #
  # image_img.short_description = 'Картинка'
  # image_img.allow_tags = True

