# Esta es la solucion del rod cutting problem utilizando la estrategia de bottom up.
# esta inspirado en el algoritmo visto en canvas.

def rod_cutting_solution(n, prices):
    dp = [0] * (n+1)

    # para luego poder guardar los valores de longitud de los cortes
    cuts = [0] * (n+1)  
    for i in range(1, n+1):
        max_value = -float('inf')
        for j in range(1, i+1):
            if prices[j] + dp[i-j] > max_value:
                max_value = prices[j] + dp[i-j]

                #aca ya se guarda el valor de la loongitud del corte dentro del arreglo 
                cuts[i] = j
        dp[i] = max_value

    # Reconstruir la solución
    solution = []
    length = n
    while length > 0:
        solution.append(cuts[length])
        length -= cuts[length]
    return dp[n], solution


# Precios para longitudes 1, 2, 3, 4
# tenemos un 0 al inicio solo por fines de simplicidad, el 0 no se usa y es mas que todo para luego usar el indice del arreglo
# como el largo de la varilla y el valor en la posicion el precio por el que se vende el corte.

prices = [0, 1, 5, 8, 9]  
n = 4
max_value, solution = rod_cutting_solution(n, prices)
print(f"Valor máximo: {max_value}")
print(f"Cortes óptimos: {solution}")