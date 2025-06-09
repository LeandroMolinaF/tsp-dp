# TSP con Programación Dinámica (Held‑Karp)

Este repositorio contiene un script en Python para resolver el Problema del Vendedor Viajero (TSP) usando programación dinámica. El script lee desde un archivo CSV las coordenadas de las ciudades y calcula la ruta óptima.

---

## Descripción del Proyecto

1. **Lectura de datos**: carga un CSV con columnas `x`, `y`, `ciudad`.
2. **Cálculo de distancias**: construye la matriz de distancias euclídeas entre todas las ciudades.
3. **Algoritmo TSP**: aplica Held‑Karp (bitmask + memoización) para obtener el costo mínimo y la ruta óptima.
4. **Salida**: muestra en consola el número de ciudades, costo del camino optimo, secuencia de ciudades y tiempo de ejecución.

---

## Requisitos

* Python 3.7 o superior
* Librerías:

  * `pandas`
  * `numpy`

Instala dependencias con:

```bash
pip install pandas numpy
```

---

## Estructura de Archivos

```plaintext
├── README.md
├── tsp-dp-path.py     # Script principal
├── ciudades_20.csv    # Ejemplo: 20 ciudades
├── ciudades_24.csv    # Ejemplo: 24 ciudades
└── ciudades_25.csv    # Ejemplo: 25 ciudades
```

---

## Uso

1. Clona el repositorio:

   ```bash
   git clone https://github.com/LeandroMolinaF/tsp-dp.git
   ```




2. Coloca tu archivo CSV (formato: `x,y,ciudad`) en la carpeta del proyecto.

3. Ejecuta el script:

    ```bash
python tsp_csv_dp.py
```

4. Cuando se solicite, ingresa la ruta al CSV

```
Ruta al CSV de ciudades: ciudades_20.csv

```

5. Observa los resultados en pantalla:

```plaintext
---- TSP ----
Número de ciudades: 20
Costo mínimo del tour: 123.45
Camino óptimo: Ciudad1 -> Ciudad5 -> ... -> Ciudad1
Tiempo de ejecución: 0.012345 segundos
```

---

## Formato del CSV de Entrada

* La primera fila debe ser el encabezado: `x,y,ciudad`.
* Cada fila contiene el nombre de la ciudad y sus coordenadas en `float`.

Ejemplo mínimo:

```csv
x,y,ciudad
10.0,5.0,A
20.0,15.0,B
5.0,12.0,C
```

---

## Detalle de Funciones

* `leer_ciudades_csv(ruta_csv)`:

  * Carga el CSV y retorna:

    * `ciudades`: lista de nombres.
    * `coords`: array de coordenadas.

* `calcular_matriz_distancias(coords)`:

  * Genera matriz `n×n` con distancias euclídeas.

* `tsp_dp(distancias)`:

  * Implementa Held‑Karp:

    * `dp[mask][pos]`: costo mínimo para visitar `mask` acabando en `pos`.
    * `parent[mask][pos]`: siguiente ciudad en el camino óptimo.
  * Retorna `(costo_mínimo, ruta_indices)`.

* `main()`:

  * Solicita ruta del CSV.
  * Ejecuta las funciones anteriores.
  * Mide y muestra tiempo de ejecución.

