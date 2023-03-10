from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.users.serializers import UserCreateSerializer, UserSerializer, UserListSerializer
from utils.permissions import UserIsOwner


User = get_user_model()


class UserCreateApiViewSet(GenericViewSet,
                           CreateModelMixin,
                           ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        return UserCreateSerializer
    
    @action(
        detail=False, permission_classes=[IsAuthenticated], methods=["get"]
    )
    def current_user(self, request, email=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserApiViewSet(GenericViewSet,
                     RetrieveModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserIsOwner]
