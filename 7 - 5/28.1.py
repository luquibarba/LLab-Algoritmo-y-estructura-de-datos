class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.clientes_atendidos = 0 

    def describir_restaurante(self):
        print(f"El restaurante se llama {self.nombre_restaurante} y sirve comida {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está ahora abierto.")

    def establecer_clientes_atendidos(self, cantidad):
        self.clientes_atendidos = cantidad

    def incrementar_clientes_atendidos(self, cantidad):
        self.clientes_atendidos += cantidad
restaurante = Restaurante("La Parrilla de Juan", "argentina")
print(f"Clientes atendidos: {restaurante.clientes_atendidos}")
restaurante.clientes_atendidos = 15
print(f"Clientes atendidos (modificado directamente): {restaurante.clientes_atendidos}")
restaurante.establecer_clientes_atendidos(40)
print(f"Clientes atendidos (establecido con método): {restaurante.clientes_atendidos}")
restaurante.incrementar_clientes_atendidos(25)
print(f"Clientes atendidos (incrementado): {restaurante.clientes_atendidos}")

