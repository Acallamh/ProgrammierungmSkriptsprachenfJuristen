# Programm 1: Mehrwertsteuerberechner
# (c) 14.04.2021, Claudia Pflügler

Artikelpreis = input("Wie viel kostet der Artikel in Euro?")

Nettopreis = str(round(int(Artikelpreis) / 119 * 100, 2))

print("Der Artikel ohne Mehrwertsteuer kostet "+Nettopreis+" Euro.")