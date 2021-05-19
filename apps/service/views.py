from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from .models import Services

#
# class ServicesView(View):
# 	def get(self, request):
# 		services = Services.objects.all()
# 		return render(request,"services/service_list.html",
# 		              {"service_list": services})