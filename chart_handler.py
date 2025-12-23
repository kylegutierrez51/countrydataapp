"""Module for handling chart visualizations."""
import streamlit as st
import plotly.express as px


def set_slider(df, min_value, max_value, key):
    """Display a year range slider and filter dataframe.

    Args:
        df (pd.DataFrame): Dataframe to filter.
        min_value (int): Minimum year value.
        max_value (int): Maximum year value.
        key: Unique key for the slider widget.

    Returns:
        pd.DataFrame: Filtered dataframe based on year range.
    """
    year_range = st.slider(" ", min_value=min_value, max_value=max_value, value=(min_value, max_value), key=key)
    start_year = year_range[0]
    end_year = year_range[1]
    filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
    return filtered_df


def display_line_chart(df, min_value, max_value, is_percentage):
    """Display line chart with year slider.

    Args:
        df (pd.DataFrame): Dataframe containing the data.
        min_value (int): Minimum year value.
        max_value (int): Maximum year value.
        is_percentage (bool): Whether to display values as percentages.
    """
    line_chart = st.checkbox("Display Line Chart", value=False, key='line')
    if line_chart:
        filtered_df = set_slider(df, min_value, max_value, key=1)
        filtered_df['Year'] = df['Year'].astype(str)  # removes commas from the years
        if is_percentage:
            filtered_df = filtered_df.melt(id_vars=['Year'], var_name='Country', value_name='Value (%)')
            chart = px.line(filtered_df, x='Year', y='Value (%)', color='Country', markers=True)
        else:
            filtered_df = filtered_df.melt(id_vars=['Year'], var_name='Country', value_name='Value')
            chart = px.line(filtered_df, x='Year', y='Value', color='Country', markers=True)
        st.plotly_chart(chart)


def display_area_chart(df, min_value, max_value, is_percentage):
    """Display area chart with year slider.

    Args:
        df (pd.DataFrame): Dataframe containing the data.
        min_value (int): Minimum year value.
        max_value (int): Maximum year value.
        is_percentage (bool): Whether to display values as percentages.
    """
    area_chart = st.checkbox("Display Area Chart", value=False, key='area')
    if area_chart:
        filtered_df = set_slider(df, min_value, max_value, key=3)
        filtered_df['Year'] = df['Year'].astype(str)  # removes commas from the years
        if is_percentage:
            filtered_df = filtered_df.melt(id_vars=['Year'], var_name='Country', value_name='Value (%)')
            chart = px.area(filtered_df, x='Year', y='Value (%)', color='Country', markers=True)
            chart.update_layout(hovermode="x unified")
        else:
            filtered_df = filtered_df.melt(id_vars=['Year'], var_name='Country', value_name='Value')
            chart = px.area(filtered_df, x='Year', y='Value', color='Country', markers=True)
            chart.update_layout(hovermode="x unified")
        st.plotly_chart(chart)


def display_bar_chart(df, min_value, max_value, is_percentage):
    """Display bar chart with year slider.

    Args:
        df (pd.DataFrame): Dataframe containing the data.
        min_value (int): Minimum year value.
        max_value (int): Maximum year value.
        is_percentage (bool): Whether to display values as percentages.
    """
    bar_chart = st.checkbox("Display Bar Chart", value=False, key='bar')
    if bar_chart:
        filtered_df = set_slider(df, min_value, max_value, key=2)
        filtered_df['Year'] = df['Year'].astype(str)  # removes commas from the years
        if is_percentage:
            filtered_df = filtered_df.melt(id_vars=['Year'], var_name='Country', value_name='Value (%)')
            chart = px.bar(filtered_df, x='Year', y='Value (%)', color='Country')
        else:
            filtered_df = filtered_df.melt(id_vars=['Year'], var_name='Country', value_name='Value')
            chart = px.bar(filtered_df, x='Year', y='Value', color='Country')
        st.plotly_chart(chart)


def display_table(df):
    """Display data table.

    Args:
        df (pd.DataFrame): Dataframe containing the data.
    """
    table = st.checkbox("Display Table", value=False, key='table')
    if table:
        df['Year'] = df['Year'].astype(str)  # removes commas from the years
        df = df.sort_values(by='Year', ascending=False)
        st.dataframe(df, hide_index=True)
