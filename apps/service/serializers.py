from rest_framework import serializers
from .models import *


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'name', 'title', 'parent', 'image']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'title', 'description', 'image']

class SubmitApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitApplication
        fields = ['id', 'name', 'mail', 'phone_number']

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'name', 'mail', 'phone_number', 'whatsapp_number',
                  'instagram', 'twitter', 'facebook']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'created_at', 'image']

class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = ['id', 'name', 'description', 'price']