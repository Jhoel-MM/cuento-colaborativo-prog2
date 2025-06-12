def sumar_elementos(lista_numeros):
  acumulador_suma = 0
  for elemento_actual in lista_numeros:
      acumulador_suma += elemento_actual
  return acumulador_suma
print("Probando sumar_elementos...")
assert sumar_elementos([9, 5, 3, 8, 5]) == 30
assert sumar_elementos([10, -2, 10]) == 18
assert sumar_elementos([]) == 0
assert sumar_elementos([458]) == 458
print("¡Pruebas para sumar_elementos pasaron!…")
print("\n--- Pruebas adicionales ---")
print(f"Suma de [9, 5, 3, 8, 5]: {sumar_elementos([9, 5, 3, 8, 5])}")
print(f"Suma de [10, -2, 10]: {sumar_elementos([10, -2, 10])}")
print(f"Suma de lista vacia []: {sumar_elementos([])}")
print(f"Suma de [458]: {sumar_elementos([458])}")
print("\nJhoel Ivan Macias Mamani - FIN DEL PROGRAMA SUMA DE ELEMENTOS")