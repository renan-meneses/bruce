from django.contrib.auth import get_user_model
from django.db import models

from apps.utils.base_model import BaseModel

User = get_user_model()


class CompaniesModel(BaseModel):
    name = models.CharField(max_length=150, unique=True)
    cnpj = models.BigIntegerField(unique=True)
    corporate_name = models.CharField(max_length=150, unique=True)
    fantasy_name = models.CharField(max_length=150, unique=True)
    user = models.ForeignKey(User, related_name="work_for", on_delete=models.CASCADE)