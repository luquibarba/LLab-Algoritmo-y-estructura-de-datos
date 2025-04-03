def mostrar_modelos_completados(modelos_completados):
    """Mostrar todos los modelos que fueron impresos."""
    print("\nLos siguientes modelos han sido impresos:")
    for modelo_completado in modelos_completados:
        print(modelo_completado)

def imprimir_modelos(diseños_no_imprimidos, modelos_completados):
    """
    Simula imprimir cada diseño, hasta que no queden más.
    Mueve cada diseño a modelos_completados después de imprimirlo.
    """
    while diseños_no_imprimidos:
        diseño_actual = diseños_no_imprimidos.pop()
        print(f"Imprimiendo modelo: {diseño_actual}")
        modelos_completados.append(diseño_actual)
