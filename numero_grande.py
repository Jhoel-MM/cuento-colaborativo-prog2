def encontrar_mayor(lista_numeros):

    if not lista_numeros:
        return None

    mayor_temporal = lista_numeros[0]

    for elemento_actual in lista_numeros[1:]:
        if elemento_actual > mayor_temporal:
            mayor_temporal = elemento_actual

    return mayor_temporal

print("\nProbando encontrar_mayor...\n")

listas_de_prueba = [
    [8, 7, 7, 6, 9],
    [0, -6, -8, -3],
    [24, 24, 24],
    [],
    [7]
]

for lista in listas_de_prueba:
    resultado = encontrar_mayor(lista)
    print(f"Lista: {lista} > Mayor encontrado: {resultado}")

assert encontrar_mayor([8, 7, 7, 6, 9]) == 9
assert encontrar_mayor([0, -6, -8, -3]) == 0
assert encontrar_mayor([24, 24, 24]) == 24
assert encontrar_mayor([]) == None
assert encontrar_mayor([7]) == 7

print("\n¡Pruebas para encontrar_mayor pasaron!…")

print("\nJhoel Ivan Macias Mamani - FIN DEL PROGRAMA ENCUENTRA EL MAYOR ELEMENTO")