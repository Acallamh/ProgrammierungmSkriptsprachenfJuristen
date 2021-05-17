# Wochenfristberechner

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WochenfristberechnerEOEVyz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from datetime import date,timedelta,datetime # Funktionen für den Umgang mit Daten

from urllib.request import urlopen, Request # Um Daten aus dem Internet abzurufen
import xml.etree.ElementTree as ET

class Ui_Wochenfristberechner(object):
    def setupUi(self, Wochenfristberechner):
        if not Wochenfristberechner.objectName():
            Wochenfristberechner.setObjectName(u"Wochenfristberechner")
        Wochenfristberechner.resize(857, 740)
        self.Einfuehrung = QLabel(Wochenfristberechner)
        self.Einfuehrung.setObjectName(u"Einfuehrung")
        self.Einfuehrung.setGeometry(QRect(20, 10, 441, 51))
        self.FristEing = QTextEdit(Wochenfristberechner)
        self.FristEing.setObjectName(u"FristEing")
        self.FristEing.setGeometry(QRect(430, 256, 104, 41))
        self.BuLEing = QTextEdit(Wochenfristberechner)
        self.BuLEing.setObjectName(u"BuLEing")
        self.BuLEing.setGeometry(QRect(430, 330, 321, 87))
        self.Ergebnis = QTextEdit(Wochenfristberechner)
        self.Ergebnis.setObjectName(u"Ergebnis")
        self.Ergebnis.setGeometry(QRect(30, 440, 721, 87))
        self.Fehlermeldung = QTextEdit(Wochenfristberechner)
        self.Fehlermeldung.setObjectName(u"Fehlermeldung")
        self.Fehlermeldung.setGeometry(QRect(30, 590, 721, 87))
        self.label = QLabel(Wochenfristberechner)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 100, 341, 61))
        self.label.setWordWrap(True)
        self.calendarWidget = QCalendarWidget(Wochenfristberechner)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(430, 10, 392, 236))
        self.label_2 = QLabel(Wochenfristberechner)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 240, 341, 61))
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(Wochenfristberechner)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 350, 331, 51))
        self.label_4 = QLabel(Wochenfristberechner)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 291, 61))
        self.pushButton = QPushButton(Wochenfristberechner)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 540, 93, 28))

        self.retranslateUi(Wochenfristberechner)

        QMetaObject.connectSlotsByName(Wochenfristberechner)
    # setupUi

    def retranslateUi(self, Wochenfristberechner):
        Wochenfristberechner.setWindowTitle(QCoreApplication.translate("Wochenfristberechner", u"Dialog", None))
        self.Einfuehrung.setText("")
        self.label.setText(QCoreApplication.translate("Wochenfristberechner", u"Bitte geben Sie das Datum an, \n"
"in dem das Ereignis eingetreten ist:", None))
        self.label_2.setText(QCoreApplication.translate("Wochenfristberechner", u"Bitte geben Sie die Zahl der Wochen ein, \n"
"welche die Frist dauert:", None))
        self.label_3.setText(QCoreApplication.translate("Wochenfristberechner", u"Geben Sie Ihr Bundesland an:", None))
        self.label_4.setText(QCoreApplication.translate("Wochenfristberechner", u"Dieses Programm berechnet Ihre Wochenfrist.", None))
        self.pushButton.setText(QCoreApplication.translate("Wochenfristberechner", u"Berechnung", None))
    # retranslateUi

def getBundesLand()->str:
    '''Eingabe eines Bundeslandes und Prüfung, ob dies gültig ist'''
    url=urlopen(
            Request("https://www.spiketime.de/feiertagapi/bundeslaender",
            headers={"Accept": "application/xml"})        
        , data=None)
    

    namespaces={'ft': 'http://schemas.datacontract.org/2004/07/FeiertagAPI'}
    document:ET.ElementTree = ET.parse(url)
    laender:ET.Element = document.getroot() 


    value = fenster.BuLEing.toPlainText().lower().strip()
    for land in laender:
        if land.find("ft:Name",namespaces).text.lower()==value or land.find("ft:Abkuerzung",namespaces).text.lower()==value:
            return str(land.find("ft:Abkuerzung",namespaces).text)
    
    fenster.Fehlermeldung.insertPlainText("Dieses Bundesland ist unbekannt. Zulässige Eingabewerte sind: ")
    for land in laender:
        fenster.Fehlermeldung.insertPlainText(f"{land.find('ft:Name',namespaces).text} ({land.find('ft:Abkuerzung',namespaces).text}) ")
    
    return None

def checkFeiertag(datum:date, bundesland:str)->bool:
    '''Funktion, um zu prüfen, ob ein Tag ein Feiertag ist'''

    url=urlopen(
        Request(f"https://www.spiketime.de/feiertagapi/feiertage/{bundesland}/{datum.year}",
        headers={"Accept": "application/xml"}), 
        data=None)
    
    namespaces={'ft': 'http://schemas.datacontract.org/2004/07/FeiertagAPI'}
    document:ET.ElementTree = ET.parse(url)
    feiertage:ET.Element = document.getroot()

    for feiertag in feiertage:
            feiertagDatum:date=datetime.strptime(feiertag.find('ft:Datum',namespaces).text[0:10],'%Y-%m-%d').date()
            if feiertagDatum==datum:
                return True
            if feiertagDatum>datum:
                break 
    return False

def berechnen():
    fenster.Fehlermeldung.setText("")
    start = fenster.calendarWidget.selectedDate().toPyDate()
    try:
        frist = int(fenster.FristEing.toPlainText())
    except:
        fenster.Fehlermeldung.setText("Sie sind doof.")
        return
    if frist < 0:
        fenster.Fehlermeldung.setText("Können Sie in der Zeit rückwärts reisen?")
        return
    
    bundesland = getBundesLand()
    if bundesland is None:
        return
    
    beginn = start+timedelta(days=1) 
    ziel = start+timedelta(weeks=frist)

    while True:
        print("Teste " + str(ziel))
        if checkFeiertag(ziel, bundesland) or ziel.weekday() >= 5:
            print(str(ziel)+" ist ein Feiertag, Samstag oder Sonntag, darum +1")
            ziel = ziel+timedelta(days=1)
        else:
            break

    fenster.Ergebnis.setText("Die Frist beginnt am "+str(beginn)+".\nDas Fristende ist am "+str(ziel)+".")



app = QApplication(sys.argv)
x = QDialog() 
fenster = Ui_Wochenfristberechner()
fenster.setupUi(x)

fenster.pushButton.clicked.connect(berechnen)

x.show()
sys.exit(app.exec())