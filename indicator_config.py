"""Configuration module for indicator mappings and categories."""


def get_economic_indicators():
    """Get economic indicator mappings.

    Returns:
        dict: Mapping of indicator names to their World Bank codes.
    """
    return {
        "": "",
        "GDP (in $USD)": "NY.GDP.MKTP.CD",
        "GDP per Capita (in $USD)": "NY.GDP.PCAP.CD",
        "Military Expenditure (% of GDP)": "MS.MIL.XPND.GD.ZS",
        "Inflation, Consumer Prices (annual %)": "FP.CPI.TOTL.ZG",
        "Unemployment, total estimate (% of total labor force)": "SL.UEM.TOTL.ZS"
    }


def get_social_indicators():
    """Get social indicator mappings.

    Returns:
        dict: Mapping of indicator names to their World Bank codes.
    """
    return {
        "": "",
        "Crude Death Rate (per 1,000 people)": "SP.DYN.CDRT.IN",
        "Life Expectancy at Birth, total years": "SP.DYN.LE00.IN",
        "Literacy Rate, adult total (% of people ages 15 and above)": "SE.ADT.LITR.ZS",
        "Total Fertility Rate (births per woman)": "SP.DYN.TFRT.IN",
    }


def get_environmental_indicators():
    """Get environmental indicator mappings.

    Returns:
        dict: Mapping of indicator names to their World Bank codes.
    """
    return {
        "": "",
        "Energy Use (kg of oil equivalent per capita)": "EG.USE.PCAP.KG.OE",
        "Renewable Energy Consumption (% of total final energy consumption)": "EG.FEC.RNEW.ZS",
        "Forest Area (% of total land area)": "AG.LND.FRST.ZS",
        "Air Pollution, exposure to levels exceeding World Health Organization guideline value (% of total)": "EN.ATM.PM25.MC.ZS",
        "Agricultural Land (% of land area)": "AG.LND.AGRI.ZS"
    }


def get_developmental_indicators():
    """Get developmental indicator mappings.

    Returns:
        dict: Mapping of indicator names to their World Bank codes.
    """
    return {
        "": "",
        "Access to Electricity (% of population)": "EG.ELC.ACCS.ZS",
        "Secure Internet Servers (per 1 million people)": "IT.NET.SECR.P6",
        "Land Area (square kms)": "AG.LND.TOTL.K2",
        "Net Migration": "SM.POP.NETM",
        "Population Density (people per square km of land area)": "EN.POP.DNST",
        "Total Population": "SP.POP.TOTL",
        "Rural Population (% of total population)": "SP.RUR.TOTL.ZS",
        "Urban Population (% of total population)": "SP.URB.TOTL.IN.ZS"
    }


def is_percentage_indicator(indicator_code):
    """Check if an indicator should be displayed as percentage.

    Args:
        indicator_code (str): World Bank indicator code.

    Returns:
        bool: True if indicator should be displayed as percentage.
    """
    percentage_indicators = [
        "MS.MIL.XPND.GD.ZS", "FP.CPI.TOTL.ZG", "SE.ADT.LITR.ZS",
        "EG.FEC.RNEW.ZS", "AG.LND.FRST.ZS", "EN.ATM.PM25.MC.ZS", "AG.LND.AGRI.ZS",
        "EG.ELC.ACCS.ZS", "SP.RUR.TOTL.ZS", "SP.URB.TOTL.IN.ZS"
    ]
    return indicator_code in percentage_indicators
