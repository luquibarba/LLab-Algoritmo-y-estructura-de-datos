
lucasb = {
        "nombre" : "Lucas",
        "apellido": "barba",
        "edad": "16",
        "ciudad": "BSAS"
}


agusq = {
            "nombre" : "Agustin",
            "apellido": "quinte",
            "edad": "16",
            "ciudad": "BSAS"
            }


octac = {
            "nombre" : "Octavio",
            "apellido": "campos",
            "edad": "16",
            "ciudad": "avellanea"
        }

gente = [lucasb, octac, agusq]



for persona in gente:
    print(f"Nombre: {persona['nombre']}, Apellido: {persona['apellido']}, Edad: {persona['edad']}, Ciudad: {persona['ciudad']}")

    