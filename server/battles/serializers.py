from rest_framework import serializers

from ..accounts.serializers import UserSerializer
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