from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Services, Picture
from . import models
from django.utils.safestring import mark_safe

@admin.register(Services)
class ProductsAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "parent", "get_image")
	list_filter = ("title",)
	search_fields = ("parent__name", "title__name")

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

	get_image.short_description = "Изображение"

	# list_display_links = ("name")
	# def get_search_results(self, request, queryset, search_term):
	# 	queryset, may_have_duplicates = super().get_search_results(
	# 		request, queryset, search_term,
	# 	)
	# 	try:
	# 		search_term_as_int = int(search_term)
	# 	except ValueError:
	# 		pass
	# 	else:
	# 		queryset |= self.model.objects.filter(id=search_term_as_int)
	# 	return queryset, may_have_duplicates


#admin.site.register(models.Services)
admin.site.register(models.Products)
#admin.site.register(models.Category)
admin.site.register(models.submit_application)
admin.site.register(models.contacts)
admin.site.register(models.news)
# admin.site.register(models.Picture)

# @admin.register(Picture)
# class PictureAdmin(admin.ModelAdmin):
# 	list_display = ['image',]
# 	fields = ['image_tag']
# 	readonly_fields = ['image_tag']


#
#
# @admin.register(Picture)
# class PictureAdmin(admin.ModelAdmin):
# 	list_display = ['get_image', ]
#
# 	def get_image(self, obj):
# 		return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

	# def preview(self, obj):
	# 	return mark_safe(f'<BASE_DIR / "media"="{obj.img_poster.url}" style="200px: 200px;">')