from rest_framework import serializers
from apps.user.models import Ovner

class OvnerSerializer(serializers.ModelSerializer):

  class Meta:
    model = Ovner
    fields = '__all__'
