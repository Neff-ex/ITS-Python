"""
Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.
"""
def numeri(list:list):
    numer = {
        "positivi": [],
        "negativi": []
    }
    for n in list:
        if n>0:
            numer[list].append(n)
        elif n<0:
            numer[list].append(n)
    return numer
