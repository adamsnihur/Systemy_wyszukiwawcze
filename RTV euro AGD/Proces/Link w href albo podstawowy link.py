import requests
from bs4 import BeautifulSoup

szukaj = input ("Wpisz nazwę szukanego produktu: ").replace(" ","+")

podstawowy_link = f"https://www.euro.com.pl/search.bhtml?keyword={szukaj}"

url = podstawowy_link

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

div_elements = soup.find('div', {'class':'product-list'})
div_elements_2 = soup.find('div', {'class':'paging'})

if div_elements_2 is None:
    print(podstawowy_link)
else:
    print(div_elements_2.find('a').get('href'))