import pandas as pd

# wczytanie danych z pliku csv
dane = pd.read_csv('/Users/joachimuetake/Lewoniewski Projekt/dane_bez_spacji.csv')

# zapis danych do pliku Excel
dane.to_excel('/Users/joachimuetake/Lewoniewski Projekt/Excel.xlsx')