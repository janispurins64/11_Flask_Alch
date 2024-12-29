alphabet = "AĀBCČDEĒFGĢHIĪJKĶLĻMNŅOPRSŠTUŪVZŽ"  # Definē latviešu alfabētu
 
word_list = [None] * len(alphabet)  # Izveido tukšu sarakstu ar alfabēta garumu
 
while None in word_list:  # Kamēr nav aizpildīti visi alfabēta saraksta elementi
    word = input("Ievadiet vārdu: ").capitalize()  # Ievadītajam vārdam jāsāka ar lielo burtu
    if word.isalpha() and word[0] in alphabet and word_list[alphabet.index(word[0])] is None:
        # Pārbauda vai ievadītais vārds satur burtus, vai pirmais burts ir jau definētajā alfabētā un vai šī vieta sarakstā ir tukša
        index = alphabet.index(word[0])
        word_list[index] = word  # Ievieto vārdu atbilstošajā vietā sarakstā
        print(f"Vārds '{word}' pievienots {index + 1}. vietā.") # Izvada kurā vietā sarakstā vārds ir ievietots
    else:
        print("Nederīgs vārds. Lūdzu, ievadiet jaunu vārdu.") # Ja neatbilst vārda prasībām, tad jautā ievadīt jaunu vārdu