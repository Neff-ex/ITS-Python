"""
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.
"""



def lista_tuple(list:tuple) -> dict:
    risultato={}
    for chiave, valore in tuple:
        if chiave in risultato:
            risultato[chiave] += valore
        else:
            risultato[chiave] = valore
    return risultato


def convert(lista:list[tuple]) -> dict:
    dizionario1:dict= {}
    for tuple in lista:
        key, value=tuple[0], tuple[1]  #opcional
        if key in dizionario1:
            dizionario1[key] += value
        else:
            dizionario1[key] = value
        return dizionario1