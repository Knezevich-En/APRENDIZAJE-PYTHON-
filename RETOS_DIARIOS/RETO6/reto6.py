import random
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&()"
password = ""

for i in range(8):
    password += random.choice(caracteres)

print(f"La contrasena generada es: {password}")