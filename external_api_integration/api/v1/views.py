from rest_framework.views import APIView
from external_api_integration.tasks import getCountryInformation
from rest_framework import status
from rest_framework.response import Response



class GetCountryInformationView(APIView):
    """
        This gets infomation of a country e.g currency, latitude, longitude
        iso2, iso3 
    """
    def get(self, request):
        if "country_name" not in request.data:
            return Response({
                "Error": "Pls provide a country name"
            }, status=status.HTTP_400_BAD_REQUEST)
        elif "year" in request.data:
            if int(request.data["year"]) > 2018 or int(request.data["year"]) < 1960:
                return Response({
                "Info": "Pls provide a year from 1960 to 2018"
            }, status=status.HTTP_400_BAD_REQUEST)
                   
        
        else:
            country_name = request.data["country_name"].capitalize()
            year = int(request.data["year"]) if "year" in request.data else 2018  
            country_data = getCountryInformation(country_name=country_name, year=year)
            return Response(data=country_data, status=status.HTTP_200_OK)



