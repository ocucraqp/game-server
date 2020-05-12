from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import action

from server.accounts.models import User
from server.battles.models import EnemyType, Enemy, Contribution
from server.battles.serializers import EnemyTypeSerializer, EnemySerializer, ContributionSerializer, DistributeStatusPointSerializer


class EnemyTypeViewSet(ModelViewSet):
    queryset = EnemyType.objects.all()
    serializer_class = EnemyTypeSerializer


class EnemyViewSet(ModelViewSet):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer


class ContributionViewSet(ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

class BattlesViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = DistributeStatusPointSerializer

    @action(detail=False, methods=['get'])
    def get_status_point(self, request):
        user = request.user
        queryset = User.objects.filter(username=user)
        serializer = DistributeStatusPointSerializer(queryset)
        return Response(serializer.data)

    # DBのUPDATE操作について作る
    @action(detail=False, methods=['post'])
    def distribute_status_point(self, request):
        user = request.user
        queryset = User.objects.filter(username=user)
        serializer = DistributeStatusPointSerializer(queryset)



