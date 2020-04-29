from rest_framework import serializers

from server.equipments.models import Weapon


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'
