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
