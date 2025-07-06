import pandas as pd 
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

path = 'html_file_path'

with open(path, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
elements = soup.find('div', class_='periodni')
element_data = []

for i in range(1,119):
        class_name = f'e{i}'
        element_div = soup.find('div', class_name)

        if element_div:
            title = element_div.find('a', class_=['sy', 'sy bs'])['title']
            symbol = element_div.find('a', class_=['sy', 'sy bs']).text.strip()
            atomic_number = element_div.find('div', class_='ab').text.strip()
            atmoic_mass = element_div.find('div', class_='mm').text.strip('[]')
        

            element_data.append({
                'Element': title,
                'Symbol': symbol,
                'Atomic Number': atomic_number,
                'Atomic Mass': atmoic_mass
            })

df = pd.DataFrame(element_data)
df.to_excel('excel_file_path', index=False)

plt.figure(figsize=(20,40))
x = df['Atomic Number']
y = df['Atomic Mass']
s = df['Symbol']
plt.plot(x, y, 'o-', color='red')
plt.xlabel("Atomic Number", fontweight='bold')
plt.ylabel("Atomic Mass", fontweight='bold')
plt.title("Atomic Mass vs Atomic Number", fontweight='bold')
plt.xticks(rotation='vertical')
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(10))
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(5))
plt.show()