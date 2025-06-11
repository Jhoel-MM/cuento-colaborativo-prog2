num_tabla = int(input("ingrese un numero para ver tapla de multiplicar:"))
print(f"\n--- Tabla del {num_tabla} ---")
for i in range (1, 11):
    resultado = num_tabla * i
    print(f"{num_tabla} x {i} = {resultado} ")