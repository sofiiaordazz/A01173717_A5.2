# Actividad 5.2 - Ejercicio de Programaci\u00f3n 2 y An\u00e1lisis Est\u00e1tico
# Sof\u00eda Ordaz L\u00f3pez - A01173717

Repositorio con el programa `computeSales.py` desarrollado en Python que calcula el costo total de ventas a partir de un cat\u00e1logo de productos y registros de ventas en formato JSON. El programa sigue el est\u00e1ndar de codificaci\u00f3n **PEP-8** y fue validado con **flake8** (cero errores) y **pylint** obteniendo una calificaci\u00f3n de **10.00/10**.

---

## Estructura del repositorio

```
A01173717_A5.2/
\u251c\u2500\u2500 computeSales.py
\u251c\u2500\u2500 A5.2 Archivos de Apoyo/
\u2502   \u251c\u2500\u2500 Results.txt               (resultados esperados)
\u2502   \u251c\u2500\u2500 TC1/
\u2502   \u2502   \u251c\u2500\u2500 TC1.ProductList.json  (cat\u00e1logo de 50 productos)
\u2502   \u2502   \u2514\u2500\u2500 TC1.Sales.json        (ventas del caso 1)
\u2502   \u251c\u2500\u2500 TC2/
\u2502   \u2502   \u2514\u2500\u2500 TC2.Sales.json        (ventas del caso 2)
\u2502   \u2514\u2500\u2500 TC3/
\u2502       \u2514\u2500\u2500 TC3.Sales.json        (ventas del caso 3)
\u251c\u2500\u2500 evidence/
\u2502   \u251c\u2500\u2500 TC1_output.txt
\u2502   \u251c\u2500\u2500 TC2_output.txt
\u2502   \u251c\u2500\u2500 TC3_output.txt
\u2502   \u2514\u2500\u2500 flake8_output.txt
\u2514\u2500\u2500 README.md
```

---

## Ejecuci\u00f3n

El programa se ejecuta desde la l\u00ednea de comandos recibiendo dos archivos JSON como argumentos:

```bash
python computeSales.py priceCatalogue.json salesRecord.json
```

Los resultados se imprimen en consola y se guardan autom\u00e1ticamente en un archivo `SalesResults.txt`.

---

## Descripci\u00f3n del programa - Compute Sales (`computeSales.py`)

### Funcionalidad

El programa lee un cat\u00e1logo de productos con precios y un registro de ventas, calcula el costo total de todas las ventas y genera un reporte.

| Funcionalidad | Detalle |
|---|---|
| **Lectura de datos** | Carga dos archivos JSON (cat\u00e1logo y ventas) |
| **C\u00e1lculo de costos** | Para cada venta: precio del producto \u00d7 cantidad |
| **Manejo de errores** | Productos no encontrados en el cat\u00e1logo se reportan en consola y se omiten |
| **Reporte** | Muestra total por venta y gran total en pantalla y en archivo |
| **Tiempo de ejecuci\u00f3n** | Se incluye al final del reporte |

### Manejo de datos inv\u00e1lidos

El programa maneja los siguientes casos de datos inv\u00e1lidos sin detenerse:

- **Producto no encontrado en el cat\u00e1logo**: Se muestra un error en consola y se omite del c\u00e1lculo.
- **Cantidad no num\u00e9rica**: Se muestra un error en consola y se omite del c\u00e1lculo.
- **Cantidades negativas**: Se procesan como devoluciones (restan del total).
- **Archivos inv\u00e1lidos o no encontrados**: Se muestra un error y el programa termina con c\u00f3digo de salida 1.

---

## Casos de prueba ejecutados

Se ejecutaron **3 casos de prueba** con los archivos proporcionados. Los tres utilizan el mismo cat\u00e1logo de productos (`TC1.ProductList.json`).

### TC1 - Caso base (datos v\u00e1lidos)

Todas las ventas tienen productos existentes en el cat\u00e1logo y cantidades positivas.

```
$ python3 computeSales.py TC1.ProductList.json TC1.Sales.json
========================================
SALES REPORT
========================================
  SALE 1     (3 items)  $83.39
  SALE 2     (2 items)  $67.57
  SALE 3     (3 items)  $144.74
  SALE 4     (3 items)  $87.23
  SALE 5     (3 items)  $94.33
  SALE 6     (8 items)  $239.04
  SALE 7     (5 items)  $182.11
  SALE 8     (7 items)  $407.30
  SALE 9     (6 items)  $851.43
  SALE 10    (6 items)  $324.72
========================================
GRAND TOTAL:  $2481.86
Time elapsed: 0.0003 seconds
========================================
```

**Resultado esperado: $2481.86** | **Resultado obtenido: $2481.86**

### TC2 - Cantidades negativas (devoluciones)

Incluye registros con cantidades negativas que representan devoluciones:
- `Fresh blueberries`: Quantity -35
- `Green smoothie`: Quantity -123

```
$ python3 computeSales.py TC1.ProductList.json TC2.Sales.json
========================================
SALES REPORT
========================================
  SALE 1     (3 items)  $4969.25
  SALE 2     (2 items)  $6352.61
  ...
  SALE 10    (6 items)  $91420.61
========================================
GRAND TOTAL:  $166568.23
Time elapsed: 0.0004 seconds
========================================
```

**Resultado esperado: $166568.23** | **Resultado obtenido: $166568.23**

### TC3 - Productos no encontrados + cantidades negativas

Incluye productos que no existen en el cat\u00e1logo (`Elotes`, `Frijoles`) y cantidades negativas. El programa reporta los errores y contin\u00faa la ejecuci\u00f3n.

```
$ python3 computeSales.py TC1.ProductList.json TC3.Sales.json
  Error: Product 'Elotes' is not in the catalogue. Skipping.
  Error: Product 'Frijoles' is not in the catalogue. Skipping.
========================================
SALES REPORT
========================================
  SALE 1     (3 items)  $4969.25
  SALE 2     (2 items)  $6352.61
  ...
  SALE 10    (6 items)  $92155.96
========================================
GRAND TOTAL:  $165235.37
Time elapsed: 0.0003 seconds
========================================
```

**Resultado esperado: $165235.37** | **Resultado obtenido: $165235.37**

### Resumen de resultados

| Caso de prueba | Total esperado | Total obtenido | Estado |
|---|---|---|---|
| TC1 | $2,481.86 | $2,481.86 | PASS |
| TC2 | $166,568.23 | $166,568.23 | PASS |
| TC3 | $165,235.37 | $165,235.37 | PASS |

---

## Cumplimiento del est\u00e1ndar PEP-8

### An\u00e1lisis con flake8

Se ejecut\u00f3 flake8 sobre el programa y no se encontraron errores:

```
$ flake8 computeSales.py
(No errors found)
```

### An\u00e1lisis con pylint

Se ejecut\u00f3 pylint sobre el programa y se obtuvo la calificaci\u00f3n m\u00e1xima:

```
$ pylint computeSales.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10
```

### Resumen de an\u00e1lisis est\u00e1tico

| Herramienta | Resultado |
|---|---|
| **flake8** | 0 errores |
| **pylint** | 10.00/10 |

Esto garantiza que el c\u00f3digo cumple con las convenciones de estilo de Python definidas en PEP-8, incluyendo: nombres de variables y funciones en `snake_case`, docstrings descriptivos, manejo adecuado de imports, longitud de l\u00ednea controlada y estructura limpia del c\u00f3digo.
