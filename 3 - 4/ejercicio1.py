def main():
    lista = []
    for i in range(4):
        elemento = int(input("ingrese numeros a la lista"))
        lista.append(elemento)
    p_elemento = devolver(lista)
    print(p_elemento)

def devolver(lista):
    return lista[0]
main()
