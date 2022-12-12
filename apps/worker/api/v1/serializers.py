from rest_framework import serializers
from apps.worker.models import Worker

class WorkerSerializer(serializers.ModelSerializer):


  class Meta:
      ordering = ['-id']
      model = Worker
      fields = ("id", "full_name", "image", "before", "after")
      extra_kwargs = {'before': {'required': False}, 'after': {'required': False},}
