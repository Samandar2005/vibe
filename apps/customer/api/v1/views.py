from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from apps.customer.models import Customer
from .serializers import CustomerSerializer

class CustomerListAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerCreateAPIView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerUpdateAPIView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDestroyAPIView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer