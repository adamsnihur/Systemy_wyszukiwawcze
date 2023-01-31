szukaj = input ("Wpisz nazwę szukanego produktu: ").replace(" ","+")

podstawowy_link = f"https://www.euro.com.pl/search.bhtml?keyword={szukaj}"

import requests
from bs4 import BeautifulSoup

url = podstawowy_link

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

div_elements = soup.find('div', {'class':'product-list'})
div_elements_2 = soup.find('div', {'class':'paging'})

paging_numbers = soup.find('div', class_='paging-numbers')
if paging_numbers:
    numbers = [number.text for number in paging_numbers.find_all('a')]
    max_number = max(numbers)
    new_url = div_elements_2.find('a').get('href').replace("strona-2", f"strona-{max_number.strip()}")
    print(new_url)
else:
    print(podstawowy_link)