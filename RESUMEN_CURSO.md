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
for correo in lista_correos:
    enviar(correo) 

while True:
    texto = input("Escriba SALIR: ")
    if texto == "SALIR": break
```

---

## 5. El Blindaje: Errores (`ERRORES`)
> **Caso de uso Real:** Cajero de interfaz a prueba de caídas.

```python
try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: Ingrese solo números.")
except KeyboardInterrupt:
    print("\nEl usuario pulsó Ctrl+C.")
```

---

## 6. Funciones (`def`)
> **Caso de uso Real:** Empaquetar bloques lógicos (como tu Calculadora de Descuentos VIP) para reutilizarlos mil veces.

```python
def aplicar_descuento(precio):
    total = precio * 0.80
    return total # Devuelve la materia procesada

resultado = aplicar_descuento(500)
```

---

## 7. Manejo de Archivos Físicos (`ARCHIVOS`)
> **Caso de uso Real:** Escribir Logs persistentes.

```python
with open("registros.txt", "w") as archivo: # "w" Borra y crea, "a" Añade.
    archivo.write("Guardar info en disco duro\n") 
```

---

## 8. Data Science (`PANDAS` / `MATPLOTLIB`)
> **Caso de uso Real:** Cruzar datos y exportar para analistas y PowerBI.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos.csv") 
df["nueva_col"] = lista_calculada
plt.bar(df["A"], df["B"])
plt.savefig("reporte.png") # Va ANTES de show()
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
for linea in archivo.readlines():
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
> Cuando extraes información e infaliblemente te genera posiciones vacías o headers, sencillamente los destruyes usando el índice antes de hacer cálculos.
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
cadena_pass += "Z" # También sirve para pegar texto orgánicamente!
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
comentario_cliente = "I absolutely hate this new update"
ia = TextBlob(comentario_cliente)
matematica_emocion = ia.sentiment.polarity 
# matemática_emocion arroja un número -0.80.
```

**8. Web Scraping (`BeautifulSoup`)**
> Robo y minería automática de código fuente web ignorando la interfaz gráfica para alimentar Excel y evadir copiado manual.
```python
import requests
from bs4 import BeautifulSoup
respuesta = requests.get("http://sitio.com")
sabueso_scrap = BeautifulSoup(respuesta.text, "html.parser")
# Caza HTML
textos = sabueso_scrap.find_all("div", class_="titulo_precio") 
for item in textos:
    print(item.text) # Revela el diamante
```

**9. La Trampa Universal: `CSV Injection`**
> Cuando transfieres tus limpiados datos a comas `.csv`, *debes* recordar inyectarle un marco de `"..."` comillas dobles, o de otra forma Pandas al leerlo sentirá que esa coma natural de la persona significa que quieres dividir esa palabra en la celda derecha.
```python
# Así se deben guardar las matrices si el texto contiene comas de puntuación:
# 101, "Comida asombrosa, deliciosa"
# 102, "Mala atención"
```

*(Este documento continuará su épico crecimiento)*
