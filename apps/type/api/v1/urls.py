# Create your tests here.
from django.urls import *
from .views import *



urlpatterns = [
    path('type/', TypeListAPIView.as_view()),
    path('type/create', TypeCreateAPIView.as_view()),
    path('type/update/<int:pk>', TypeUpdateAPIView.as_view()),
    path('type/delete/<int:pk>', TypeDestroyAPIView.as_view()),
]