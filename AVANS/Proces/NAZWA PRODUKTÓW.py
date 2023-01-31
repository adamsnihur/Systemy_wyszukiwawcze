# Finalna nazwa dostępnych produktów.

from bs4 import BeautifulSoup
import requests

url = 'https://www.avans.pl/search?query[menu_item]=&query[querystring]=lacie%2520dysk'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

c_grids = soup.find_all('div', class_='c-grid')

for c_grid in c_grids:
    c_grid_cols = c_grid.find_all('div', class_='c-grid_col is-grid-col-1')
    for c_grid_col in c_grid_cols:
        if not c_grid_col.find('div', class_='a-typo is-text'):
            c_offerbox_data = c_grid_col.find('div', class_='c-offerBox_data')
            product_name = c_offerbox_data.text.replace('\t', '').replace('\n', '')
            print(product_name.lstrip())