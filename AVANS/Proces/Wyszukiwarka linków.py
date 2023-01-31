# podstawowy link

szukaj = input ("Wpisz nazwę szukanego produktu: ").replace(" ","%20")

podstawowy_link = f"https://www.avans.pl/search?query[menu_item]=&query[querystring]={szukaj}"

print(f"Adres URL: {podstawowy_link}")