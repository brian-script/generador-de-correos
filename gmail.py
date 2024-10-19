import random

print("*** generador de correos electronicos ***\n")

with open("palabras.txt", "r") as palabras:
    palabra = [linea.strip() for linea in palabras.readlines()]

lista = []
contraseña_final = []

cantidad = int(input("¿Cuántos correos quieres?: "))
cont = 0

while cont < cantidad:
    correo = ""
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[{]};:,<.>/?\\|`~ ¬ªº£€¥©®™¿¡"
    contraseña_inicial = ""

    for i in range(3):
        correo += random.choice(palabra).strip()
    lista.append(correo + str(random.randint(1, 1000)) + "@gmail.com")

    for i in range(10):
        contraseña_inicial += random.choice(caracteres)
    contraseña_final.append(contraseña_inicial)  

    cont += 1  

with open("correos.txt", "w") as archivo:
    for i in range(cantidad):
        archivo.write(f"\nCorreo número {i + 1} \n{lista[i]}")
        archivo.write(f"\nContraseña: {contraseña_final[i]}\n")


