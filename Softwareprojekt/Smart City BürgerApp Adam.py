plz_liste = []
beschreibungen = []

print("Willkommen beim Polizei-Meldesystem")
print("Hier kannst du Vorfälle der Polizei melden! ")
print("Zum Beenden der Eingabe schreibe 'stop' bei der Postleitzahl")
print()

eingabe_aktiv = True

while eingabe_aktiv == True:
    plz = input("Postleitzahl des Vorfalls: ")
    if plz.lower() != "stop":     #Es wird geprüft, ob der Nutzer die Eingabe beenden will
        beschreibung = input("Was ist passiert? Beschreiben Sie den Vorfall: ")
        plz_liste.append(plz)     #Der Liste plz_liste wird die eingegebene Postleitzahl hinzugefügt
        beschreibungen.append(beschreibung) #Der Liste beschreibungen wird die eingegebene Beschreibung des Vorfalls hinzugefügt
        print("Meldung gespeichert")
        print() #Zeilenumbruch
    else:
        eingabe_aktiv = False

print() 
print("MELDUNGEN")

#Zählen wie oft jede Postleitzahl gemeldet wurde:
plz_einmal = []       # Wird gebraucht um eine Liste zu haben, die jede Postleitzahl nur einmal enthält, egal wieviele Meldungen diese PLZ erhält.
plz_meldungen = []    # Anzahl der Meldungen pro Postleitzahl

# Alle gemeldeten Postleitzahlen werden durchgegangen:
for i in range(len(plz_liste)):
    plz_aktuell = plz_liste[i]
    schon_drin = False
    for j in range(len(plz_einmal)):
        if plz_einmal[j] == plz_aktuell: #Prüfen, ob die PLZ schon in der einmal Liste (plz_einmal) ist
            plz_meldungen[j] = plz_meldungen[j] + 1 # Wenn ja: Zähler erhöhen
            schon_drin = True
    if schon_drin == False:
        plz_einmal.append(plz_aktuell) # Wenn die PLZ noch nicht enthalten ist wird sie hinzugefügt
        plz_meldungen.append(1) 

for i in range(len(plz_einmal)):
    print("PLZ " + plz_einmal[i] + ": " + str(plz_meldungen[i]) + " Meldung(en)") # Ausgabe der Anzahl der Meldungen je Postleitzahl

print()
print("MELDUNGEN ABRUFEN")
print("Gib eine Postleitzahl ein um die Meldungen nur dort zu sehen")
print("Gib 'alle' ein, um alle Meldungen anzuzeigen")
print("Mit 'ende' beendet sich das Programm")
print()

abfrage_aktiv = True #Benötigt, um das Programm zu beenden wenn 'ende' eingegeben wird

while abfrage_aktiv == True:
    abfrage = input("Was möchten Sie anzeigen?: ").strip().lower() #Leerzeichen am Anfang und Ende werden entfernt, alle Buchstaben werden kleingeschrieben

    if abfrage == "ende": #Falls 'ende' eingegeben wird, beendet sich das Programm
        abfrage_aktiv = False
    else:
        gefunden = False
        for i in range(len(plz_liste)): #Alle Meldungen durchgehen
            if abfrage == "alle" or abfrage == plz_liste[i]:
                print("PLZ " + plz_liste[i] + ": " + beschreibungen[i]) #Treffer wird ausgegeben
                gefunden = True
        if gefunden == False: #Falls keine passende PLZ oder Meldung zu einer Postleitzahl gefunden wurde
            print("Keine passenden Meldungen gefunden")
        print()