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

## 8. Data Science y Estadística (`PANDAS` / `MATPLOTLIB`)
> **Caso de uso Real:** Cruzar datos, limpiar basura y exportar reportes para gerencia y PowerBI.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos.csv") 

# `.astype(float)`: Herramienta de oro post-lectura. Obliga a que una columna
# que vino contaminada como texto se vuelva decimal matemático puro para graficar.
df["PRECIOS"] = df["PRECIOS_SUCIOS"].astype(float)

# Exportación (.to_excel / .to_csv)
# Guardamos los resultados finales puros (index=False evita que se imprima la enumeración inútil).
df.to_excel("reporte_financiero_limpio.xlsx", index=False)

# ----------------- INTELIGENCIA DE NEGOCIOS -----------------

# Agrupaciones (Group By y Aggregation): Sumatoria y Estadísticas Masivas
# Si tienes una base gigante y quieres saber cuánto vendió cada departamento, 
# se usa groupby en la columna meta y se le exige procesar (.agg / .sum).
resumen = df.groupby(['CATEGORIA']).agg({'PRECIO': 'sum'})
# También puedes aplicar la versión express:
# resumen = df.groupby("CATEGORIA")["PRECIO"].sum()

# Gráficos (Data Visualization) de la Agrupación (Se saca desde en index)
plt.bar(resumen.index, resumen["PRECIO"])
plt.title("Ventas por Categoría") # Adornar
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

**2. Ignorar Cabeceras por Patrón (`.startswith(...)`)**
> Usado al minar archivos TXT llenos de asteriscos. 
```python
for linea in lineas_del_archivo:
    if linea.startswith("*"): continue # ¡Lo ignora!
    print("Linea de tabla útil:", linea)
```

**3. El Machete de Frases (`.split("|")`)**
> Corta un texto masivo en base a un ancla dejándote una lista.

**4. Arrancar Cabezas y Colas (`.pop()`)**
> Sencillamente destruye la posición X de una lista generada con márgenes corruptos.

**5. El Acumulador o Contador (`+=`)**
> Darle memoria creciente o decreciente a una variable orgánica.

**6. El Dios del Tiempo (`datetime` y `.strftime()`)**
> Fábrica de nombres de archivos inquebrantables (`"%Y-%m-%d"`).

**7. Inteligencia Artificial NLP (`TextBlob`)**
> Obtener métricas flotantes entre -1.0 y 1.0 para analizar psicología.

**8. Web Scraping Pura (`BeautifulSoup` y `.text`)**
> Diferencia brutal entre HTML sucio vs extraer la carne limpia con `.text`.

**9. Desglose de APIs Remotas (`.json()`)**
> Traducir la respuesta gigante de internet a Python.

**10. La Trampa Universal: `CSV Injection`**
> Envolver frases humanas en Excel con dobles comillas `"..."` para no distorsionar las comas naturales.

**11. Destructor de Vacíos y Clones (`.dropna()` / `.drop_duplicates()`)**
> Purgar filas que tienen casillas obligatorias vacías o registros repetidos por error humano en CSVs.
```python
# Borra la fila entera si en la columna ID no hay texto
df_limpio = df.dropna(subset=['ID_VENTA']) 
# Destruye filas exactamente iguales
df_limpio = df_limpio.drop_duplicates()
```

**12. Cirugía de Strings en Tablas (`.str.replace()` y el misterio de Regex)**
> Pandas requiere declarar el poder `.str` antes de alterar letras. 
> IMPORTANTE: Al reemplazar cosas raras como símbolos de Dólar (`$`), añadir el `regex=False` es obligatorio para evitar que Pandas intente invocar el lenguaje hack matemático de "Expresiones Regulares" y force al sistema a simplemente leer tu símbolo de dólar como una inofensiva letra a borrar.
```python
# El regex=False es tu escudo protector para símbolos extraños de facturación.
df['PRECIO'] = df['PRECIO'].str.replace('$', '', regex=False)

# Si una celda está vacía (NaN), le pone "DESCONOCIMIENTO".
df['PRODUCTO'] = df['PRODUCTO'].fillna('PRODUCTO_DESCONOCIDO')
```

---

## 🏆 11. Tu Historial de Retos Operativos (`CERTIFICACIÓN MÁSTER LOCAL`)

1. **API Anidada**: Extracción JSON en servidor.
2. **Casino Infalible**: Menú interactivo `while True` protegido.
3. **Generador Masivo**: OS path y automatización de archivos.
4. **Data Analytics V0**: Fabricación de DF e inyección de Gráficos PNG.
5. **Generador Tokens**: Algoritmo `random.choice`.
6. **Descuento Modular**: Capsulas `def` universales.
7. **Pipeline de Datos Legado**: Escaneo vectorial, ignorado de headers, `.split("|")` y cast flote.
8. **Analista NLP**: Clasificación Sentimental mediante TextBlob.
9. **Super-Ingeniería Pandas-AI**: Recombinando Sentimientos IA en nuevas series Excel evadiendo inyecciones de Coma.
10. **Extractor Hacker (Scraping)**: Ingeniería inversa a los `span.text`.
11. **Super-Auditor Contable**: Masterización de `dropna`, limpieza total de precios con bypass de `regex=False`, con recolección global y `.groupby().agg`.

*(El manual evoluciona constantemente)*
