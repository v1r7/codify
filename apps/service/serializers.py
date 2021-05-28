from rest_framework import serializers
from .models import *


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['title', 'description']

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['name', 'title', 'parent']

class SubmitApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitApplication
        fields = ['name', 'mail', 'phone_number',]

class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = ['name', 'description', 'price']

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['name', 'mail', 'phone_number', 'whatsapp_number',
                  'instagram', 'twitter', 'facebook']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'description', 'created_at']

