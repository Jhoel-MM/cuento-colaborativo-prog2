def saludar(nombre_persona):
  mensaje = f"Hola, {nombre_persona}! ¡Que bueno tenerte aqui!"
  print(mensaje)

def sumar(a, b):
  resultado_suma = a + b
  return resultado_suma

saludar("Mary")
saludar("raul")

resultado1 = sumar(9, 7)  
print(f"La suma de 9 y 7 es: {resultado1}")

resultado2 = sumar(150, 250)
print(f"La suma de 150 y 250 es: {resultado2}")