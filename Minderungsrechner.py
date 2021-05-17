# Minderung im Kaufrecht
# (C) 20.04.2021 Michael Beurskens

def GeldBetrag(text:str)->float:    
  while True:    
    wert=input(text)
    try:
      eingabe=float(wert)
      if(eingabe<0): 
        print("Bitte eine positive Zahl eingeben.") 
      else:
        if(round(eingabe,2) != eingabe): 
          print("Bitte maximal zwei Nachkommastellen eingeben.")
        else:
          break
    except:
      print("Bitte geben Sie eine Kommazahl ein")
  return eingabe

# Kaufpreis muss > 0 sein
Kaufpreis=-1
while Kaufpreis<=0:
  Kaufpreis:float=GeldBetrag("Geben Sie den Kaufpreis ein: ")

# Keine zusätzliche Bedingung
WahrerWert:float=GeldBetrag("Geben Sie den wahren Wert (mit Mangel) ein: ")

# Bedingung: Größer oder gleich wahrer Wert
HypoWert=0
while HypoWert<Kaufpreis:
  HypoWert:float=GeldBetrag("Geben Sie den hypothetischen Wert (ohne Mangel) ein: ")

geminderterKaufpreis = round(Kaufpreis * WahrerWert / HypoWert, 2)

print("Der geminderte Kaufpreis beträgt " + str(geminderterKaufpreis) + "€.")