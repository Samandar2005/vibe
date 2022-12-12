from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.worker.models import Worker
from .serializers import WorkerSerializer

class WorkerListAPIView(ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerCreateAPIView(CreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerUpdateAPIView(UpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerDestroyAPIView(DestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

