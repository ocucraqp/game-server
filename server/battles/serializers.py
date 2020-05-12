from rest_framework import serializers

from server.accounts.serializers import UserSerializer
from server.accounts.models import User
from server.battles.models import EnemyType, Enemy, Contribution


class EnemyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnemyType
        fields = '__all__'


class EnemySerializer(serializers.ModelSerializer):
    type = EnemyTypeSerializer()

    class Meta:
        model = Enemy
        fields = '__all__'


class ContributionSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Contribution
        fields = '__all__'

class DistributeStatusPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            model.st_point,
            model.status_hp,
            model.status_arm,
            model.status_luck,
        ]
