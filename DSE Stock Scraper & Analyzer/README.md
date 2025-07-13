# DSE Stock Scraper & Analyzer

A Python project to automatically scrape the latest share prices from the Dhaka Stock Exchange (DSE) and export the data to Excel for further analysis.

## Features

- Scrapes the latest share prices and trading data from the official DSE website.
- Extracts key information, including:
  - Trading Code
  - Last Traded Price
  - High, Low, Closing Price
  - Yesterday’s Closing Price
  - Change, Trade, Value (mn), Volume
- Saves the collected data to an Excel file for easy access and analysis.

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [pandas](https://pypi.org/project/pandas/)
- [openpyxl](https://pypi.org/project/openpyxl/) (for Excel export)

## Output

- The output Excel file (`dsebd.xlsx`) will contain all the latest stock data from the DSE, organized in columns for easy filtering and analysis.

## Customization

- You can change the output file path in the script as needed.
- The script can be extended to support additional analysis or export formats.

## Disclaimer

This project is intended for educational and research purposes. Please ensure compliance with DSE's terms of use and data policies before using this tool for commercial purposes.


