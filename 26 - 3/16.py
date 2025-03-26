
glosario = {
    "def": "Se utiliza para definir una función en Python.",
    "if": "Se usa para ejecutar un bloque de código solo si se cumple una condición especificada.",
    "for": "Permite crear un bucle que itera sobre una secuencia (como una lista, tupla, etc.) y ejecuta un bloque de código para cada elemento.",
    "elif": "Se utiliza para especificar una condición adicional en una estructura condicional, que se evalúa si la condición del if es falsa."
}


glosario["else"] = "Se usa para ejecutar un bloque de código cuando ninguna de las condiciones anteriores (if o elif) se cumple."
glosario["class"] = "Se usa para definir una clase, que es una plantilla para crear objetos con atributos y métodos."
glosario["import"] = "Permite traer módulos o bibliotecas externas al código y acceder a sus funciones y clases."
glosario["while"] = "Permite ejecutar un bloque de código mientras una condición sea verdadera."
glosario["return"] = "Se utiliza para devolver un valor desde una función."

for clave, valor in glosario.items():
    print(f"{clave}: {valor}")
