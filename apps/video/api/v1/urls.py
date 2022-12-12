# Create your tests here.
from django.urls import *
from .views import *


urlpatterns = [
    path('video/', VideoListAPIView.as_view()),
    path('video/create', VideoCreateAPIView.as_view()),
    path('video/update/<int:pk>', VideoUpdateAPIView.as_view()),
    path('video/delete/<int:pk>', VideoDestroyAPIView.as_view()),
]