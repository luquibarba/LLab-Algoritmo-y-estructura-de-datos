lenguajes_favoritos = {'Juan': 'python', 'Sara': 'c', 'Eduardo': 'rust', 'Agustina': 'c#'}
personas = {'juan', 'lucas', 'sara', 'agustin'}

for nombre in lenguajes_favoritos.keys():
    if nombre.lower() in personas:
        print(f"{nombre.title()} ha repondido.")
    else:
        print(f"{nombre.title()} te invitamos a decir tu lenguaje favorito.")
