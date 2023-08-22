from django.urls import path
from external_api_integration.api.v1.views import GetCountryInformationView

urlpatterns = [
    path("fetch-country-information/",GetCountryInformationView.as_view(), name="fetch-country-information")
]