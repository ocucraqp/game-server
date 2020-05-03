from rest_framework.viewsets import ModelViewSet

from server.battles.models import EnemyType, Enemy, Contribution
from server.battles.serializers import EnemyTypeSerializer, EnemySerializer, ContributionSerializer


class EnemyTypeViewSet(ModelViewSet):
    queryset = EnemyType.objects.all()
    serializer_class = EnemyTypeSerializer

class EnemyViewSet(ModelViewSet):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer

class ContributionViewSet(ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
