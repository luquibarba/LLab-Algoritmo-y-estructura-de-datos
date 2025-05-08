class Usuario:
    def __init__(self, nombre, apellido, intentos_login):
        self.nombre = nombre
        self.apellido = apellido
        self.intentos_login = intentos_login
    def describir_usuario():
        print("El nombre del usuario es: {self.nombre} {self.apellido}")
    def saludar_usuario():
        print("Hola, {self.nombre}!")
    def incrementar_intentos_login():
        self.intentos_login += 1
    def reiniciar_intentos_login():
        self.intentos_login = 0

Usuario.incrementar_intentos_login()
Usuario.incrementar_intentos_login()
Usuario.incrementar_intentos_login()
Usuario.incrementar_intentos_login()


print (self.intentos_login)
