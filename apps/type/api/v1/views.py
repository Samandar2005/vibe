from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.type.models import Type
from .serializers import TypeSerializer

class TypeListAPIView(ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeCreateAPIView(CreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeUpdateAPIView(UpdateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeDestroyAPIView(DestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer