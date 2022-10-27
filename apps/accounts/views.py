from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.accounts.models import User
from apps.accounts.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """ CREATE 메소드는 허용하지 않습니다. """
        response = {'ERROR': 'CREATE 메소드는 허용하지 않습니다.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
