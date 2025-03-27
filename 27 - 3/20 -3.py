respuestas = []
a = ""
while a != "ninguno":
    a = ""
    a = input ("Si pudieras visitar un lugar en el mundo, ¿a dónde irías? Escribe 'ninguno' para finalizar ")
    if a == "ninguno":
        break
    else:
        respuestas.append(a)

print (*respuestas)

