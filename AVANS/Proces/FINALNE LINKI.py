# SCRAPOWANIE LINKÓW

from bs4 import BeautifulSoup
import requests

szukaj = input ("Wpisz nazwę szukanego produktu: ").replace(" ","%20")

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
      print(f"{nastepna_strona}")
else:
  print(f"{podstawowy_link}")