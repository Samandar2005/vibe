# Create your tests here.
from django.urls import *
from .views import *



urlpatterns = [
    path('worker/', WorkerListAPIView.as_view()),
    path('worker/create', WorkerCreateAPIView.as_view()),
    path('worker/update/<int:pk>', WorkerUpdateAPIView.as_view()),
    path('worker/delete/<int:pk>', WorkerDestroyAPIView.as_view()),
]