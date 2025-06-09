import pandas as pd
import numpy as np
import math
import time

# Leer ciudades y coordenadas desde CSV
def leer_ciudades_csv(ruta_csv):
    df = pd.read_csv(ruta_csv)
    ciudades = df['ciudad'].tolist()
    coords = df[['x', 'y']].values
    return ciudades, coords

# Calcular matriz de distancias a partir de las coordenadas
def calcular_matriz_distancias(coords):
    n = len(coords)
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist[i, j] = math.hypot(coords[i][0] - coords[j][0],
                                     coords[i][1] - coords[j][1])
    return dist

# TSP 
def tsp_dp(distancias):
    n = len(distancias)
    ALL_VISITED = (1 << n) - 1
    INF = math.inf
    dp = [[None] * n for _ in range(1 << n)]
    parent = [[None] * n for _ in range(1 << n)]

    def visit(mask, pos):
        if mask == ALL_VISITED:
            return distancias[pos][0]
        if dp[mask][pos] is not None:
            return dp[mask][pos]

        best_cost = INF
        best_next = None
        for city in range(n):
            if not (mask & (1 << city)):
                cost = distancias[pos][city] + visit(mask | (1 << city), city)
                if cost < best_cost:
                    best_cost = cost
                    best_next = city
        dp[mask][pos] = best_cost
        parent[mask][pos] = best_next
        return best_cost

   
    min_cost = visit(1, 0)

    
    path = [0]
    mask = 1
    pos = 0
    while mask != ALL_VISITED:
        nxt = parent[mask][pos]
        path.append(nxt)
        mask |= (1 << nxt)
        pos = nxt
    path.append(0)

    return min_cost, path


def main():
    ruta_csv = input("Ruta al CSV de ciudades (x,y,ciudad): ").strip()
    ciudades, coords = leer_ciudades_csv(ruta_csv)
    dist_matrix = calcular_matriz_distancias(coords)

    start = time.perf_counter()
    cost, camino = tsp_dp(dist_matrix)
    elapsed = time.perf_counter() - start

    print("\n---- TSP ----")
    print(f"Número de ciudades: {len(ciudades)}")
    print(f"Costo mínimo: {cost:.2f}")
    print("Camino óptimo:", " -> ".join(ciudades[i] for i in camino))
    print(f"Tiempo de ejecución: {elapsed:.6f} segundos")

if __name__ == "__main__":
    main()
