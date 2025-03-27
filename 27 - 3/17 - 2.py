
mascota1 = {
    "tipo": "Perro",
    "nombre_dueño": "Juan"
}

mascota2 = {
    "tipo": "Gato",
    "nombre_dueño": "Ana"
}

mascota3 = {
    "tipo": "Pájaro",
    "nombre_dueño": "Carlos"
}


mascotas = [mascota1, mascota2, mascota3]


for mascota in mascotas:
    print(f"Tipo de animal: {mascota['tipo']}")
    print(f"Nombre del dueño: {mascota['nombre_dueño']}")

