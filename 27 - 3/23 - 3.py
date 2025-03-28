def hacer_album(artista, titulo, canciones=None):
    album = {f"artista": artista, "titulo": titulo}
    if canciones:
        album["canciones"] = canciones
    return album

album1 = hacer_album("Kanye West", "Graduation")
album2 = hacer_album("Gustavo Cerati", "Ahí Vamos")
album3 = hacer_album("WOS", "CARAVANA", 2)  

print(album1)
print(album2)
print(album3)

y = "si"
while y != "no":
    a = input(f"Introduce un artista")
    b = input (f"Introduce el titulo de un album suyo")
    albumuser = hacer_album(a,b)
    print(f"Álbum ingresado:", albumuser)
    y = input("Continuar?")