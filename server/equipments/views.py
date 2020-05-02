from rest_framework.viewsets import ModelViewSet

from server.equipments.models import Weapon
from server.equipments.serializers import WeaponSerializer


class WeaponViewSet(ModelViewSet) :
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
