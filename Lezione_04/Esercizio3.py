"""Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it.
 Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments."""

def make_shirt(misura:str, scritta:str):
    print(f"La maglitta é taglia {misura} e voglio che ci sia scritto '{scritta}' impreso.")

make_shirt("L", "I <3 Sushi")
make_shirt(scritta="Amo Venezuela", misura="M")
