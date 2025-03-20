pizza = ["queso", "2 quesos", "3 quesos"]
for a in pizza:
    print ("Me gusta la pizza de:", (a))

print ("me encanta hecha al horno")

pizzas_amigo = list(pizza)
pizza.append("4 quesos")
pizzas_amigo.append("4 jamones")
for a in pizza:
    print ("Me gusta la pizza de:", (a))
for a in pizzas_amigo:
    print ("A mi amigo le gusta la pizza de:", (a))
print (pizza)
print (pizzas_amigo)