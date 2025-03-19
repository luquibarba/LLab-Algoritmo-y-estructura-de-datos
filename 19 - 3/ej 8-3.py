lista = ["juan", "pepe", "ricky", "centurion"]
print(f"Hola {lista[0]}. Te invito mañana para venir a comer a casa. Avisame!")
print(f"Hola {lista[1]}. Te invito mañana para venir a comer a casa. Llamame!")
print(f"Hola {lista[2]}. Te invito mañana para venir a comer a casa. Hablame!")
print(f"Hola {lista[3]}. Te invito mañana para venir a comer a casa.")

print(f"{lista[2]} no puede ir a comer mañana")
lista[3] = input("Ingresa al nuevo invitado:")

print(f"Hola {lista[0]}. Te invito mañana para venir a comer a casa. Avisame!")
print(f"Hola {lista[1]}. Te invito mañana para venir a comer a casa. Llamame!")
print(f"Hola {lista[2]}. Te invito mañana para venir a comer a casa. Hablame!")
print(f"Hola {lista[3]}. Te invito mañana para venir a comer a casa.")

print("Conseguimos mesa más grande, así que voy a invitar a más gente")
lista.insert(0, "cacho")
lista.insert(2, "hector")
lista.append("juanfer")

print(f"Hola {lista[0]}. Te invito mañana para venir a comer a casa. Avisame!")
print(f"Hola {lista[1]}. Te invito mañana para venir a comer a casa. Llamame!")
print(f"Hola {lista[2]}. Te invito mañana para venir a comer a casa. Hablame!")
print(f"Hola {lista[3]}. Te invito mañana para venir a comer a casa.")
print(f"Hola {lista[4]}. Podes mañana venir a comer a casa?")
print(f"Hola {lista[5]}. Veni mañana a comer a casa.")
print(f"Hola {lista[6]}. Te copas mañana a casa?")

