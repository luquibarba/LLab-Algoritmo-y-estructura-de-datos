personas = int(input("Cuantas personas van a haber para cenar??"))
if personas > 8:
    print ("van a tener que esperar para una mesa")
elif personas < 8 or personas == 8:
    print("Pasen tranquilos")