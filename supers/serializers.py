from rest_framework import serializers
from .models import Super

class SuperSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'catchphrase', 'super_type_id']
        depth = 1
