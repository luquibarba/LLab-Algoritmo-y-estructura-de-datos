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


user1 = Usuario("Lucas", "Barba", 25)  
user2 = Usuario("Agus", "Quinte", 30)  

user1.describir_usuario()
user1.saludar_usuario()
user2.describir_usuario()
user2.saludar_usuario()
