from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from api.companies.repository import RepositoryCompanies
from api.companies.serializers import CompaniesModel, CompaniesSerializer, CompaniescreatSerializer


class CompaniesView(ModelViewSet):

    queryset = CompaniesModel.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ["name", "cnpj", "corporate_name", "fantasy_name", "user" ]
    search_fields = ["name", "cnpj", "corporate_name", "fantasy_name", "user" ]
    ordering_fields = ["name", "cnpj", "corporate_name", "fantasy_name", "user" ]

    def get_serializer_class(self):

        if self.action in ["create", "update"]:
            return CompaniescreatSerializer

        return CompaniesSerializer
