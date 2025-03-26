persona = int(input("Ingresa la edad de la persona:"))
if persona <= 2:
    print("La persona es un bebe")
elif persona <= 4 and persona >= 2:
    print("La persona es un niño")
elif persona <= 13 and persona >= 4:
    print("La persona es un nene")
elif persona <= 20 and persona >= 13:
    print("La persona es un adolecente mayor")
elif persona <= 65 and persona >= 20:
    print("La persona es un adulto")
else:
    print("Es un señor adulto")
