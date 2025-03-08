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
Ejemplo de tabla con costos realistas: ya que dice que los costos de copy y replace son menos de hacer delete seguido de un insert. 
costo(Copy)=1,
costo(Replace)=2,
costo(Delete)=3,
costo(Insert)=4,
costo(Twiddle)=5,
costo(Kill)=0 (solo al final).


(Para efectos prácticos se usa el ejemplo proporcionado)
|   | "" | a    | l   | t   | r   | u   | i   | s   | t   | i   | c   |
|---|----|----  |---- |---- |---- |---- |---- |---- |---- |---- |---- |
| ""| 0   |  4  |  8  | 12  | 16  | 20  | 24  | 28  | 32  | 36  | 40  |    
| a | 3   |  0  |  4  |  8  | 12  | 16  | 20  | 24  | 28  | 32  | 36  |    
| l | 6   |  3  |  0  |  4  |  8  | 12  | 16  | 20  | 24  | 28  | 32  |    
| g | 9   |  6  |  3  |  2  |  6  | 10  | 14  | 18  | 22  | 26  | 30  |    
| o | 12  |  9  |  6  |  5  |  6  | 10  | 14  | 18  | 22  | 26  | 30  |    
| r | 15  | 12  |  9  |  8  |  5  |  9  | 13  | 17  | 21  | 25  | 29  |    
| i | 18  | 15  | 12  | 11  |  8  |  9  |  9  | 13  | 17  | 21  | 25  |    
| t | 21  | 18  | 15  | 12  | 11  | 12  | 12  | 13  | 13  | 17  | 21  |    
| h | 24  | 21  | 18  | 15  | 14  | 13  | 13  | 14  | 14  | 14  | 18  |    
| m | 27  | 24  | 21  | 18  | 17  | 16  | 16  | 17  | 17  | 17  | 14  |   



## Ecuacion recurrente:

T[i][j]=min⎩

⎧​T[i−1][j−1]+costo(Copy), si X[i]=Y[j],
T[i−1][j−1]+costo(Replace) si X[i]!=Y[j],
T[i−1][j]+costo(Delete),
T[i][j−1]+costo(Insert),
T[i−2][j−2]+costo(Twiddle)​si i≥2,j≥2,X[i−1]=Y[j],X[i]=Y[j−1].​

Ajuste final para Kill:
Costo total=min⁡(T[m][n],min⁡0≤k≤m(T[k][n]+costo(Kill))).
Explicación del ejemplo (algorithm → altruistic)
Twiddle en "th":

X[7..8]="th", Y[7..8]="ht".

Costo: T[6][6]+5=9+5=14.

Kill al final:
Costo total = T[9][10]=14 (sin necesidad de Kill, ya que i=m+1 y j=n).

Secuencia óptima:
Copy (a), Copy (I), Replace (g→t), Delete (o), Copy (r), Insert (u), Insert (i), Insert (s), Twiddle (th→ht), Insert (c).