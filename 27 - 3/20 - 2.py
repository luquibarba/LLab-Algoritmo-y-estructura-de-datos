pedidos_sandwich = ["atun", "pollo", "jyq", "veggie", "pastron", "pastron", "pastron"]

sandwiches_terminados = []

for sandwich in pedidos_sandwich:
    print(f"Prepare tu sandwich {sandwich}.")
    sandwiches_terminados.append(sandwich)

print("preparados:")
print(*sandwiches_terminados)

print ("Nos quedamos sin sandwiches de pastron")
while "pastron" in pedidos_sandwich:
    pedidos_sandwich.pop()

print("Pastron eliminado")