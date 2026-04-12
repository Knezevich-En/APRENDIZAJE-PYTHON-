# 🐍 Resumen Definitivo: Python Desde Cero hasta Inteligencia Artificial

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
plt.savefig("grafico.png") # Debe ir ANTES de show()
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
- **`continue`**: Usado dentro de un bucle para ignorar el código restante y saltar a la siguiente repetición.
- **`len(lista)`**: Para contar exactamente cuántos elementos tiene una estructura de datos.
- **`.lower()` y `.upper()`**: Usados en cadenas de texto para forzarlas a minúsculas o mayúsculas.
- **`.strip()` y `.capitalize()`**: Usados para limpiar espacios en blanco pegados por error y forzar la primera letra a mayúscula.
- **Encadenamiento de Métodos (Method Chaining)**: Puedes aplicar múltiples filtros seguidos: `texto.strip().upper()`.
- **Acumulador de Textos (`+=`)**: Puedes usar `+=` para concatenar (pegar) letras continuamente.
- **Fechas Limpias (`datetime`)**: La herramienta `datetime.now()` combinada con el limpiador `.strftime("%Y-%m-%d_%H-%M-%S")` genera firmas de tiempo inquebrantables.
- **Límite del modo Write (`"w"`)**: El modo `"w"` en `with open` crea **archivos**, pero es incapaz de generar la *carpeta padre* si no existe previamente.
- **Descabezar Datos Sucios `.pop(0)`**: Si abres archivos viejos y las primeras/últimas líneas son basura visual, usar `.pop(0)` arranca esas líneas destructivas para no colapsar tu DataFrame.
- **Procesamiento de Lenguaje Natural (NLP)**: Con solo importar un modelo Machine Learning como `TextBlob`, se puede invocar su propiedad matemática `.sentiment.polarity` para medir estadísticamente el odio o amor en una cadena de texto sin ser expertos en redes neuronales. 

---

## 🏆 12. Historial de Retos Diarios (`RETOS_DIARIOS` y `DATA_AVANZADA`)
Aquí se documentan los proyectos construidos al poner todo a prueba.

**Mini Reto #4: El Analista de Presupuestos**
- **Objetivo:** Exportar gráficas a imágenes PNG generadas estructuralmente desde Matplotlib.

**Mini Reto #5: El Purificador de Datos (Data Cleaning)**
- **Objetivo:** Recibir un lote de textos pésimamente formateados, y usar un algoritmo aplicando métodos de limpieza de cadenas (`.strip().capitalize()`).

**Mini Reto #6: El Creador de Contraseñas (Ciberseguridad)**
- **Objetivo:** Programar un generador de tokens usando acumuladores y `random.choice`.

**Mini Reto #7: El Reloj Maestro (Manejo de Timestamps e I/O)**
- **Objetivo:** Integrar la librería base `datetime` combinándolo con comandos de I/O.

**Mini Reto #8: La Calculadora de Descuentos VIP (Lógica Modular)**
- **Objetivo:** Encapsular un motor matemático en una función independiente (usando `def` y `return`) conectándolo a un `while True`.

**Reto Avanzado #1: El Minero de Datos (Data Engineering)**
- **Objetivo:** Aislar una tabla de un .txt dañado en un sistema legacy lleno de fallos de memoria, rompiendo filas con el `.split("|")` y purificando dinámicamente usando `.pop()` en listas de Python hasta inyectarlo sin letras a base de datos de Pandas.

**Reto Avanzado #2: El Lector de Mentes (Inteligencia Artificial / NLP)**
- **Objetivo:** Cargar en tu computadora y memoria RAM un cerebro gratuito de inteligencia artificial puramente algorítmico, y enviar textos de usuarios capturados en un `while True` a su red neuronal usando `TextBlob` para obtener y catalogar su reacción (Enfado/Felicidad) como variables flotantes controladas.

*(Este documento será actualizado todos los días después de que resuelvas tu Reto Diario)*
