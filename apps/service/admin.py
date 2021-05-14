from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Services
from . import models

@admin.register(Services)
class ProductsAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "parent")
	list_filter = ("title",)
	search_fields = ("parent__name", "title__name")
	# list_display_links = ("name")
	def get_search_results(self, request, queryset, search_term):
		queryset, may_have_duplicates = super().get_search_results(
			request, queryset, search_term,
		)
		try:
			search_term_as_int = int(search_term)
		except ValueError:
			pass
		else:
			queryset |= self.model.objects.filter(id=search_term_as_int)
		return queryset, may_have_duplicates


#admin.site.register(models.Services)
admin.site.register(models.Products)
#admin.site.register(models.Category)
admin.site.register(models.submit_application)
admin.site.register(models.contacts)
admin.site.register(models.news)
admin.site.register(models.Picture)

