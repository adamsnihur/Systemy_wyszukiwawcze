from datetime import datetime
from bs4 import BeautifulSoup
import requests
import shutil

path = "/Users/joachimuetake/SW projekt/"

szukaj = input ("Szukaj w AVANS: ").replace(" ","%20")

podstawowy_link = f"https://www.avans.pl/search?query[menu_item]=&query[querystring]={szukaj}"

#Pobranie zawartości strony
strona = requests.get(podstawowy_link)
zawartosc = strona.content

#Utworzenie parsera
soup = BeautifulSoup(zawartosc, "html.parser")

#Szukanie elementu zawierającego informację o liczbie produktów
element = soup.find("div", {"class": "c-toolbar_item is-pagination"})
span = element.find("span", {"class": "is-total"})
a = element.find("a", {"class": "is-nextLink"})

#Sprawdzenie, czy element istnieje i wyświetlenie
if span:
  liczba_produktow = int(span.text)
  if a:
    for i in range(1, liczba_produktow+1):
      nastepna_strona = a['href'].replace("page=2", f"page={i}")
      NEW_URL = f"{nastepna_strona}"
      response = requests.get(NEW_URL)
      soup = BeautifulSoup(response.text, 'html.parser')

      div_element = soup.find('div', {'class': 'c-grid'})

      with open('/Users/joachimuetake/SW projekt/dane.csv', 'a') as file:
        for element in div_element.find_all('div', {'class': 'c-grid_col is-grid-col-1'}):
            c_offerbox_data = element.find('div', {'class': 'c-offerBox_data'})
            product_name = c_offerbox_data.text.replace('\t', '').replace('\n', '')
            date_now = datetime.now().strftime("%d.%m.%Y")
            if element.find('div', {'class': 'c-offerBox_row is-discount'}) is not None:
                price_div = element.find('div', {'class': 'a-price_old is-small'})
                price_div_no_zl = price_div.text.replace("zł", "")
                price_div_float = float(price_div_no_zl.replace(",", "."))
                file.write(date_now + ' / ' + 'AVANS / ' + str(price_div_float) + ' / ' + product_name.lstrip().replace('/', '') + '\n')
            elif element.find('div', {'class': 'c-offerBox_row is-discount'}) is None:
                if element.find('div', {'class': 'a-typo is-text'}) is None:
                    price_div = element.find('div', {'class': 'a-price clearfix2'})
                    price_div_no_zl = price_div.text.replace("zł", "")
                    price_div_float = float(price_div_no_zl.replace(",", "."))
                    file.write(date_now + ' / ' + 'AVANS / ' + str(price_div_float) + ' / ' + product_name.lstrip().replace('/', '') + '\n')
  else:
    NEW_URL = f"{podstawowy_link}"
    response = requests.get(NEW_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    div_element = soup.find('div', {'class': 'c-grid'})

    with open('/Users/joachimuetake/SW projekt/dane.csv', 'a') as file:
      for element in div_element.find_all('div', {'class': 'c-grid_col is-grid-col-1'}):
          c_offerbox_data = element.find('div', {'class': 'c-offerBox_data'})
          product_name = c_offerbox_data.text.replace('\t', '').replace('\n', '')
          date_now = datetime.now().strftime("%d.%m.%Y")
          if element.find('div', {'class': 'c-offerBox_row is-discount'}) is not None:
              price_div = element.find('div', {'class': 'a-price_old is-small'})
              price_div_no_zl = price_div.text.replace("zł", "")
              price_div_float = float(price_div_no_zl.replace(",", "."))
              file.write(date_now + ' / ' + 'AVANS / ' + str(price_div_float) + ' / ' + product_name.lstrip().replace('/', '') + '\n')
          elif element.find('div', {'class': 'c-offerBox_row is-discount'}) is None:
              if element.find('div', {'class': 'a-typo is-text'}) is None:
                  price_div = element.find('div', {'class': 'a-price clearfix2'})
                  price_div_no_zl = price_div.text.replace("zł", "")
                  price_div_float = float(price_div_no_zl.replace(",", "."))
                  file.write(date_now + ' / ' + 'AVANS / ' + str(price_div_float) + ' / ' + product_name.lstrip().replace('/', '') + '\n')

else:
  NEW_URL = f"{podstawowy_link}"
  response = requests.get(NEW_URL)
  soup = BeautifulSoup(response.text, 'html.parser')

  div_element = soup.find('div', {'class': 'c-grid'})

  with open('/Users/joachimuetake/SW projekt/dane.csv', 'a') as file:
    for element in div_element.find_all('div', {'class': 'c-grid_col is-grid-col-1'}):
        c_offerbox_data = element.find('div', {'class': 'c-offerBox_data'})
        product_name = c_offerbox_data.text.replace('\t', '').replace('\n', '')
        date_now = datetime.now().strftime("%d.%m.%Y")
        if element.find('div', {'class': 'c-offerBox_row is-discount'}) is not None:
            price_div = element.find('div', {'class': 'a-price_old is-small'})
            price_div_no_zl = price_div.text.replace("zł", "")
            price_div_float = float(price_div_no_zl.replace(",", "."))
            file.write(date_now + ' / ' + 'AVANS / ' + str(price_div_float) + ' / ' + product_name.lstrip().replace('/', '') + '\n')
        elif element.find('div', {'class': 'c-offerBox_row is-discount'}) is None:
            if element.find('div', {'class': 'a-typo is-text'}) is None:
                price_div = element.find('div', {'class': 'a-price clearfix2'})
                price_div_no_zl = price_div.text.replace("zł", "")
                price_div_float = float(price_div_no_zl.replace(",", "."))
                file.write(date_now + ' / ' + 'AVANS / ' + str(price_div_float) + ' / ' + product_name.lstrip().replace('/', '') + '\n')

# Kopiowanie pliku
shutil.copyfile(f'{path}dane.csv', f'{path}dane_bez_spacji.csv')

# Usuwanie znaków " "
with open(f'{path}dane_bez_spacji.csv', 'r+') as f:
    lines = [line.replace(" ","") for line in f.readlines()]
    f.seek(0)
    f.writelines(lines)
    f.truncate()