"""Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop."""

def make_album(artista, titulo, num_canciones=None):
    album = {
        'artista': artista,
        'titulo': titulo
    }
    if num_canciones is not None:
        album['num_canciones'] = num_canciones
    return album

while True:

    artista_input = input("pon el nombre de tu artista (o 'abandona'): ").strip()

    if artista_input.lower() == 'abandona':
        break

    nombre = input("Introduce el titulo: ").strip()

    album = make_album(artista_input, nombre)
    print(album)