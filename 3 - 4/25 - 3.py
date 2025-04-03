def hacer_auto(fabricante, modelo,**info_auto):
    info_auto['fabricante'] = fabricante
    info_auto['modelo'] = modelo
    return info_auto
auto = hacer_auto(
    'Clio', '3200',
    color = 'verde',
    frenos = 'False'
)
print(f"{auto}")