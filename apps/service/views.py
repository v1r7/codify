from rest_framework import generics
from .serializers import ServicesSerializer, ProductsSerializer, SubmitApplicationSerializer, ContactsSerializer, \
    NewsSerializer, RatesSerializer
from .models import Service, Product, SubmitApplication, Contact, News, Rate
from rest_framework.permissions import AllowAny


class ServicesView(generics.ListAPIView):
    permission_classes = AllowAny,
    serializer_class = ServicesSerializer
    queryset = Service.objects.all()


class ProductsView(generics.RetrieveAPIView):
    permission_classes = AllowAny,
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()


class SubmitApplicationView(generics.CreateAPIView):
    permission_classes = AllowAny,
    serializer_class = SubmitApplicationSerializer
    queryset = SubmitApplication.objects.all()

    # def SubmitApplicationCreate(self, serializer):
    #     serializer.save(customer=self.request.user)


class ContactsView(generics.ListAPIView):
    permission_classes = AllowAny,
    serializer_class = ContactsSerializer
    queryset = Contact.objects.all()


class NewsView(generics.ListAPIView):
    permission_classes = AllowAny,
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class RatesView(generics.ListAPIView):
    permission_classes = AllowAny,
    serializer_class = RatesSerializer
    queryset = Rate.objects.all()
