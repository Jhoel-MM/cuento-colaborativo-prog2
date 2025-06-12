def contar_apariciones(lista, elemento_buscado):

    contador = 0

    for elemento in lista:
        if elemento == elemento_buscado:
            contador += 1
    return contador

print("\nProbando contar_apariciones...\n")

lista_ejemplo = [5, 4, 4, 8, 8, 5, 6, 2, 1, 1, 8, 4]
elementos_a_buscar = [5, 4, 1, 8]

for elemento in elementos_a_buscar:
    resultado = contar_apariciones(lista_ejemplo, elemento)
    print(f"Elemento '{elemento}' aparece {resultado} veces en la lista: {lista_ejemplo}")
print("\nJhoel Ivan Macias Mamani - FIN DEL PROGRAMA QUE CUENTA LAS VECES QUE APARECE UN ELEMENTO")