from rest_framework.viewsets import ModelViewSet

from server.accounts.models import User
from server.accounts.serializers import StatusSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StatusViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = StatusSerializer
