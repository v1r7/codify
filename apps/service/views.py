from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import ServicesSerializer, ProductsSerializer, SubmitApplicationSerializer, ContactsSerializer, \
    NewsSerializer, RatesSerializer
from .models import Services, Products, SubmitApplication, Contacts, News, Rates
from rest_framework.permissions import AllowAny


class ServicesView(generics.ListAPIView):
    permission_classes = AllowAny,
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()

class ProductsView(generics.RetrieveAPIView):
    permission_classes = AllowAny,
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

class SubmitApplicationView(generics.CreateAPIView):
    permission_classes = AllowAny,
    serializer_class = SubmitApplicationSerializer
    queryset = SubmitApplication.objects.filter()

    def SubmitApplicationCreate(self, serializer):
        serializer.save(customer=self.request.user)

class ContactsView(generics.ListAPIView):
    permission_classes = AllowAny,
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()

class NewsView(generics.ListAPIView):
    permission_classes = AllowAny,
    serializer_class = NewsSerializer
    queryset = News.object.all()

class RatesView(generics.ListAPIView):
    permission_classes = AllowAny,
    serializer_class = RatesSerializer
    queryset = Rates.object.all()

