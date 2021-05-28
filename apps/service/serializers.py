from rest_framework import serializers
from .models import Product, Service, SubmitApplication, Rate, Contact, News


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'service_id', 'link']


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'title', 'products', 'image']


class SubmitApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitApplication
        fields = ['name', 'email', 'phone_number', 'created_at', 'comment']


class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['name', 'description', 'price']


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'mail', 'phone_number', 'whatsapp_number',
                  'instagram', 'twitter', 'facebook']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'description', 'created_at', 'image']