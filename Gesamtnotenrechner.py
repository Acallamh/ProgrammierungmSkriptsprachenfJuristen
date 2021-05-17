# Voraussetzungen für Angabe von ganzen Noten
def ganzeNote(text:str) -> int:
    while True:
        wert=input(text)
        try: 
            eingabe=int(wert)
            if(eingabe<0):
                print("Geben Sie bitte eine positive Zahl ein.")
            else:
                if(eingabe>18):
                    print("Geben Sie bitte eine gültige Note (zwischen 0 und 18 Punkten) ein.")
                else:
                    break
        except:
            print("Geben Sie bitte eine Zahl (ohne Nachkommastellen) ein.")
    return eingabe
    
#Nur .5 zulässig

# Voraussetzungen für Gesamtnoten
def Gesamtnote(text:str) -> float:
    while True:
        wert=input(text)
        try: 
            eingabe=float(wert)
            eingabe=eingabe.replace(",",".")
            if(eingabe<0):
                print("Geben Sie bitte eine positive Zahl ein.")
            elif(eingabe>18):
                    print("Geben Sie bitte eine gültige Note (zwischen 0 und 18 Punkten) ein.")
            else:
                if(Nachkommastellen(eingabe) != eingabe):
                    print("Geben Sie eine Note mit zwei Nachkommastellen ein.")
                else:
                    break
        except:
            print("Geben Sie bitte eine Zahl ein.")
    return eingabe

def Nachkommastellen(abc):
    return int(abc*100)/100

def NotenstufeGanzeNote(ganznote): #notenstufen bitte nochmal überarbeiten
    if(ganznote >= 0 and ganznote <= 1.49):
        Notenstufe = "ungenügend"
    elif(ganznote >= 1.50 and ganznote <= 3.99):
        Notenstufe = "mangelhaft"
    elif(ganznote >= 4.00 and ganznote <= 6.49):
        Notenstufe = "ausreichend"
    elif(ganznote >= 6.50 and ganznote <= 8.99):
        Notenstufe = "befriedigend"
    elif(ganznote >= 9.00 and ganznote <= 11.49):
        Notenstufe = "vollbefriedigend"
    elif(ganznote >= 11.50 and ganznote <= 13.99):
        Notenstufe = "gut"
    else:
        Notenstufe = "sehr gut"
    return Notenstufe

# Umwandlung von Noten in Notenstufen
def Notenstufe(gesamtnote:float) -> str:
    if(gesamtnote >= 0 and gesamtnote <= 1.49):
        Notenstufe = "ungenügend"
    elif(gesamtnote >= 1.50 and gesamtnote <= 3.99):
        Notenstufe = "mangelhaft"
    elif(gesamtnote >= 4.00 and gesamtnote <= 6.49):
        Notenstufe = "ausreichend"
    elif(gesamtnote >= 6.50 and gesamtnote <= 8.99):
        Notenstufe = "befriedigend"
    elif(gesamtnote >= 9.00 and gesamtnote <= 11.49):
        Notenstufe = "vollbefriedigend"
    elif(gesamtnote >= 11.50 and gesamtnote <= 13.99):
        Notenstufe = "gut"
    else:
        Notenstufe = "sehr gut"
    return Notenstufe

#Abfrage schriftliche Klausuren EJS

Klausur1 = ganzeNote("Geben Sie bitte die Note der 1. Klausur an: ")
Klausur2 = ganzeNote("Geben Sie bitte die Note der 2. Klausur an: ")
Klausur3 = ganzeNote("Geben Sie bitte die Note der 3. Klausur an: ")
Klausur4 = ganzeNote("Geben Sie bitte die Note der 4. Klausur an: ")
Klausur5 = ganzeNote("Geben Sie bitte die Note der 5. Klausur an: ")
Klausur6 = ganzeNote("Geben Sie bitte die Note der 6. Klausur an: ")


#Gesamtnote schriftliche Noten EJS

GesamtnoteSchriftlichEJS = Nachkommastellen((Klausur1 + Klausur2 + Klausur3 + Klausur4 + Klausur5 + Klausur6) / 6)
print("In den schriftlichen Klausuren der EJS haben Sie die Gesamtnote " + str(GesamtnoteSchriftlichEJS) + " erreicht.")

#Counter, um durchgefallene Klausuren zu zählen

counter = 0
if Klausur1 < 4:
    counter = counter + 1
if Klausur2 < 4:
    counter = counter + 1
if Klausur3 < 4:
    counter = counter + 1
if Klausur4 < 4:
    counter = counter + 1
if Klausur5 < 4:
    counter = counter + 1
if Klausur6 < 4:
    counter = counter + 1

print("In den schriftlichen Klausuren der EJS sind Sie in " + str(counter) + " Klausuren durchgefallen.")
    
if(GesamtnoteSchriftlichEJS < 3.8 or counter > 3):
    print("Sie haben die schriftlichen Prüfungen der Ersten Juristischen Staatsprüfung nicht bestanden.")
    exit
else:
    print("Sie haben damit die schriftlichen Klausuren der EJS bestanden und sind zur mündlichen Prüfung zugelassen worden.")

#Abfrage mündliche Prüfung

MdlPrüfung = Gesamtnote("Geben Sie bitte die Gesamtnote der mündlichen Prüfung an: ")

#Gesamtnote EJS

GesamtnoteEJS = Nachkommastellen(0.7 * GesamtnoteSchriftlichEJS + 0.3 * MdlPrüfung)
print("Die Gesamtnote der Ersten Juristischen Staatsprüfung beträgt "+ str(GesamtnoteEJS)+".")

#Notenstufe EJS

NotenstufeEJS = Notenstufe(GesamtnoteEJS)

print("Sie haben damit die in der ersten Juristischen Staatsprüfung die Notenstufe " + NotenstufeEJS + " erreicht.")

#Abfrage Note Seminararbeit

Seminararbeit = ganzeNote("Geben Sie die Note Ihrer Seminararbeit im Schwerpunkt an: ")
MdlMitarbeit = ganzeNote("Geben Sie die Note an, die Sie für die mündliche Mitarbeit erhalten haben: ")
SeminararbeitMdlMitarbeit = Seminararbeit * 2 / 3 + MdlMitarbeit * 1 / 3

#Abfrage Note Klausur

SPKlausur = ganzeNote("Geben Sie die Note der Schwerpunktklausur an: ") #hier auch wieder kommazahl

#Gesamtnote JUP

GesamtnoteJUP = Nachkommastellen(0.4*SPKlausur + 0.6*SeminararbeitMdlMitarbeit)


if(GesamtnoteJUP < 4.00):
    print("Sie haben versagt.")
    exit
else:
    print("Sie haben in der Juristischen Universitätsprüfung die Gesamtnote"+str(GesamtnoteJUP)+"erreicht.")

NotenstufeJUP = Notenstufe(GesamtnoteJUP)
print("Sie haben in der Juristischen Universitätsprüfung die Notenstufe "+ NotenstufeJUP +" erreicht.")


#Gesamtnoten + Notenstufe EJP

EJP = Nachkommastellen(0.7*GesamtnoteEJS + 0.3*GesamtnoteJUP)

if(EJP < 4.00):
    print("Sie haben die Erste Juristische Prüfung nicht bestanden.")
    exit
else:
    print("Herzlichen Glückwunsch! Sie haben die Erste Juristische Prüfung bestanden.")


NotenstufeEJP:str = Notenstufe(EJP)
print("Sie haben in der Ersten Juristischen Prüfung die Gesamtnote "+ str(EJP) +" erreicht. Dies entspricht der Notenstufe "+NotenstufeEJP+".")