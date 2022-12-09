# Create your tests here.
from django.urls import *
from .views import *



urlpatterns = [
    path('ovner/', OvnerListAPIView.as_view()),
    path('ovner/create/', OvnerCreateAPIView.as_view()),
    path('ovner/update/<int:pk>', OvnerUpdateAPIView.as_view()),
    path('ovner/delete/<int:pk>', OvnerDestroyAPIView.as_view()),
]