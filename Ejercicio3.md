# Ejercicio 3

Se debe transformar X[1:m] en Y[1:n], teniendo una secuencia óptima de operaciones. 
Identificamos dp[i][j] como el costo mínimo pra transformar los primeros u caracteres de X en los primeros j caracteres de Y.

Identificamos las siguientes operaciones con sus costos:

1. Copy: dp[i][j] = dp[i - 1][j - 1] + costo
2. Replace: dp[i][j] = dpi[i - 1][j - 1] + costo
3. Delete: dp[i][j] = dp[i - 1][j] + costo
4. Insert: dp[i][j] = dp[i][j - 1] + costo
5. Twiddle: dp[i][j] = dp[i - 2][j - 2] + costo
6. Kill: dp[i][j] = dp[m][n] + costo

## Condiciones iniciales:

- dp[0][j] = j * costo --> Si X está vacío, solo se inertan caracteres de Y.
- dp[i][0] = i x costo --> Si Y esta vacío, solo se eliminan carcateres de X.

## Sucesos antes de aplicar la operación:
1. Aplicando Copy: estado anterior de dp[i-1][j-1], debido al procesamiento hasta i - 1 y j - 1.
2. Aplicando Replace: se hace el replace indicando un estado anterior de dp[i-1][i-j]
3. Aplicando Delete: Como se procesa hasta la subcadena en X i - 1 y Y queda igual tenemos: dp[i-1][j]
4. Aplicando Insert: el estado anterior seria dp[i][j-1], se procesa la subcadena X hasta i y Y hasta j - 1.
5. Aplicando Twiddle: El estado anterior seria dp[i-2][j-2], procesando X hasta i - 2 y Y hasta j - 2.
6. Aplicando Kill: Se tendría que haber procesado toda la subcadena anterior, quedando como dp[m+1][j]

## Tabla T

(Para efectos prácticos se usa el ejemplo proporcionado)
|   | "" | a  | l  | t  | r  | u  | i  | s  | t  | i  | c  |
|---|----|----|----|----|----|----|----|----|----|----|----|
| ""| 0  |  1 | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 |    
| a | 1  | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |    
| l | 2  | 1  | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  |    
| g | 3  | 2  | 1  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  |    
| o | 4  | 3  | 2  | 2  | 2  | 3  | 4  | 5  | 6  | 7  | 8  |    
| r | 5  | 4  | 3  | 3  | 2  | 3  | 4  | 5  | 6  | 7  | 8  |    
| i | 6  | 5  | 4  | 4  | 3  | 3  | 3  | 4  | 5  | 6  | 7  |    
| t | 7  | 6  | 5  | 4  | 4  | 4  | 4  | 4  | 4  | 5  | 6  |    
| h | 8  | 7  | 6  | 5  | 5  | 5  | 5  | 5  | 5  | 5  | 6  |    
| m | 9  | 8  | 7  | 6  | 6  | 6  | 6  | 6  | 6  | 6  | 6  |   
