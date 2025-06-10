base1 = 10
altura1 = 5
area1 = base1 * altura1
print(f"El area del rectangulo 1 ({base1}*{altura1}) es : {area1}")

base2 = 7
altura2 = 3
area2 = base2 * altura2
print(f"el area del rectangualo 2 ({base2}*{altura2}) es : {area2}")
def mostar_area_rectangulo(numero, base, altura):
  area = calcular_area_rectangulo(base, altura)
  print(f"el area del rectangulo {numero} ({base}*{altura}) es : {area}")