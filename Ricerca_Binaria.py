"""
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno del della lista, altrimenti False
"""

def ric_bin(lista, num) -> None:
    mid:int = len(lista) //2
    if lista[mid] == num:
        print("numero trovato")

    elif lista[mid] > num:
        ric_bin(lista[:mid], num)
    
    elif lista[mid] < num:
        ric_bin(lista[mid + 1:], num)