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


# 2. Desarrollar un algoritmo para calcular el determinante de una matriz NXN.
# La matriz debe disponer de un método llamado fill_matrix()
# que llena la matriz de números aleatorios entre 1 y 20.

import random


class Matriz:

    def __init__(self, n):
        self.n = n
        self.matriz = [[0 for _ in range(n)] for _ in range(n)]

    # Método para llenar la matriz con números aleatorios
    def fill_matrix(self):
        for i in range(self.n):
            for j in range(self.n):
                self.matriz[i][j] = random.randint(1, 20)

    # Método para mostrar la matriz
    def mostrar(self):
        print("\nMatriz:")
        for fila in self.matriz:
            print(fila)

    # Método para calcular el determinante
    def determinante(self, matriz=None):

        if matriz is None:
            matriz = self.matriz

        # Caso base 1x1
        if len(matriz) == 1:
            return matriz[0][0]

        # Caso base 2x2
        if len(matriz) == 2:
            return (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])

        det = 0

        # Expansión por cofactores
        for c in range(len(matriz)):

            submatriz = []

            for fila in matriz[1:]:
                nueva_fila = fila[:c] + fila[c+1:]
                submatriz.append(nueva_fila)

            signo = (-1) ** c

            det += signo * matriz[0][c] * self.determinante(submatriz)

        return det


# Programa principal
try:
    n = int(input("Ingrese el tamaño de la matriz NxN: "))

    if n <= 0:
        print("Error: El tamaño debe ser mayor que 0.")

    else:
        matriz = Matriz(n)

        matriz.fill_matrix()
        matriz.mostrar()

        print("\nDeterminante:", matriz.determinante())

except ValueError:
    print("Error: Debe ingresar un número entero válido.")
