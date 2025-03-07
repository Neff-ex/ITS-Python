"""Scrivere un programma in Python che richieda all'utente di inserire un numero intero rappresentante
il numero di neonati e utilizzi lo statement match per fornire una risposta appropriata:

- Se il numero inserito è 1, stampare "Congratulazioni!"
- Se il numero inserito è 2, stampare "Wow! Gemelli!"
- Se il numero inserito è 3, stampare "Wow! Tre!"
- Se il numero inserito è 4, stampare "Mamma mia Quattro! Wow!"
- Se il numero inserito è 5, stampare "Incredibile! Cinque!"
- Altrimenti, stampare "Non ci credo! n bambini!", sostituendo n con il numero inserito."""

bebes=int(input("Cuantos bebes deseas?  "))

match bebes:
    case 1:
        print("Felicidades!")
    case 2:
        print("Increible! Gemelos!")
    case 3:
        print("Dios! SOn Trillizos")
    case 4:
        print("Madre mia! Cuatro!")
    case 5:
        print("Prepara esa billetera jaja")
    case _:
        print("Se te murieron esas crias, mis condolencias")