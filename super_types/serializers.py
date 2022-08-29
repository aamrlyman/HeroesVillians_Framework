from rest_framework import serializers
from .models import SuperType

class Super_Type(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['id', 'type']

