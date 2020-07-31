# Práctica 1

1. Se tienen los siguientes mapas de bits:
   a. 1110 0110 0001 1111 0001 1000 | 1 = 12 | 0 = 12
   b. 0011 1011 1100 0001 1111 1011 | 1 = 15 | 0 = 9

Si el tamaño de bloque es de 2 KB, ¿Cuánto espacio total está siendo consumido
por los procesos y cuánto espacio total está libre para asignar (suma de los
huecos) para cada uno de los casos?

a. 12*2 = 24 | 12*2 = 24
b. 15*2 = 30 | 9*2 = 18

¿Cuál es el espacio mayor espacio libre contiguo en cada casos?

a. 4*2=8
b. 5*2=10

2. Convierta las siguientes listas de distribución de memoria (Proceso/Hueco)
   en el mapa de bits respectivo. Muestre el resultado en hexadecimal.

   a.
   [ P | 0 | 3 ] - [ P | 3 | 2 ] - [ H | 5 | 3 ] - [ P | 8 | 4 ] -
   [ H | 12 | 5 ] - [ P | 17 | 3 ] - [ H | 20 | 2 ] - [ P | 22 | 3 ] -
   [ H | 25 | 4 ] - [ P | 29 | 3 ]

   b.
   [ H | 0 | 4 ] - [ P | 4 | 2 ] - [ P | 6 | 4 ] - [ H | 10 | 2 ] -
   [ P | 12 | 2 ] - [ H | 14 | 4 ] - [ P | 18 | 4 ] - [ P | 22 | 3 ] -
   [ H | 25 | 6 ] - [ P | 31 | 1 ]

   - Listas enlazadas

     - 11111000111100000111001110000111
     - F8F07387

     - 00001111110011000011111110000001
     - FCC3F81

3. En la siguiente tabla, la primera columna indica el tamaño total de memoria
   direccionable, la segunda columna indica el tamaño de bloque o unidad de
   asignación, calcule para cada fila el tamaño del mapa de bits
   correspondiente en bytes.

| Memoria |    Unidad |              Mapa de bits en bits |            Mapa de bits en bytes |
|--------:|----------:|----------------------------------:|---------------------------------:|
|    1 GB |      2 KB | (2^30)/(2^11)=>2^19=>2^9*1=512 KB |  (2^19)/(2^3)=>2^16=>2^6*1=64 KB |
|    4 GB |      4 KB |          (2^32)(*2^12)=>2^20=1 MB | (2^20)/(2^3)=>2^17=>2^7*1=128 KB |
|  512 MB | 512 bytes |           (2^29)/(2^9)=>2^20=1 MB | (2^20)/(2^3)=>2^17=>2^7*1=128 KB |
|    2 TB |      8 KB | (2^41)/(2^13)=>2^28=>2^8*1=256 MB |    (2^28)/(2^3)=>2^25=>2^5=32 MB |
|   16 TB |     16 KB |  (2^4*2^40)/(2^4*2^10)=>2^30=1 GB |        (2^30)/(2^3)=>2^27=128 MB                          |

4. Considere un sistema de intercambio en el que la memoria consiste en los
   siguientes tamaños de hueco, por orden de memoria: 15 KB, 6 KB, 18 KB, 24
   KB, 5 KB, 11 KB, 9 KB y 20 KB. ¿Cuál hueco se toma para las siguientes
   solicitudes de segmento sucesivas:


Primer ajuste?

> a(8 KB) b(14 KB) c(4 KB) d(6 KB)

| Estado | 1     | 2    | 3     | 4     | 5    | 6     | 7    | 8     |
|--------|-------|------|-------|-------|------|-------|------|-------|
| 0      | 15 KB | 6 KB | 18 KB | 24 KB | 5 KB | 11 KB | 9 KB | 20 KB |
|        | 8     |      | 14    |       |      |       |      |       |
| 1      | 7 KB  |      | 4 KB  |       |      |       |      |       |
|        | 4     | 6    |       |       |      |       |      |       |
| Final  | 3 KB  | 0    | 4 KB  |       |      |       |      |       |

Mejor ajuste?

> a(8 KB) b(14 KB) c(4 KB) d(6 KB)

| Estado | 15 KB | 6 KB | 18 KB | 24 KB | 5 KB | 11 KB | 9 KB | 20 KB |
|--------|-------|------|-------|-------|------|-------|------|-------|
| 0      | 14    | 6    |       |       | 4    |       | 8    |       |
| Final  | 1     | 0    | 18    | 24    | 1    | 11    | 1    | 20    |

Peor ajuste?

> a(8 KB) b(14 KB) c(4 KB) d(6 KB)

| Estado | 15 KB | 6 KB | 18 KB | 24 KB | 5 KB | 11 KB | 9 KB | 20 KB |
|--------|-------|------|-------|-------|------|-------|------|-------|
| 0      |       |      |       | 8     |      |       |      | 14    |
|        |       |      |       | 16    |      |       |      | 6     |
| 1      |       |      | 4     | 6     |      |       |      |       |
| Final  | 15    | 6    | 14    | 10    | 5    | 11    | 9    | 6     |

Siguiente ajuste?

> a(8 KB) b(14 KB) c(4 KB) d(6 KB)

| Estado | 15 KB | 6 KB | 18 KB | 24 KB | 5 KB | 11 KB | 9 KB | 20 KB |
|--------|-------|------|-------|-------|------|-------|------|-------|
| 0      | 8     |      | 14    |       |      |       |      |       |
|        |       |      | 4     |       |      |       |      |       |
| 1      |       |      | 4     | 6     |      |       |      |       |
| Final  | 7     | 6    |       | 18    | 5    | 11    | 9    | 20    |
