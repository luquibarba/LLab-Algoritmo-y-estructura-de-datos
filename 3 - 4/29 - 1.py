class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
    
    def describir_restaurante(self):
        print(self.nombre_restaurante)
        print(self.tipo_cocina)
    
    def abrir_restaurante(self):
        print(f"El restaurante '{self.nombre_restaurante}' ya está abierto!")

class PuestoDeHelados(Restaurante):
    def __init__(self, nombre_restaurante, tipo_cocina, sabores):
        super().__init__(nombre_restaurante, tipo_cocina) 
        self.sabores = sabores  
    
    def mostrar_sabores(self):
        print(f"Sabores disponibles en {self.nombre_restaurante}:")
        for sabor in self.sabores:
            print(sabor)

puesto = PuestoDeHelados("Helados La Delicia", "Postres", ["Vainilla", "Chocolate", "Fresa", "Menta"])

puesto.mostrar_sabores()

puesto.describir_restaurante()
puesto.abrir_restaurante()
