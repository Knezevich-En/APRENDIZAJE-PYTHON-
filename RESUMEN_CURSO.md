# 🐍 Resumen Definitivo: Python Desde Cero hasta Inteligencia Artificial

¡Esta es tu hoja de trucos (Cheat Sheet) maestra! Aquí está todo lo que hemos dominado estructurado con ejemplos del **mundo real**, para que sepas no solo cómo escribirlo, sino *cuándo* usarlo en una empresa.

---

## 1. Variables, Tipos de Datos y Entradas (`VARIABLES_TIPOS`)
> **Caso de uso Real:** Formularios de registro web básicos, captura de precios en un Punto de Venta.

```python
nombre_cliente = "Arturo"
monto_pagar = 145.50
print(f"Factura generada para {nombre_cliente}. Total: ${monto_pagar}")

estado_activo = True  # Útil para saber si un empleado sigue en la empresa.
edad = int(input("¿Cuántos años tienes?: ")) # Forzado a Int
```

---

## 2. Lógica y Condiciones (`CONDICIONES`)
> **Caso de uso Real:** Filtros de pasarelas de pago.

```python
tarjeta_expirada = False
saldo = 50

if tarjeta_expirada == True:
    print("Pago DENEGADO")
elif saldo >= 100:
    print("Pago EXITOSO. ¡Gracias por la compra!")
else: print("Saldo INSÚFICIENTE.")
```

---

## 3. Estructuras de Datos (`ESTRUCTURAS_DATOS`)
> **Caso de uso Real:** Listados ordenados de extracción (Listas) y lectura de JSON webs (Diccionarios).

```python
archivos = ["julio.csv", "agosto.csv"]
archivos.append("nuevo.csv") # Listas mutables.

empleado = { "id": 1001, "rol": "Admin" }
print(empleado["rol"]) # Diccionario con Etiquetas.
```

---

## 4. Bucles y Repeticiones (`BUCLES`)
> **Caso de uso Real:** Envío masivo de correos (For). Mantener el programa prendido (While).

```python
# Bucle For con Iterable: Pasa por cada objeto sin necesitar índices.
for correo in lista_correos:
    enviar(correo) 

# Bucle For Numérico (Rango Fijo)
for i in range(8): # Obliga a girar la máquina exactamente 8 veces.
    print(i)
    
# Menú Infinito
while True:
    texto = input("Escriba SALIR: ")
    if texto == "SALIR": break
```

---

## 5. El Blindaje: Errores (`ERRORES`)
> **Caso de uso Real:** Cajero de interfaz a prueba de caídas o reconexión web segura.

```python
try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: Ingrese solo números. Trataste de volver a Entero un texto.")
except KeyboardInterrupt:
    print("\nEl usuario pulsó Ctrl+C en consola.")
except Exception as e:
    # Este bloque atrapa todo lo demás que no definiste.
    print(f"Error genérico: {e}")
```

---

## 6. Funciones (`def`)
> **Caso de uso Real:** Empaquetar bloques lógicos (como tu Calculadora de Descuentos VIP) para reutilizarlos mil veces.

```python
def aplicar_descuento(precio):
    total = precio * 0.80
    return total # Devuelve la materia procesada, rompiendo la función.

resultado = aplicar_descuento(500)
```

---

## 7. Manejo de Archivos Físicos Avanzado (`ARCHIVOS`)
> **Caso de uso Real:** Escribir Logs persistentes o cargar la memoria completa de un TXT a Python.

```python
# MODO DE ESCRITURA ("w")
with open("registros.txt", "w") as archivo: 
    archivo.write("Guardar info en disco duro\n") 
    
# MODO LECTURA DE MATRICES (".readlines")
with open("dataset.txt", "r") as archivo:
    # A diferencia del .read() normal, readlines convierte cada renglón del
    # bloc de notas en un índice de una Lista Gigante para recorrer con For-Loop.
    lineas_como_lista = archivo.readlines()
```

---

## 8. Data Science (`PANDAS` / `MATPLOTLIB`)
> **Caso de uso Real:** Cruzar datos y exportar para analistas y PowerBI.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos.csv") 

# `.astype(float)`: Herramienta de oro post-lectura. Obliga a que una columna
# que vino contaminada como texto (Ej. precios con comillas) se vuelva decimal matemático.
df["PRECIOS_PURA"] = df["PRECIOS_SUCIOS"].astype(float)

plt.bar(df["A"], df["PRECIOS_PURA"])
plt.savefig("reporte.png") # Va ANTES de show() o se guarda la foto en blanco!
plt.show() 
```

---

## 10. Descubrimientos Proactivos (¡La Armería del Datos!)

Esta es tu armería técnica para limpiar y escarbar en el caos. La lista está equipada con su respectivo código para que lo imites.

**1. Formateo y Limpieza Cruda (`.strip()`, `.upper()`, `.lower()`)**
> Útil para desinfectar entradas de teclado para que no exploten tus bloques 'If'.
```python
entrada = "   sALiR  "
if entrada.strip().upper() == "SALIR":
    print("Cerrando sistema exitosamente.")
```

**2. Ignorar Cabeceras por Patrón (`.startswith(...)`)**
> Usado al minar archivos TXT inmensos que en el top están llenos de decoraciones con asteriscos. 
```python
for linea in lineas_del_archivo:
    if linea.startswith("*") or linea.startswith("LOG:"):
        continue # Ignora la línea si tiene asteriscos y salta a la siguiente!
    print("Linea de tabla útil:", linea)
```

**3. El Machete de Frases (`.split("|")`)**
> Imprescindible para sistemas COBOL o viejos. Corta un texto masivo en base a un ancla de tu elección dejándote una lista `[]`.
```python
# Ejemplo: "| 001 | Arturo |"
datos = linea_cruda.split("|") 
# Automáticamente crea la lista -> ['', ' 001 ', ' Arturo ', '']
```

**4. Arrancar Cabezas y Colas (`.pop()`)**
> Cuando extraes información e infaliblemente te genera posiciones vacías o headers, sencillamente los destruyes usando el índice.
```python
precios = ["EL TITULO BASURA DEL EXCEL", 50, 40, 20]
precios.pop(0) # Apunta y elimina el indice [0]. La lista se regenera.
print(precios) # -> [50, 40, 20]
```

**5. El Acumulador o Contador (`+=`)**
> La forma matemática de darle memoria creciente o decreciente a una variable.
```python
intentos = 0
precio_total = 0

intentos += 1 # Le suma 1 cada que avanza.
precio_total += 50.50 # El número va creciendo orgánicamente sin reiniciarse.
cadena_pass += "Z" # También sirve para ir pegando texto a tu contraseña
```

**6. El Dios del Tiempo (`datetime` y `.strftime()`)**
> Tu fábrica de nombres de archivos inquebrantables.
```python
from datetime import datetime
hora_sucia = datetime.now()
# Formato A-M-D Hora-Minutos-Segundos (File-Friendly, jamas uses DOS PUNTOS en nombres de windows)
hora_limpia = hora_sucia.strftime("%Y-%m-%d_%H-%M-%S") 
ruta = f"C:\\reportes\\log_{hora_limpia}.txt"
```

**7. Inteligencia Artificial NLP (`TextBlob`)**
> Obtener métricas flotantes entre -1.0 y 1.0 para analizar psicología y priorizar tickets de soporte técnico.
```python
from textblob import TextBlob
comentario = "I absolutely hate this new update"
ia = TextBlob(comentario)
matematica_emocion = ia.sentiment.polarity 
# matemática_emocion arroja un número -0.80.
```

**8. Web Scraping (`BeautifulSoup` y `.text`)**
> Cazar HTML puro y depurarlo. La diferencia brutal entre `.text` de Response (Todo el HTML sucio de la web) vs `.text` en Iteraciones Limpias.
```python
import requests
from bs4 import BeautifulSoup
respuesta = requests.get("http://sitio.com")
# El .text aquí trae el código puro <HEAD> de toda la web en formato String.
sabueso_scrap = BeautifulSoup(respuesta.text, "html.parser")

textos_crudos = sabueso_scrap.find_all("span", class_="text") 
for item in textos_crudos:
    # El .text acá anula y le quita todas las etiquetas <span> a la iteración aislada
    # devolviendo solo las Palabras humanas de adentro.
    print(item.text) 
```

**9. Desglose de APIs Remotas (`.json()`)**
> Traducir la respuesta gigante de un servidor web directamente a Diccionarios Nativos de Python estructurados. Utilizado en PokeAPI / JsonPlaceHolder.
```python
respuesta = requests.get("http://api.com/usuario")
diccionario_python = respuesta.json()
print(diccionario_python["nombre"])
```

**10. La Trampa Universal: `CSV Injection`**
> Cuando transfieres tus limpiados datos a comas `.csv`, *debes* recordar inyectarle un marco de `"..."` comillas dobles, o de otra forma Pandas al leerlo sentirá que esa coma natural de la persona significa que quieres dividir esa palabra en la celda derecha originando `NaNs` asimétricos masivos en el DataFrame final.
```python
# 101, "Comida asombrosa, deliciosa" -> Pasa la coma sin romperse.
```

---

## 🏆 11. Tu Historial de Retos Operativos (`CERTIFICACIÓN LOCAL`)

Tus logros en simulaciones de negocio documentadas metódicamente:
1. **API Anidada**: Desglose de "diccionarios" webs usando `requests.get().json()` de una pasarela.
2. **Casino Infalible**: Tu primera interacción usando un menú `while True` con excepciones.
3. **Generador Masivo**: Bucle For usado como clonador de documentos con manipulación de librerías nativas Path/OS.
4. **Data Analytics V0**: Fabricar DataFrames crudos con diccionarios y la Exportación del Gráfico PNG.
5. **Generador Tokens**: Algoritmo `random.choice` con multiplicador `for i in range(8)` y la herramienta del pegamento con bucles `+=`.
6. **Descuento Modular**: Obra encapsulada matemática con implementaciones con un menú protegido `.strip().upper() == "SALIR"`.
7. **Filtrado Legacy COBOL (Data Engineering)**: Cargar Data cruda `.readlines()`. Uso avanzado del `.startswith()`, destruyendo cadenas por barras `split("|")`, retirando cabezas huecas `.pop(0)` y transformado por la fuerza a matriz decimal gracias a Pandas `.astype(float)`.
8. **Pipeline NLP Full-Stack**: Integrar Pandas `df["COL"]` enviando las celdas texto a la memoria Neuronal de `TextBlob.polarity`, para sobreescribir la matriz bajo diccionarios lógicos (Enojado/Feliz) pre-exportación en `.to_excel`.
9. **Infiltración Web Informática (Web Scraping)**: Ingeniería Inversa en el DOM del internet. Extraer los datos mediante etiquetas `.find_all("class")` y purificando la sintaxis asquerosa usando `iteracion.text`.

*(Este documento continuará su épico crecimiento conforme destruyas nuevos paradigmas de programación)*
