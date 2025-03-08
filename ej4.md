# Ejercicio 4

Dado el siguiente grafo dirigido y ponderado:

V={A,B,C,D,E}

E={(A,B,6),(A,C,7),(B,C,8),(B,D,5),(B,E,−4),(C,D,−3),(C,E,9),(D,B,−2),(E,D,7)}

Tomamos el nodo A como el vértice de origen (s=A).

#### Paso 1: Inicialización

Se inicializan las distancias:

d[A]= 0, d[B]= inf, d[C]= inf, d[D]= inf, d[E]= inf

El arreglo π de predecesores se inicializa con valores nulos.

#### Paso 2: Relajación de todas las aristas ∣V∣−1=4 veces

Iteramos sobre todas las aristas durante 4 iteraciones.

Estado al final de la iteración 1:

d[A]= 0, d[B]= 2, d[C]= 7, d[D]= 4, d[E]= 2

Estado final tras iteraciones restantes:

d[A]= 0, d[B]= 2, d[C]= 7, d[D]= 4, d[E]= 2

Después de las 4 iteraciones, el arreglo d contiene las distancias más cortas desde A a cada nodo.


### Subestructura Óptima y Subproblemas Traslapados

La subestructura óptima del problema se debe a que cualquier camino más corto hacia un nodo v se construye a partir de caminos más cortos hacia sus predecesores u, es decir:

d[v] = min(d[v], d[u] + w(u,v))

Este principio es similar al de la programación dinámica, ya que cada iteración refina la solución basándose en soluciones anteriores.

Los subproblemas traslapados aparecen porque se reutilizan las soluciones parciales calculadas en iteraciones previas para actualizar las distancias en iteraciones posteriores.

### Recurrencia del Algoritmo

La ecuación de recurrencia que calcula la solución óptima es:

d_k(v) = min para (u, v) pertenecen a E, (d_(k-1)(u) + w(u,v))

donde d_k(v) representa la distancia mínima a v después de k iteraciones.
