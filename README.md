# Global Country Data Dashboard

A Streamlit-based interactive application for exploring and visualizing global country data across multiple categories including economic, social, environmental, and developmental indicators. Its purpose is for users to quickly look up and visualize select information about different countries from 1900s - 2000s so that they can compare data between different countries and learn about them.

This application uses the World Bank API to display the data.

## Project Structure

```
CountryDataApp/
├── CountryDataExplorer.py    # Main application entry point
├── data_fetcher.py            # Country and indicator data retrieval
├── indicator_config.py        # Indicator definitions and configurations
├── data_processor.py          # Data processing and transformation
├── chart_handler.py           # Chart and table display functions
└── util.py                    # Utility functions and styling
```


## Installation
1. Install Python 3.x
2. Clone or download this repository
```bash
git clone https://github.com/kylegutierrez51/countrydataapp.git
```
3. Set up a virtual environment in Python
```bash
python -m venv .venv
```

4. Activate the virtual environment
```bash
.venv\Scripts\Activate.ps1
```

5. Install required dependencies:
```bash
pip install streamlit pandas numpy plotly requests
```

## Usage

Run the application using Streamlit:

```bash
streamlit run CountryDataExplorer.py
```

The application will open in your default web browser.

