print("Conversión de número octal de 5 dígitos a decimal")

d1 = int(input("Ingrese el primer dígito: "))
d2 = int(input("Ingrese el segundo dígito: "))
d3 = int(input("Ingrese el tercer dígito: "))
d4 = int(input("Ingrese el cuarto dígito: "))
d5 = int(input("Ingrese el quinto dígito: "))

decimal = d1 * 8**4 
decimal += d2 * 8**3 
decimal += d3 * 8**2 
decimal += d4 * 8**1 
decimal += d5 * 8**0

print("El número en decimal es:", decimal)