from rest_framework.response import Response

from api.companies.serializers import CompaniescreatSerializer


class RepositoryCompanies:
    def create_companies(self, request):
        serializer = CompaniescreatSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
