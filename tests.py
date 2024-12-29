#Alfabēta burti
alfabets = "AĀBCČDEĒFGĢHIĪJKLMNŅOPRSŠTUŪVZŽ"
#Saraksts, kur glabās vārdus pēc alfabēta kārtas
saraksts = [None] * len(alfabets)  

#Vai vārds atbilst prasībām
def parbaudit_vardu(vards):
    #Vai vārds sākas ar lielo burtu un vai tas satur tikai burtus
    if not vards[0].isupper() or not vards.isalpha(): 
        print("Kļūda: Ievadītais vārds neatbilst noteikumiem.")
        return False
    return True
 
#Cikls ņem jaunus vārdus un tos ieliek sarakstā līdz ir pilns
while None in saraksts:
    vards = input("Lūdzu ievadiet vārdu: ")
    #Pārbauda ievadīto vārdu ar iepriekš rakstīto funkciju
    if not parbaudit_vardu(vards):
        continue
    #Pirmo burtu pārvērš lielajā burtā un iegūst pirmo burtu kā mainīgo
    pirmais_burts = vards[0].upper()
    #Noskaidro vārda alfabēta pozīciju izmantojot pirmo burtu
    pozicija = alfabets.index(pirmais_burts)
    #Ja tajā vietā jau ir vārds, to aizstāj ar jauno vārdu
    if saraksts[pozicija] is not None:
        print(f"Vārds '{vards}' ir ievietots {pozicija + 1}. pozīcijā, aizstājot '{saraksts[pozicija]}'.")
    else:
    #Ja nav vārda, ko aizvietot, tad ievieto sarakstā 
        print(f"Vārds '{vards}' ir ievietots {pozicija + 1}. pozīcijā.")
    #Saglabā vārdu, lai sāktu ciklu no jauna
    saraksts[pozicija] = vards
 
#Kad saraksts ir pilnībā aizpildīts, tad izvada visu sarakstu
print("Saraksts ir pilnībā aizpildīts:")
for i, vards in enumerate(saraksts):
    print(f"{i + 1}. pozīcija: {vards}")

