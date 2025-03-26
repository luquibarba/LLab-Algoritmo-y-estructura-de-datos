usuarios_actuales = ["shadow", "papupues", "mager", "mateoHuracan2008", "tito"]
usuarios_nuevos = ["Juligamer", "fabrikgamer", "sSlofer", "maGer", "tito"]

for usuarios in usuarios_actuales:
    for usuarios_nuevo in usuarios_nuevos:
        if usuarios.lower() in usuarios_nuevo.lower():
            print("Error, el nombre:",usuarios,"ya esta elegido")