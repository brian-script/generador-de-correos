import random

print("***generador de correos electronicos ***\n")

with open ("palabras.txt", "r") as palabras:
    palabra = [linea.strip() for linea in palabras.readlines()]

correo = ""
lista = []
cantidad = int(input("Cuantos correos quieres?: "))
cont = 0
while cont < cantidad:
    correo = ""
    for i in range(0, 3):
        correo = correo + random.choice(palabra).strip()
    lista.append(correo + str(random.randint(1, 1000)) + "@gmail.com")
    cont = cont + 1

print(lista)

with open("correos.txt", "w") as archivo:
    for num, a in enumerate(lista):
        archivo.write(f"\nCorreo numero {num + 1} \n{a}")
