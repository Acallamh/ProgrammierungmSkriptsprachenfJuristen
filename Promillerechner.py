# Programm 2: Promillerechner
# (C) 14.04.2021, Claudia Pflügler

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BlutalkoholkonzentrationrechnerKAVoRH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import * # hier musste erst Version umgeändert werden, warum?
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys #das wurde nicht im designer eigenständig hinzugefügt - why?


class Ui_AlkRechner(object):
    def setupUi(self, AlkRechner):
        if not AlkRechner.objectName():
            AlkRechner.setObjectName(u"AlkRechner")
        AlkRechner.resize(641, 543)
        self.EingabenButton = QPushButton(AlkRechner)
        self.EingabenButton.setObjectName(u"EingabenButton")
        self.EingabenButton.setGeometry(QRect(410, 80, 131, 31))
        self.AbbrechenButton = QPushButton(AlkRechner)
        self.AbbrechenButton.setObjectName(u"AbbrechenButton")
        self.AbbrechenButton.setGeometry(QRect(410, 120, 131, 28))
        self.Einleitung = QLabel(AlkRechner)
        self.Einleitung.setObjectName(u"Einleitung")
        self.Einleitung.setGeometry(QRect(20, 10, 441, 41))
        self.Geschlecht = QTextEdit(AlkRechner)
        self.Geschlecht.setObjectName(u"Geschlecht")
        self.Geschlecht.setGeometry(QRect(20, 60, 161, 31))
        self.Menge = QTextEdit(AlkRechner)
        self.Menge.setObjectName(u"Menge")
        self.Menge.setGeometry(QRect(20, 100, 161, 31))
        self.AlkAnteil = QTextEdit(AlkRechner)
        self.AlkAnteil.setObjectName(u"AlkAnteil")
        self.AlkAnteil.setGeometry(QRect(20, 140, 161, 31))
        self.GeschlechtAnt = QTextEdit(AlkRechner)
        self.GeschlechtAnt.setObjectName(u"GeschlechtAnt")
        self.GeschlechtAnt.setGeometry(QRect(210, 60, 161, 31))
        self.MengeAnt = QTextEdit(AlkRechner)
        self.MengeAnt.setObjectName(u"MengeAnt")
        self.MengeAnt.setGeometry(QRect(210, 100, 161, 31))
        self.AlkAnteilAnt = QTextEdit(AlkRechner)
        self.AlkAnteilAnt.setObjectName(u"AlkAnteilAnt")
        self.AlkAnteilAnt.setGeometry(QRect(210, 140, 161, 31))
        self.Fehlermeldung = QLineEdit(AlkRechner)
        self.Fehlermeldung.setObjectName(u"Fehlermeldung")
        self.Fehlermeldung.setGeometry(QRect(90, 220, 221, 81))
        self.textEdit = QTextEdit(AlkRechner)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 310, 351, 31))
        self.Gewicht = QTextEdit(AlkRechner)
        self.Gewicht.setObjectName(u"Gewicht")
        self.Gewicht.setGeometry(QRect(20, 180, 161, 31))
        self.GewichtAnt = QTextEdit(AlkRechner)
        self.GewichtAnt.setObjectName(u"GewichtAnt")
        self.GewichtAnt.setGeometry(QRect(210, 180, 161, 31))

        self.retranslateUi(AlkRechner)

        QMetaObject.connectSlotsByName(AlkRechner)
    # setupUi

    def retranslateUi(self, AlkRechner):
        AlkRechner.setWindowTitle(QCoreApplication.translate("AlkRechner", u"Dialog", None))
        self.EingabenButton.setText(QCoreApplication.translate("AlkRechner", u"Eingaben komplett", None))
        self.AbbrechenButton.setText(QCoreApplication.translate("AlkRechner", u"Abbrechen", None))
        self.Einleitung.setText(QCoreApplication.translate("AlkRechner", u"Beantworten Sie die Fragen, um Ihre Blutalkoholkonzentration zu berechnen.", None))
    # retranslateUi

def berechne():    
    # es fehlt die Möglichkeit, in das GeschlechtAnt Feld einen Text einzugeben, bzw. aus diesem dann auch Geschlechtmw zu definieren, oder?
    # es fehlt Fehlermeldung, wenn andere Buchstaben als m oder w eingegeben werden

    Geschlechtmw = fenster.GeschlechtAnt.toPlainText() ## .currentText #warum gibt es currenttext nicht???

    if(Geschlechtmw == "m"):
        Reduktionsfaktor = 0.7
    elif(Geschlechtmw == "w"):
        Reduktionsfaktor = 0.6
    else: 
        fenster.Fehlermeldung.setText("Kein m oder w!")
        return

    
    # hier fehlt Fehlermeldung, wenn negative Menge eingegeben wird
    try:
        GetrunkeneMenge = float(fenster.MengeAnt.toPlainText()) #wie kann ich QTextEdit in float umwandeln?
    except:
        fenster.Fehlermeldung.setText("Getrunkene Menge ist keine Zahl")
        return
    
    try:
        Alkoholanteil = float(fenster.AlkAnteilAnt.toPlainText())
    except:
        fenster.Fehlermeldung.setText("Geben Sie einen Wert ein.")

    
    GewichtKG = fenster.GewichtAnt.toPlainText()


    Alkoholmasse = float(GetrunkeneMenge) * float(Alkoholanteil) * float(8) #Berechnung Masse des Alkohols
    Blutalkohol = round(float(Alkoholmasse) / float(GewichtKG) * float(Reduktionsfaktor), 2) #Berechnung Blutalkohol in Promille
    fenster.textEdit.insertPlainText("Die Blutalkoholkonzentration beträgt "+ str(Blutalkohol)+" Promille.") #Ausgabe Blutalkohol in Promille

def stoppen():
    sys.exit()

app = QApplication(sys.argv)
x = QDialog() 
fenster = Ui_AlkRechner()
fenster.setupUi(x)

fenster.EingabenButton.clicked.connect(berechne)

fenster.Geschlecht.insertPlainText("Sind Sie männlich = m, oder weiblich = w?")
fenster.Menge.insertPlainText("Wie viele Liter an alkoholischen Getränken haben Sie getrunken?")
fenster.AlkAnteil.insertPlainText("Welchen Alkoholanteil hatten diese alkoholischen Getränke in Prozent?")
fenster.Gewicht.insertPlainText("Wie viel wiegen Sie in Kilogramm?")

fenster.AbbrechenButton.clicked.connect(stoppen)

x.show()
sys.exit(app.exec())