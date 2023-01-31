import time
import requests
from bs4 import BeautifulSoup

szukaj = input ("Wpisz nazwę szukanego produktu: ").replace(" ","+")

podstawowy_link = f"https://www.euro.com.pl/search.bhtml?keyword={szukaj}"

url = podstawowy_link

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

div_elements = soup.find('div', {'class':'product-list'})
div_elements_2 = soup.find('div', {'class':'paging'})

paging_numbers = soup.find('div', class_='paging-numbers')

if paging_numbers:
    numbers = [number.text for number in paging_numbers.find_all('a')]
    max_number = max(numbers)
    for i in range(1, int(max_number)+1):
        new_url = f"https://www.euro.com.pl{div_elements_2.find('a').get('href').replace('strona-2', 'strona-' + str(i))}"
        response = requests.get(new_url)
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        products = soup.find_all('div', class_='product-for-list')
        for product in products:
            name = product.find('h2', class_='product-name').text.strip()
            price = product.find('div', class_='price-normal selenium-price-normal').text.strip().replace("zł", "")
            data = time.strftime("%d.%m.%Y")
            shop = 'RTV euro AGD'
            with open('dane.csv', 'a') as file:
                file.write(f'{data} / {shop} / {price} / {name} \n')

else:
    response = requests.get(podstawowy_link)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    products = soup.find_all('div', class_='product-for-list')
    for product in products:
        name = product.find('h2', class_='product-name').text.strip()
        price = product.find('div', class_='price-normal selenium-price-normal').text.strip().replace("zł", "")
        data = time.strftime("%d.%m.%Y")
        shop = 'RTV euro AGD'
        with open('dane.csv', 'a') as file:
            file.write(f'{data} / {shop} / {price} / {name} \n')