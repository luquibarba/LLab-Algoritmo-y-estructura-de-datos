ciudades = {

    'BSAS' : {
        "pais" : "Argentina",
        "poblacion": "8 millones",
        "dato": "roban mucho"
    },

    'tokyo' : {
        "pais" : "Japon",
        "Poblacion" : "20 millones",
        "dato" : "es la capital"
    },

    'rio' : {
        "pais" : "Brasil",
        "Poblacion" : "10 millones",
        "dato" : "es la capital"
    }
}

for ciudad, info in ciudades.items():
    print(f"Ciudad:",{ciudad}, "\n")

    for key, datos in info.items():
        print(f"{key}: {datos}")
