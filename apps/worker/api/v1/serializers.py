from rest_framework import serializers
from apps.worker.models import Worker

class WorkerSerializer(serializers.ModelSerializer):

  class Meta:
    model = Worker
    fields = '__all__'
