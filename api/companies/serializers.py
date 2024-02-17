from rest_framework import serializers

from apps.companies.models import CompaniesModel


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompaniesModel
        fields = ("id", "name", "cnpj", "cnpj", "corporate_name","fantasy_name", "user")


class CompaniescreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompaniesModel
        fields = "__all__"

