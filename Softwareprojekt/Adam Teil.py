standortPolizist = {
     1: 3,
     2: 4,
     3: 6,
     4: 5,
     5: 2,
     6: 8,
     7: 1
    }


auswahl = int(input("Gib die Nummer des Polizisten ein, von dem du den Standort wissen möchtest: ")) #Man kann die Nummer des Polizisten eingeben, von dem man den Standort wissen möchte.

print("Polizist " + str(auswahl) + " befindet sich gerade im Bereich: " + str(standortPolizist[auswahl])) #Es wird ausgegeben, wo sich der ausgewählte Polizist befindet.

auswahl = input("Willst du den Standort eines Polizisten ändern? ")

if auswahl == "ja" or "Ja":
    while auswahl == "ja" or "Ja":
        auswahl = int(input("Wie lautet die Nummer des Polizisten? "))
        if auswahl > len(standortPolizist):
            print("Den Polizisten gibt es nicht! ")
        else:
            neuerWert = int(input("Welchen Bereich möchtest du ihm zuweisen? "))
            standortPolizist[auswahl] = neuerWert
            print("Dem Polizisten " + str(auswahl) + " wurde der Bereich " + str(neuerWert) + " zugewiesen! ")
            auswahl = input("Möchtest du noch einen Standort ändern? ")
                
print("Programm beendet! ")        
 
