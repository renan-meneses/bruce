from django.urls import include, path

from rest_framework import routers

from .viewsets import CompaniesView

router = routers.DefaultRouter()
router.register(r"", CompaniesView, "Companies")


urlpatterns = [path("Companies/", include(router.urls))]
