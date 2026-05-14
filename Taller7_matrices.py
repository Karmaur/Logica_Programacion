# 1.	Elaborar un algoritmo que genere un arreglo de N elementos y los ordene
#       de mayor a menor usando método burbuja.

try:
    # Solicitar cantidad de elementos
    n = int(input("Ingrese la cantidad de elementos del arreglo: "))

    # Validar que sea mayor a 0
    if n <= 0:
        print("Error: La cantidad debe ser mayor que 0.")

    else:
        arreglo = []

        # Ingreso de elementos
        for i in range(n):
            while True:
                try:
                    numero = float(input(f"Ingrese el elemento {i + 1}: "))
                    arreglo.append(numero)
                    break
                except ValueError:
                    print("Error:Ingrese un número valido.")

        print("\nArreglo original:")
        print(arreglo)

        # Método burbuja de mayor a menor
        for i in range(n):
            for j in range(0, n - i - 1):
                if arreglo[j] < arreglo[j + 1]:
                    # Intercambiar elementos
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

        print("\nArreglo ordenado de mayor a menor:")
        print(arreglo)

except ValueError:
    print("Error: Debe ingresar un número entero")
