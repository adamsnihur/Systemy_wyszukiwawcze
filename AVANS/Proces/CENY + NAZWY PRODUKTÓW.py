from bs4 import BeautifulSoup
import requests

url = 'https://www.avans.pl/search?query[menu_item]=&query[querystring]=lacie%2520dysk'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

div_element = soup.find('div', {'class': 'c-grid'})

for element in div_element.find_all('div', {'class': 'c-grid_col is-grid-col-1'}):
    c_offerbox_data = element.find('div', {'class': 'c-offerBox_data'})
    product_name = c_offerbox_data.text.replace('\t', '').replace('\n', '')
    if element.find('div', {'class': 'c-offerBox_row is-discount'}) is not None:
        price_div = element.find('div', {'class': 'a-price_old is-small'})
        print(price_div.text + ' / ' + product_name.lstrip())
    elif element.find('div', {'class': 'c-offerBox_row is-discount'}) is None:
        if element.find('div', {'class': 'a-typo is-text'}) is None:
            price_div = element.find('div', {'class': 'a-price clearfix2'})
            print(price_div.text + ' / ' + product_name.lstrip())