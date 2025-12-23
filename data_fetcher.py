"""Module for fetching country and indicator data from World Bank API."""
import requests
import streamlit as st


@st.cache_data
def fetch_countries():
    """Fetch country data from World Bank API.

    Returns:
        dict: Dictionary mapping country names to their id, latitude, and longitude.
    """
    url = "https://api.worldbank.org/v2/country?format=json&per_page=300"
    response = requests.get(url)
    data = response.json()
    countries_dict = {}  # create a country dictionary
    for item in data[1]:
        # gets name, id, latitude, and longitude of each country
        if item['id'] not in ['CHI', 'SXM', 'PSE', 'MAF', 'GIB', 'CUW', 'NA'] and item['region']['id'] != 'NA':
            # exclude countries/territories with no longitude/latitude and remove non-countries (regions)
            # 'NA' excludes aggregates. Although the json file has
            # "{"id":"ABW","iso2Code":"AW","name":"Aruba","region":{"id":"LCN","iso2code":"ZJ","value":"Latin America & Caribbean"} . . .",
            # "Latin America & Caribbean" is not shown because "countries_dict[item['name']] is getting "Aruba", and getting
            # its id and latitude and longitude.
            countries_dict[item['name']] = {
                "id": item['id'],
                "latitude": item.get('latitude'),
                "longitude": item.get('longitude')
            }
    return countries_dict


def fetch_indicator_data(selected_countries, countries_dict, indicator):
    """Fetch indicator data for selected countries.

    Args:
        selected_countries (list): List of country names.
        countries_dict (dict): Dictionary of country data.
        indicator (str): World Bank indicator code.

    Returns:
        dict: Dictionary mapping country names to their dates and values.
    """
    indicator_data = {}
    for country in selected_countries:
        country_id = countries_dict[country]['id']
        url = f"https://api.worldbank.org/v2/country/{country_id}/indicator/{indicator}?format=json&per_page=100"
        response = requests.get(url)
        data = response.json()
        dates = []
        values = []
        for item in data[1]:  # data[1] is where all country info is located
            if 'value' in item:
                # obtain the year and value corresponding to the specified indicator
                dates.append(item["date"])
                values.append(item["value"])

        indicator_data[country] = {"dates": dates, "values": values}

    return indicator_data
