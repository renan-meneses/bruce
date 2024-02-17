from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from api.companies.repository import RepositoryCompanies
from api.companies.serializers import CompaniesModel, CompaniesSerializer, CompaniescreatSerializer


class BrandViewSet(ModelViewSet):
    queryset = CompaniesModel.objects.all()
    serializer_class = CompaniesSerializer

    def create(self, request):
        response = RepositoryCompanies.create_brand(self, request)
        return response


class CompaniesView(ModelViewSet):

    queryset = CompaniesModel.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ["name", "client"]
    search_fields = ["name"]
    ordering_fields = ["name", "client"]

    def get_serializer_class(self):

        if self.action in ["create", "update"]:
            return CompaniescreatSerializer

        return CompaniesSerializer
