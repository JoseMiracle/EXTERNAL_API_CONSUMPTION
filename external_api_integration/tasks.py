import requests
import pandas as pd


from external_api_integration.years import (
    FIRST_TWENTY_YEARS,
    SECOND_TWENTY_YEARS,
    THIRD_TWENTY_YEARS,
)
from timeit import default_timer as timer



def getCountryInformation(country_name: str, year: int):
    start = timer()

    response = requests.get("https://countriesnow.space/api/v0.1/countries/population")

    country_info = response.json()

    parsed_data = country_info["data"]

    df = pd.DataFrame(parsed_data)

    target_country = country_name  # Replace with the desired country name
    
    target_country_data = df[df["country"] == target_country] # Filter for the target country

    merged_information = None
    country_information = {}
    if not target_country_data.empty:
        capital_info_and_iso = getCountryCapitalAndTheirIso(
            target_country=target_country
        )  # This is to get the country's capital and their Iso
        country_currency = getCountryCurrency(target_country=target_country)
        
        population_counts = target_country_data["populationCounts"].values[0] # Access the populationCounts for the target country
        year_index = year - 1960

        if year in FIRST_TWENTY_YEARS:
            country_information[
                f"counts of population in year:{year}"
            ] = population_counts[year_index]["value"]

        elif year in SECOND_TWENTY_YEARS:
            country_information[
                f"counts of population in year:{year}"
            ] = population_counts[year_index]["value"]

        elif year in THIRD_TWENTY_YEARS:
            country_information[
                f"counts of population in year:{year}"
            ] = population_counts[year_index]["value"]

        merged_country_information = capital_info_and_iso | country_information | country_currency
        return merged_country_information
    else:
        return {
            "Error": "country not found"
        }
    

# NOTE: # https://countriesnow.space/api/v0.1/countries/population/cities/filter


def getCountryCapitalAndTheirIso(target_country) -> dict[str, any]:
    """
    This gets the country's capital, iso2, and iso3
    """
    response = requests.get("https://countriesnow.space/api/v0.1/countries/capital")

    country_info = response.json()
    parsed_data = country_info["data"]
    df = pd.DataFrame(parsed_data)

    # Find the index of the country in the DataFrame
    country_index = df[df["name"] == target_country].index[0]

    # Retrieve the capital, iso2, and iso3 directly using .loc
    capital_of_target_country = df.loc[country_index, "capital"]
    iso2_of_target_country = df.loc[country_index, "iso2"]
    iso3_of_target_country = df.loc[country_index, "iso3"]

    return {
        "country": target_country,
        "capital": capital_of_target_country,
        "iso2_of_country": iso2_of_target_country,
        "iso3_of_country": iso3_of_target_country,
    }



def getCountryCurrency(target_country):
    response = requests.get("https://countriesnow.space/api/v0.1/countries/currency")

    country_info = response.json()
    parsed_data = country_info["data"]
    df = pd.DataFrame(parsed_data)

    # Find the index of the country in the DataFrame
    country_index = df[df["name"] == target_country].index[0]
    target_country_currency = df.loc[country_index, "currency"]
    return {
        f"{target_country} currency":target_country_currency
    }

    