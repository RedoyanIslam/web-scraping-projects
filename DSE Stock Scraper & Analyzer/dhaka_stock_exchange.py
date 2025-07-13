from bs4 import BeautifulSoup
import requests
import pandas as pd 

all_stocks = []

url = 'https://www.dsebd.org/latest_share_price_scroll_l.php'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
stocks = soup.find_all('table', class_='table table-bordered background-white shares-table fixedHeader')

for stock in stocks:
    rows = stock.find_all('tr')

    for row in rows[1:]:
        cols = row.find_all('td')

        code = cols[1].find('a').text
        ltp = cols[2].get_text()
        high = cols[3].get_text()
        low = cols[4].get_text()
        closep = cols[5].get_text()
        ycp = cols[6].get_text()
        change = cols[7].get_text()
        trade = cols[8].get_text()
        value = cols[9].get_text()
        volume = cols[10].get_text()

        all_stocks.append({
            'Trading Code': code,
            'Last Traded Price': ltp,
            'High': high,
            'Low': low,
            'Closing Price': closep,
            'Yesterday’s Closing Price': ycp,
            'Change': change,
            'Trade': trade,
            'Value(mn)': value,
            'Volume': volume
        })

df = pd.DataFrame(all_stocks)
df.to_excel('E:/dsebd.xlsx', index=True)