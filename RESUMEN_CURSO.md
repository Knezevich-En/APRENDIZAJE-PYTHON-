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

## 7. Manejo de Archivos y Automatización (`OS` e `I/O`)
> **Caso de uso Real:** Mover PDFs masivamente, crear carpetas automáticas (`os.makedirs`) o guardar Logs persistentes.

```python
import os

# CREAR CARPETAS ("exist_ok" evita que el servidor explote si la carpeta ya existe)
os.makedirs("REPORTES_MENSUALES", exist_ok=True)

# MODO DE ESCRITURA BÁSICA DE ARCHIVOS
with open("registros.txt", "w") as archivo: # "w" Borra y crea, "a" añade sin borrar
    archivo.write("Guardar info en disco duro\n") 
    
# MODO LECTURA DE MATRICES (".readlines")
with open("dataset.txt", "r") as archivo:
    # readlines convierte cada renglón del bloc de notas en un índice de una Lista Gigante 
    # para recorrer con tu For-Loop directamente.
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
# que vino contaminada como texto se vuelva decimal matemático puro para graficar.
df["PRECIOS_PURA"] = df["PRECIOS_SUCIOS"].astype(float)

plt.bar(df["A"], df["PRECIOS_PURA"])
plt.savefig("reporte.png") # Va ANTES de show() o se guarda la foto en blanco!
plt.show() 
```

---

## 9. Programación Orientada a Objetos (`POO`)
> **Caso de uso Real:** En lugar de hacer docenas de variables esparcidas (`saldo1`, `saldo2`), empacas la biología completa del objeto bajo una plantilla maestra (`class`) que instanciarás cientos de veces para representar Clientes vivos o Cuentas Bancarias con memoria de acumulación.

```python
# 1. Definición del Plano (Siempre en CamelCase: "CuentaBancaria")
class VehiculoDron:
    
    # 2. El Constructor (__init__): Corre automáticamente al "Nacer" el objeto.
    # La palabra 'self' es OBLIGATORIA. Representa al objeto en sí mismo ("Yo").
    def __init__(self, bateria_inicial):
        self.encendido = False
        self.bateria = bateria_inicial # Memoria interna
        
    # 3. Los Comportamientos (Métodos): Funciones atadas directamente a las acciones del objeto.
    def despegar(self):
        if self.bateria > 10:
            self.encendido = True
            self.bateria -= 10 # Las matemáticas de memoria acumulativa
            print(f"Despegando... Batería restante: {self.bateria}%")
        else:
            print("Batería insuficiente. Recarga requerida.")

# 4. Uso en el Mundo Real (Instanciar)
# Creamos el clon (el Objeto) y le inyectamos 100 de batería al nacer.
mi_dron = VehiculoDron(100)

mi_dron.despegar() # -> Imprime: Despegando... Batería restante: 90%
mi_dron.despegar() # -> Imprime: Despegando... Batería restante: 80%

print(mi_dron.bateria) # Al leer su corazón, dice 80 directamente. Tiene memoria perpetua.
```

---

## 10. Descubrimientos Proactivos (¡La Armería del Datos!)

**1. Limpieza Cruda (`.strip()`, `.upper()`, `.lower()`)**
> Desinfectar entradas de teclado para que no explote tu validación If.
```python
entrada = "   sALiR  "
if entrada.strip().upper() == "SALIR":
    print("Cerrando sistema exitosamente.")
```

**2. Ignorar Cabeceras por Patrón (`.startswith(...)`)**
> Usado al minar archivos TXT llenos de asteriscos. 
```python
for linea in lineas_del_archivo:
    if linea.startswith("*"): continue # ¡Lo ignora!
    print("Linea de tabla útil:", linea)
```

**3. El Machete de Frases (`.split("|")`)**
> Imprescindible para sistemas COBOL o viejos. Corta un texto masivo en base a un ancla dejándote una lista.
```python
datos = "| 001 | Arturo |".split("|") 
```

**4. Arrancar Cabezas y Colas (`.pop()`)**
> Sencillamente destruye la posición X de una lista generada con márgenes corruptos.
```python
precios = ["EL TITULO BASURA DEL EXCEL", 50, 40]
precios.pop(0) # Apunta y elimina. Cae la basura.
```

**5. El Acumulador o Contador (`+=`)**
> Darle memoria creciente o decreciente a una variable orgánica.
```python
precio_total = 0
precio_total += 50.50 
```

**6. El Dios del Tiempo (`datetime` y `.strftime()`)**
> Fábrica de nombres de archivos inquebrantables.
```python
from datetime import datetime
# Formato File-Friendly, jamas uses DOS PUNTOS en nombres de windows!!
hora_limpia = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
ruta = f"C:\\reportes\\log_{hora_limpia}.txt"
```

**7. Inteligencia Artificial NLP (`TextBlob`)**
> Obtener métricas flotantes entre -1.0 y 1.0 para analizar psicología y priorizar tickets de soporte.
```python
from textblob import TextBlob
matematica_emocion = TextBlob("I absolutely hate this update").sentiment.polarity 
# Arroja un número tipo -0.80.
```

**8. Web Scraping Pura (`BeautifulSoup` y `.text`)**
> La diferencia brutal entre `.text` de Response (Todo el HTML sucio de la web) vs `.text` aislando la carne útil en ciclos de Extracción.
```python
import requests
from bs4 import BeautifulSoup
respuesta = requests.get("http://sitio.com")
sabueso_scrap = BeautifulSoup(respuesta.text, "html.parser") # HTML Sucio

textos_crudos = sabueso_scrap.find_all("span", class_="text") 
for item in textos_crudos:
    print(item.text) # Revela el diamante destripado (La carne)
```

**9. Desglose de APIs Remotas (`.json()`)**
> Traducir la respuesta de un servidor de internet directamente a Diccionarios Nativos de Python estructurados.
```python
respuesta = requests.get("http://api.com/usuario")
print(respuesta.json()["nombre"])
```

**10. La Trampa Universal: `CSV Injection`**
> Cuando transfieres textos humanos a Excel `.csv`, *debes* englobarlos en comillas dobles `"..."`, de lo contrario Pandas sentirá que cualquier coma de puntuación interna es el activador de una "Siguiente Columna" destruyendo las dimensiones.

---

## 🏆 11. Tu Historial de Retos Operativos (`CERTIFICACIÓN MÁSTER LOCAL`)

1. **API Anidada**: Extracción JSON en servidor externo.
2. **Casino Infalible**: Menú robusto blindado con Excepciones de teclado.
3. **Generador Masivo**: OS path y automatización de lotes de carpetas.
4. **Data Analytics V0**: Exportación estática gráfica mediante Matplotlib y Pandas.
5. **Generador Tokens**: Algoritmo random de ciberseguridad con iteradores aditivos y constructivos (+=).
6. **Descuento Modular**: Capsulas `def` infalibles a pruebas de typo's.
7. **Pipeline de Datos Legado**: Escaneo vectorial, ignorado de headers, fragmentos (`split`) y limpieza con `pop`.
8. **Analista Sentimental NLP**: Uso de cerebro local `TextBlob` interactivo clasificador de inputs infinitos.
9. **Super-Ingeniería Pandas-AI**: Absorción de columnas CSV sin coma-injection, integración profunda del cerebro TextBlob a los registros base y rearme y anexión de nuevos Dataframes clasificados a idiomas humanos mediante Excel.
10. **Extractor Web (Scraping)**: Engaño de puertos HTTP e ingeniería inversa al DOM usando analizadores HTML con recolección de Listas y limpieza `span.text`.

*(El manual evoluciona constantemente)*
