class Restaurante :
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
    
    def describir_restaurante(self):
        print(self.nombre_restaurante)
        print(self.tipo_cocina)
    
    def abrir_restaurante(self):
        print (f"El restaurante '{self.nombre_restaurante}' ya esta abierto!")

restaurante = Restaurante(f"La Popular", "Argentina")  

restaurante.describir_restaurante()
restaurante.abrir_restaurante()