"""Module for processing and transforming country indicator data."""
import pandas as pd


def process_indicator_data(indicator_data, is_percentage):
    """Process indicator data into a structured dataframe.

    Args:
        indicator_data (dict): Dictionary containing country data with dates and values.
        is_percentage (bool): Whether to format values as percentages.

    Returns:
        tuple: (df, min_year, max_year, country_count) or (None, None, None, country_count) if no data.
    """
    df = pd.DataFrame()
    min_year = "2024"  # used to find min year for chart
    max_year = "1900"  # used to find max year
    country_count = 0

    for country, data in indicator_data.items():
        # loop iterates over each country and its data (country = key, data = value)
        country_df = pd.DataFrame({
            'Year': data['dates'],
            country: data['values']
        })
        # country_df contains years and values of countries
        country_count += 1

        for i in range(len(country_df['Year']) - 1, -1, -1):
            # iterate from end to 0 (-1 is excluded) and take -1 steps back (decrement by 1)
            # the -1 step causes it to start from last element (1960) and go up (to 2024)
            if not pd.isna(country_df[country][i]):
                min_year = country_df['Year'][i]
                break
                # purpose is so that, for ex., if you select Afghanistan and GDP (Current $USD),
                # line chart goes from 2001 to 2022 (the data before 2001 is "nan") instead of 1960-2022,
                # making it way easier for people to see data without getting frustrated.
                # adding more countries can change the min_year

        for i in range(len(country_df)):
            if not pd.isna(country_df[country].iloc[i]):
                # uses iloc to access rows by position
                max_year = country_df['Year'].iloc[i]
                break
            elif i == len(country_df) - 1:
                max_year = None  # used in case country has no data

        if df.empty:
            # copies first country from country_df into df on first iteration
            df = country_df.copy()
            if is_percentage:
                df[country] = df[country].apply(lambda x: f"{x:.2f}%" if pd.notnull(x) else "No Data")
                # "if pd.notnull(x) else "No Data" displays "No Data" instead of "nan%"
                # converts the values of the country into percentages to 2 decimal places
        else:
            df = pd.merge(df, country_df, on='Year', how='outer')
            # how = 'outer' makes all years appear even if some are missing in one country's data.
            # so, if one country has a specific year while the other doesn't, the other's value gets filled with "NaN"
            # on = 'Year' allows Pandas to align rows in the two dataframes
            if is_percentage:
                df[country] = df[country].apply(lambda x: f"{x:.2f}%" if pd.notnull(x) else "No Data")
                # "if pd.notnull(x) else "No Data" displays "No Data" instead of "nan%"
                # converts the values of the country into percentages to 2 decimal places

    if max_year is None:
        return None, None, None, country_count

    df['Year'] = pd.to_datetime(df['Year'], format='%Y').dt.year  # allows us to use years to sort and plot

    # create min and max val for int representation
    min_value = int(min_year)
    max_value = int(max_year)

    df = df[(df['Year'] >= min_value) & (df['Year'] <= max_value)]
    # without adding parentheses, Python gets "min_year & df['Year']" which results in a type-mismatch comparison error
    # basically filters out all years with no values in countries as best as it can for improved user experience
    df = df.sort_values(by='Year', ascending=True)  # orders data by year so that the years are displayed in order

    return df, min_value, max_value, country_count
