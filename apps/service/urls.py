from django.conf import settings
from django.urls import path
from .views import ServicesView, ProductsView, SubmitApplicationView, ContactsView, NewsView, RatesView

urlpatterns = [
    path('service/', ServicesView.as_view()),
    path('product/', ProductsView.as_view()),
    path('submitapplication/', SubmitApplicationView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('news/', NewsView.as_view()),
    path('rates/', RatesView.as_view()),

]