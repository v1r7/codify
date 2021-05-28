from django.contrib import admin
from .models import *
from . import models
from django.utils.safestring import mark_safe

@admin.register(Services)
class ProductsAdmin(admin.ModelAdmin):
	list_display = ("name", "title", "parent", "get_image")
	list_filter = ("name",)
	search_fields = ("parent__name", "title__name")

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

	get_image.short_description = "Изображение"

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
	list_display = ("title", "description", "get_image")

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

	get_image.short_description = "Изображение"

@admin.register(SubmitApplication)
class SubmitApplicationAdmin(admin.ModelAdmin):
	list_display = ("name", "mail", "phone_number", "created_at")
	list_filter = ("created_at")

@admin.register(Rates)
class RatesAdmin(admin.ModelAdmin):
	list_display = ("name", "description", "price",)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
	list_display = ("name", "mail", "phone_number", "whatsapp_number", "instagram", "twitter", "facebook")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	list_display = ("title", "description", "created_at", "get_image")
	list_filter = ("title", "created_at")

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

	get_image.short_description = "Изображение"

