from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from api.accounts.serializers import UserSerializer
from apps.accounts.models import User


class AccountsViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "id", "name", "email", "surname"
    ]
    search_fields = ["id", "name", "email", "surname"]
    ordering_fields = ["id", "name", "email", "surname"]
