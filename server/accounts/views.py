from rest_framework.viewsets import ModelViewSet

from server.accounts.models import User
from server.accounts.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # TODO: ModelViewSet.mixins.UpdateModelMixinを参考にする
    # @action(detail=False, methods=['get'])
    # def get_buyable_weapon(self, request):
    #     user = request.user
    #     queryset = Weapon.objects.filter(price__gte=user.money)
    #     serializer = WeaponSerializer(queryset, many=True)
    #     return Response(serializer.data)
