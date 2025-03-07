"""Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica), salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."""


giorno=int(input("inserisci una data:  "))
mese=int(input("inserisci mese dell'anno:  "))

data=(giorno, mese)
 
match data:
    case (1, 1):
        print(f"Capodanno")
    case (14, 2):
        print(f"San Valentino")
    case (2, 6):
        print(f"Festa della reppublica")
    case (15, 8):
        print(f"Ferragosto")
    case (31, 10):
        print(f"Halloween")
    case (25, 12):
        print(f"Natale")
    case _:
        print(f"Nessuna festivita importante in questa data")