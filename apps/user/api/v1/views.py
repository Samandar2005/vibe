from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.user.models import Ovner
from .serializers import OvnerSerializer

class OvnerListAPIView(ListAPIView):
    queryset = Ovner.objects.all()
    serializer_class = OvnerSerializer

class OvnerCreateAPIView(CreateAPIView):
    queryset = Ovner.objects.all()
    serializer_class = OvnerSerializer

class OvnerUpdateAPIView(UpdateAPIView):
    queryset = Ovner.objects.all()
    serializer_class = OvnerSerializer

class OvnerDestroyAPIView(DestroyAPIView):
    queryset = Ovner.objects.all()
    serializer_class = OvnerSerializer