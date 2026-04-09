# 🐍 Resumen Definitivo: Python Desde Cero

¡Esta es tu hoja de trucos (Cheat Sheet)! Aquí está todo lo que hemos aprendido y dominado a lo largo de los ejercicios y retos. Úsala para repasar la sintaxis o cuando no recuerdes cómo se escribía algo.

---

## 1. Variables, Tipos de Datos y Entradas (`VARIABLES_TIPOS`)
La base de nuestro código. Usamos variables para almacenar información y f-strings para imprimir texto dinámico.
```python
# f-strings: Mezclar texto con variables de forma rápida
nombre = "Arturo"
print(f"Hola {nombre}")

# Tipos de datos principales
texto = "Letras" (string)
entero = 23      (int)
decimal = 15.5   (float)
booleano = True  (bool)

# Pedir datos y forzarlos a ser número
edad = int(input("¿Cuántos años tienes?: "))
temperatura = float(input("¿Grados?: "))
```

---

## 2. Lógica y Condiciones (`CONDICIONES`)
Usado para que el ordenador tome decisiones.
```python
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres un niño")
    
# Operadores lógicos: 'and' (y) / 'or' (o)
if tengo_dinero and hay_pizza:
    print("Compramos la pizza")
```

---

## 3. Estructuras de Datos (`ESTRUCTURAS_DATOS`)
Para guardar docenas de cosas sin crear cientos de variables.

**Listas (Para guardar cosas por orden númerico):**
```python
lista = ["Manzana", "Pera", "Mango"]
print(lista[0]) # Imprime 'Manzana' (¡Empieza en 0!)
lista.append("Uva") # Añade al final de la lista
```

**Diccionarios (Para guardar cosas con etiquetas/nombres):**
```python
perfil = {"nombre": "Arturo", "edad": 23}
print(perfil["nombre"]) # Acceder al valor
perfil["ciudad"] = "Guayaquil" # Añadir nueva llave
```

---

## 4. Bucles y Repeticiones (`BUCLES`)
Automatización de tareas repetitivas.

**Bucle `for` (Repetir para cada elemento de una lista):**
```python
for juguete in lista_de_juguetes:
    print(f"Limpiando el {juguete}")
```

**Bucle `while` (Repetirse hasta que una condición se rompa):**
```python
contador = 0
while True: # Bucle infinito
    contador += 1
    if contador == 5:
        break # Rompe el bucle a la fuerza
```

---

## 5. El Blindaje: Errores y Excepciones (`ERRORES`)
Para que un mal teclado no explote nuestro programa.
```python
try:
    numero = int(input("Ingresa un número: "))
except ValueError:
    print("¡Debías usar números, no texto!")
except KeyboardInterrupt:
    print("\nAdios (Pulsaste Ctrl+C)")
```

---

## 6. Crear tus Propias Herramientas (`FUNCIONES`)
No repitamos código, lo paquetizamos usando `def` y lo devolvemos con `return`.
```python
def sumar_precios(precio1, precio2):
    total = precio1 + precio2
    return total # Devuelve el resultado sin imprimirlo

resultado = sumar_precios(50, 100)
```

---

## 7. Manejo de Archivos Físicos (`ARCHIVOS`)
Sobrevivir al apagado de la computadora.
```python
# 'w' (Sobrescribe todo), 'a' (Añade al final), 'r' (Lee)
with open("ruta/mis_metas.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Conseguir un cambio físico\n") # \n para salto de linea
```

---

## 8. El Poder de APIs y Módulos Externos (`LIBRERIAS`)
El internet es tuyo usando `import`.
```python
import random
numero = random.randint(1, 10) # Numero al azar 1-10

# Sacar datos de internet con una API (Pokemon, Usuarios, Clima)
import requests
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
diccionario_api = respuesta.json() # Traduce a un diccionario Python.
```

---

## 9. Ciencia de Datos y Gráficos (`CIENCIA_DATOS`)
Filtrar millones de datos en 3 líneas de código.
```python
import pandas as pd
import matplotlib.pyplot as plt

# Crear o Leer Tablas "DataFrames"
df = pd.read_csv("mis_datos.csv")

# Matemáticas masivas
df["Total"] = df["Sueldo"] + df["Bono"]

# Filtros condicionales
jefes_millonarios = df[ df["Total"] > 5000 ]

# Guardado a Excel
jefes_millonarios.to_excel("jefes.xlsx", index=False)

# Gráficos
plt.bar(df["Empleado"], df["Total"])
plt.show()
```

---

## 10. La Automatización Pura (`AUTOMATIZACION`)
Controlar Windows directamente usando tu código.
```python
import os
import shutil

# Crear carpetas si no existen
os.makedirs("NUEVA_CARPETA", exist_ok=True)

# Escanear qué hay en la carpeta y mover un archivo
archivos = os.listdir("CIENCIA_DATOS")
shutil.move("ruta/archivo1.csv", "ruta2/destino.csv")
```

---

## 11. Descubrimientos Proactivos (¡Trucos Avanzados!)
A lo largo de los ejercicios descubriste e implementaste por tu cuenta estas herramientas profesionales:
- **`continue`**: Usado dentro de un bucle para ignorar el código restante y saltar automáticamente a la siguiente repetición.
- **`len(lista)`**: Para contar exactamente cuántos elementos tiene una estructura de datos.
- **`.lower()`**: Usado en cadenas de texto para transformarlas a minúsculas y hacer que el código sea resistente a mayúsculas mal escritas (Case-Insensitive).
- **`.strip()`**: Para limpiar variables de texto y quitar espacios en blanco invisibles o saltos de línea al final pegados por error.
- **`KeyboardInterrupt`**: Usado junto a `try / except` para evitar que Python cierre feamente con letras rojas si el usuario pulsa `Ctrl + C`.

---

## 🏆 12. Historial de Mini Retos Diarios (`RETOS_DIARIOS`)
Aquí se documentan los proyectos construidos al poner todo a prueba.

**Mini Reto #1: El Recolector de Usuarios**
- **Objetivo:** Conectarse a la API web `https://jsonplaceholder.typicode.com/users`, extraer datos anidados y convertirlos en un DataFrame exportado a Excel (`.xlsx`).
- **Qué pusiste a prueba:** Tu habilidad de manejar diccionarios dentro de diccionarios `["address"]["city"]`, manejar bucles `for` para rellenar listas independientes y usar `requests` mezclado con `pandas`.

**Mini Reto #2: El Casino Infalible**
- **Objetivo:** Crear un juego en consola que te pide adivinar un número al azar, contando los intentos e impidiendo que el código se rompa al ingresar letras u otros símbolos.
- **Qué pusiste a prueba:** `while True`, la inclusión directa del paquete `random`, el control de excepciones estricto usando `except ValueError` y actualizar variables de estado (`intento += 1`). 

**Mini Reto #3: El Secretario Automático (Generador Masivo)**
- **Objetivo:** Crear dinámicamente múltiples sub-carpetas y archivos de texto (`.txt`) independientes, uno para cada cliente en una base de datos, inyectando plantillas de correos con formato personalizado.
- **Qué pusiste a prueba:** Tu dominio de `os.makedirs` y creación local de rutas de sistema largas, el scope (ámbito) de las variables como `ruta_destino` dentro de bucles `for`, la escritura en modo "w", y las "f-strings".

*(Este documento será actualizado todos los días después de que resuelvas tu Reto Diario)*
