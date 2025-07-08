import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/List_of_aircraft_of_the_Egyptian_Air_Force'

all_aircraft = []

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
aircrafts = soup.find_all('table', class_='wikitable sortable')

for aircraft in aircrafts:
    rows = aircraft.find_all('tr')

    for row in rows[1:]:
        cols = row.find_all('td')

        if len(cols) < 5:
            continue

        aircraft_name = cols[0].find('a').text

        origin =  ', '.join([a_tag.text for a_tag in cols[1].find_all('a')]) if cols[1].find_all('a') else cols[1].get_text(strip=True)

        purpose_data = cols[2].get_text(separator='/', strip=True) if len(cols) > 2 and cols[2].get_text(separator='/', strip=True) else 'N/A'

        version_data = cols[3].get_text(separator='/', strip=True) if len(cols) > 3 and cols[3].get_text(separator='/', strip=True) else 'N/A'

        quantity_data = cols[4].get_text(separator='/', strip=True) if len(cols) > 4 and cols[4].get_text(separator='/', strip=True) else 'N/A'

        all_aircraft.append({
            'Aircraft': aircraft_name,
            'Origin': origin,
            'Type': purpose_data,
            'Version': version_data,
            'Quantity': quantity_data
        })

df = pd.DataFrame(all_aircraft)
df.to_excel('excel_file_path', index=False)
print('Completed')
