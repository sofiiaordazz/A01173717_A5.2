# Actividad 5.2 - Ejercicio de Programación 2 y Análisis Estático
# Sofía Ordaz López - A01173717

Repositorio con el programa `computeSales.py` desarrollado en Python que calcula el costo total de ventas a partir de un catálogo de productos y registros de ventas en formato JSON. El programa sigue el estándar de codificación **PEP-8** y fue validado con **flake8** (cero errores) y **pylint** obteniendo una calificación de **10.00/10**.

---

## Estructura del repositorio

```
A01173717_A5.2/
├── computeSales.py
├── A5.2 Archivos de Apoyo/
│   ├── Results.txt               (resultados esperados)
│   ├── TC1/
│   │   ├── TC1.ProductList.json  (catálogo de 50 productos)
│   │   └── TC1.Sales.json        (ventas del caso 1)
│   ├── TC2/
│   │   └── TC2.Sales.json        (ventas del caso 2)
│   └── TC3/
│       └── TC3.Sales.json        (ventas del caso 3)
├── evidence/
│   ├── TC1_output.txt
│   ├── TC2_output.txt
│   ├── TC3_output.txt
│   └── flake8_output.txt
└── README.md
```

---

## Ejecución

El programa se ejecuta desde la línea de comandos recibiendo dos archivos JSON como argumentos:

```bash
python computeSales.py priceCatalogue.json salesRecord.json
```

Los resultados se imprimen en consola y se guardan automáticamente en un archivo `SalesResults.txt`.

---

## Descripción del programa - Compute Sales (`computeSales.py`)

### Funcionalidad

El programa lee un catálogo de productos con precios y un registro de ventas, calcula el costo total de todas las ventas y genera un reporte.

| Funcionalidad | Detalle |
|---|---|
| **Lectura de datos** | Carga dos archivos JSON (catálogo y ventas) |
| **Cálculo de costos** | Para cada venta: precio del producto x cantidad |
| **Manejo de errores** | Productos no encontrados en el catálogo se reportan en consola y se omiten |
| **Reporte** | Muestra total por venta y gran total en pantalla y en archivo |
| **Tiempo de ejecución** | Se incluye al final del reporte |

### Manejo de datos inválidos

El programa maneja los siguientes casos de datos inválidos sin detenerse:

- **Producto no encontrado en el catálogo**: Se muestra un error en consola y se omite del cálculo.
- **Cantidad no numérica**: Se muestra un error en consola y se omite del cálculo.
- **Cantidades negativas**: Se procesan como devoluciones (restan del total).
- **Archivos inválidos o no encontrados**: Se muestra un error y el programa termina con código de salida 1.

---

## Casos de prueba ejecutados

Se ejecutaron **3 casos de prueba** con los archivos proporcionados. Los tres utilizan el mismo catálogo de productos (`TC1.ProductList.json`).

### TC1 - Caso base (datos válidos)

Todas las ventas tienen productos existentes en el catálogo y cantidades positivas.

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

Incluye productos que no existen en el catálogo (`Elotes`, `Frijoles`) y cantidades negativas. El programa reporta los errores y continúa la ejecución.

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

## Cumplimiento del estándar PEP-8

### Análisis con flake8

Se ejecutó flake8 sobre el programa y no se encontraron errores:

```
$ flake8 computeSales.py
(No errors found)
```

### Análisis con pylint

Se ejecutó pylint sobre el programa y se obtuvo la calificación máxima:

```
$ pylint computeSales.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10
```

### Resumen de análisis estático

| Herramienta | Resultado |
|---|---|
| **flake8** | 0 errores |
| **pylint** | 10.00/10 |

Esto garantiza que el código cumple con las convenciones de estilo de Python definidas en PEP-8, incluyendo: nombres de variables y funciones en `snake_case`, docstrings descriptivos, manejo adecuado de imports, longitud de línea controlada y estructura limpia del código.
