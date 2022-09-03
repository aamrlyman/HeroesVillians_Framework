from rest_framework import serializers
from .models import SuperType

class Super_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['id', 'type']

