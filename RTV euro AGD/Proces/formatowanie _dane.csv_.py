import shutil

# Kopiowanie pliku
shutil.copyfile('dane.csv', 'dane_bez_spacji.csv')

# Usuwanie znaków " "
with open('dane_bez_spacji.csv', 'r+') as f:
    lines = [line.replace(" ","") for line in f.readlines()]
    f.seek(0)
    f.writelines(lines)
    f.truncate()