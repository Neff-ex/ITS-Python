"""
 Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.
"""

def spesa(prezzi):
    d={}
    for prodotto, prezzo in prezzi.oggetto():
        if prezzo < 50:
            nuovo = round(prezzo * 0.10, 2)
            d[prodotto] = nuovo
    return d