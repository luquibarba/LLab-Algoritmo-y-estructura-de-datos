class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad 

    def describir_usuario(self):
        print(self.nombre)
        print(self.apellido)
        print(self.edad)

    def saludar_usuario(self):
        print(f"Hola {self.nombre}, como andas?") 
    
    intentos_login = 0
    
    def incrementar_intentos_login(self):
        Usuario.intentos_login += 1
    
    def reiniciar_intentos_login(self):
        Usuario.intentos_login = 0

class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios
    
    def mostrar_privilegios(self):
        print("Privilegios:")
        for p in self.privilegios:
            print(f"- {p}")

class Administrador(Usuario):
    def __init__(self, nombre, apellido, edad, privilegios):
        super().__init__(nombre, apellido, edad)
        self.privilegios = Privilegios(privilegios)
    
    def mostrar_privilegios(self):
        self.privilegios.mostrar_privilegios()

admin = Administrador("Carlos", "Gomez", 40, ["puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios"])
admin.mostrar_privilegios()
admin.describir_usuario()
admin.saludar_usuario()
