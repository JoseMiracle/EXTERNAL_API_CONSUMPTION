from rest_framework.views import APIView
from external_api_integration.tasks import getCountryInformation
from rest_framework import status
from rest_framework.response import Response



class GetCountryInformationView(APIView):
    def get(self, request):
        country_name = request.data["country_name"].capitalize()
        try:
            year = int(request.data["year"]) or 2020
        except:
            year = 2018
        
        country_data = getCountryInformation(country_name=country_name, year=year)

        return Response(data=country_data, status=status.HTTP_200_OK)
