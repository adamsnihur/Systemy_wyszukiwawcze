# OSTATECZNY
# Link szukanego produktu + liczba stron produktów + liczba w dobrym miejscu.

szukaj = input ("Wpisz nazwę szukanego produktu: ").replace(" ","+")

podstawowy_link = f"https://www.euro.com.pl/search.bhtml?keyword={szukaj}"

import requests
from bs4 import BeautifulSoup

link = podstawowy_link

response = requests.get(link)
soup = BeautifulSoup(response.content, 'html.parser')
paging_numbers = soup.find('div', class_='paging-numbers')
if paging_numbers:
    numbers = [number.text for number in paging_numbers.find_all('a')]
    max_number = max(numbers)
    print(max_number.strip())
    print(podstawowy_link)
else:
    print(podstawowy_link)