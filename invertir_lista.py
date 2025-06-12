def invertir_lista(lista_original):
  lista_invertida = []

  for i in range(len(lista_original) - 1, -1, -1):
      lista_invertida.append(lista_original[i])

  return lista_invertida

print("\nProbando invertir_lista...\n")

lista_prueba = [1, 2, 3, 4, 5, 6, 7]
lista_resultante = invertir_lista(lista_prueba)

print(f"Lista original: {lista_prueba}")
print(f"Lista invertida: {lista_resultante}")

assert lista_resultante == [7, 6, 5, 4, 3, 2, 1]
assert lista_prueba == [1, 2, 3, 4, 5, 6, 7] 

assert invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
assert invertir_lista([]) == []

print("¡Pruebas para invertir_lista pasaron!…")
print("\nJhoel Ivan Macias Mamani - FIN DEL PROGRAMA QUE INVIERTE LOS ELEMENTOS DE UNA LISTA")