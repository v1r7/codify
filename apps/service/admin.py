from django.contrib import admin
from .models import Product, Service, SubmitApplication, Rate, Contact, News
from django.utils.safestring import mark_safe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "link", "service_id", "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

    get_image.short_description = "Изображение"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

    get_image.short_description = "Изображение"


@admin.register(SubmitApplication)
class SubmitApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "created_at")
    # list_filter = ("created_at")


@admin.register(Rate)
class RatesAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price",)


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("name", "mail", "phone_number", "whatsapp_number", "instagram", "twitter", "facebook")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at", "get_image")
    list_filter = ("title", "created_at")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

    get_image.short_description = "Изображение"
