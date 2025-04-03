class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.clientes_atendidos = 0 
    
    def describir_restaurante(self):
        print(f"Restaurante: {self.nombre_restaurante}")
        print(f"Cocina: {self.tipo_cocina}")
    
    def abrir_restaurante(self):
        print(f"El restaurante '{self.nombre_restaurante}' ya está abierto!")
    def establecer_clientes_atendidos(self, cantidad):
        self.clientes_atendidos = cantidad
    
    def incrementar_clientes_atendidos(self, cantidad):
        self.clientes_atendidos += cantidad


restaurante = Restaurante("La Popular", "Argentina")


print(f"Clientes atendidos al princpio: {restaurante.clientes_atendidos}")


restaurante.clientes_atendidos = 50
print(f"Clientes atendidos despues: {restaurante.clientes_atendidos}")


restaurante.establecer_clientes_atendidos(100)
print(f"Clientes atendidos despyes de establecer: {restaurante.clientes_atendidos}")


restaurante.incrementar_clientes_atendidos(20)
print(f"Clientes atendidos al incrementar: {restaurante.clientes_atendidos}")
restaurante.describir_restaurante()
restaurante.abrir_restaurante()
