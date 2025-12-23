import numpy as np
import streamlit as st
import pandas as pd
import util as util


from data_fetcher import fetch_countries, fetch_indicator_data
from indicator_config import (
    get_economic_indicators,
    get_social_indicators,
    get_environmental_indicators,
    get_developmental_indicators,
    is_percentage_indicator
)
from data_processor import process_indicator_data
from chart_handler import display_line_chart, display_area_chart, display_bar_chart, display_table


util.page_color()

st.title("Country Data Explorer")


countries = fetch_countries()
sorted_country_names = sorted(countries.keys())  # this sorts countries by alphabet
selected_countries = st.multiselect("Select Countries", options=sorted_country_names)

if selected_countries:
    world_map = st.checkbox("Display Map", value=True, key='map')  # checkbox for user to display map
    # used to store longitude and latitude to display the map
    coordinates = np.zeros((len(selected_countries), 2))  # make distinct 1D arrays for each selected country

    if world_map:  # if user selects checkbox
        for country_index in range(len(selected_countries)):
            country_name = selected_countries[country_index]
            country_data = countries[country_name]
            for j in range(1):
                coordinates[country_index][j] = country_data['latitude']
                coordinates[country_index][j+1] = country_data['longitude']
                # set latitude and longitude for each country into their own 1D arrays

        map_data = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])  # used to display each country on the map as a red dot
        st.map(map_data)  # displays the map
    else:
        st.session_state.map_display = False

    util.button_style()

    # used to determine whether the charts and table need percentages or not
    if 'chart_percentage' not in st.session_state:
        st.session_state.chart_percentage = False


    cols = st.columns(4)  # used to display the side-by-side buttons in columns

    if "selected_category" not in st.session_state:
        st.session_state.selected_category = -1
        # allows selected_category to be saved with a value so that important features like the selectbox and charts don't disappear when user
        # chooses an option in selectbox (aka when streamlit reruns)

    with cols[0]:
        if st.button("Economic Factors"):
            st.session_state.selected_category = 0
    with cols[1]:
        if st.button("Social Factors"):
            st.session_state.selected_category = 1
    with cols[2]:
        if st.button("Environmental Factors"):
            st.session_state.selected_category = 2
    with cols[3]:
        if st.button("Developmental Factors"):
            st.session_state.selected_category = 3

    selected_category = st.session_state.selected_category
    indicator_code = None  # set to nothing, so it can be used outside of if statements

    if selected_category == 0:  # economic indicators/factors
        indicator_map = get_economic_indicators()
        indicator = st.selectbox("Select an economic factor to see data on", list(indicator_map.keys()))
        indicator_code = indicator_map[indicator]
        st.session_state.chart_percentage = is_percentage_indicator(indicator_code)

    elif selected_category == 1:  # social indicators/factors
        indicator_map = get_social_indicators()
        indicator = st.selectbox("Select a social factor to see data on", list(indicator_map.keys()))
        indicator_code = indicator_map[indicator]
        st.session_state.chart_percentage = is_percentage_indicator(indicator_code)

    elif selected_category == 2:  # environmental indicators/factors
        indicator_map = get_environmental_indicators()
        indicator = st.selectbox("Select an environmental factor to see data on", list(indicator_map.keys()))
        indicator_code = indicator_map[indicator]
        st.session_state.chart_percentage = is_percentage_indicator(indicator_code)

    elif selected_category == 3:  # developmental indicators/factors
        indicator_map = get_developmental_indicators()
        indicator = st.selectbox("Select a developmental factor to see data on", list(indicator_map.keys()))
        indicator_code = indicator_map[indicator]
        st.session_state.chart_percentage = is_percentage_indicator(indicator_code)

    if indicator_code:
        indicator_data = fetch_indicator_data(selected_countries, countries_dict=countries, indicator=indicator_code)
        # a dictionary with country names as keys and data (dates and values)

        df, min_value, max_value, country_count = process_indicator_data(
            indicator_data,
            st.session_state.chart_percentage
        )

        if max_value is None:
            # Warning if all countries selected contain no data
            # Ex. Afghanistan -> Environmental Factors -> Energy use
            if country_count == 1:
                st.warning("This country has no available data for the selected indicator.")
            else:
                st.warning("These countries have no available data for the selected indicator.")
        else:
            # Plot charts and table
            display_line_chart(df, min_value, max_value, st.session_state.chart_percentage)
            display_area_chart(df, min_value, max_value, st.session_state.chart_percentage)
            display_bar_chart(df, min_value, max_value, st.session_state.chart_percentage)
            display_table(df)