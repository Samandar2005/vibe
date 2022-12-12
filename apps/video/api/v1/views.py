from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.video.models import Video
from .serializers import VideoSerializer

class VideoListAPIView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoCreateAPIView(CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoUpdateAPIView(UpdateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDestroyAPIView(DestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer