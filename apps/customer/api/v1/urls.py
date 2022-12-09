# Create your tests here.
from django.urls import *
from .views import *



urlpatterns = [
    path('customer/', CustomerListAPIView.as_view()),
    path('customer/create', CustomerCreateAPIView.as_view()),
    path('customer/update/<int:pk>', CustomerUpdateAPIView.as_view()),
    path('customer/delete/<int:pk>', CustomerDestroyAPIView.as_view()),
]