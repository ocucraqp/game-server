from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from server.equipments.models import Weapon
from server.equipments.serializers import WeaponSerializer


class WeaponViewSet(ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

    @action(detail=False, methods=['get'])
    def get_buyable_weapon(self, request):
        user = request.user
        queryset = Weapon.objects.filter(price__gte=user.money)
        serializer = WeaponSerializer(queryset, many=True)
        return Response(serializer.data)

    # @action(detail=False, methods=['get'])
    # def get_buyable_armor(self, request):
    #     user = request.user
    #     queryset = Armor.objects.filter(price__gte=user.money)
    #     serializer = WeaponSerializer(queryset, many=True)
    #     return Response(serializer.data)
