# tasas permitidas
tasas = ['USD', 'EUR', 'MXN']

print("Monedas disponibles:")
for moneda in tasas:
    print(moneda)

# seleccionar moneda destino
while True:
    moneda_destino = input("¿A qué moneda deseas convertir? ").upper()
    if moneda_destino in tasas:
        break
    else:
        print("Moneda no válida.")

# consumir API SIN API KEY
import requests

url = "https://api.exchangerate-api.com/v4/latest/COP"

response = requests.get(url)
data = response.json()

# obtener tasa
tasa = data["rates"][moneda_destino]

# pedir valor en COP
while True:
    entrada = input("Ingresa el valor en pesos colombianos (COP): ")
    try:
        valor_envio = float(entrada)
        if valor_envio < 0:
            print("Ingresa un valor positivo.")
            continue
        break
    except:
        print("Error: solo números.")

# conversión
conversion = valor_envio * tasa

# resultado
print(f"{valor_envio} COP = {round(conversion, 2)} {moneda_destino}")
