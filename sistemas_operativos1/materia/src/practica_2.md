# Práctica 2

> No están todos los ejercicios, solo uno de cada algoritmo

1. Con la siguiente cadena de referencia: 1,2,0,3,4,2,0,1,5,2,0,6,1,2,3,7,6,3.
Indique cuántos fallos de página ocurrirán para un algoritmo de reemplazo
óptimo y uno LRU, si se tienen 4 marcos.

## Reemplazo Óptimo

| 1 | 2 | 0 | 3 | 4 | 2 | 0 | 1 | 5 | 2 | 0 | 6 | 1 | 2 | 3 | 7 | 6 | 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 3 | 3 | 3 |
|   | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 7 | 7 | 7 |
|   |   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
|   |   |   | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| x | x | x | x | x |   |   |   | x |   |   | x |   |   | x | x |   |   |

9 fallos

## LRU

| 1 | 2 | 0 | 3 | 4 | 2 | 0 | 1 | 5 | 2 | 0 | 6 | 1 | 2 | 3 | 7 | 6 | 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 1 | 1 | 1 | 1 | 6 | 6 |
|   | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
|   |   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 3 | 3 |
|   |   |   | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 | 6 | 6 | 6 | 6 | 7 | 7 | 7 |
| x | x | x | x | x |   |   | x | x |   |   | x | x |   | x | x | x |   |

12 fallos

2. Con la siguiente cadena de referencia: 3,4,2,0,1,5,2,7,6,3,2,1,2,6,3,0.
Indique cuántos fallos de página ocurrirán para un algoritmo FIFO, si se tienen
3 macros

## FIFO

| 3 | 4 | 2 | 0 | 1 | 5 | 2 | 7 | 6 | 3 | 2 | 1 | 2 | 6 | 3 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 3 | 3 | 0 | 0 | 0 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 6 | 6 | 6 |
|   | 4 | 4 | 4 | 1 | 1 | 1 | 7 | 7 | 7 | 2 | 2 | 2 | 2 | 3 | 3 |
|   |   | 2 | 2 | 2 | 5 | 5 | 5 | 6 | 6 | 6 | 1 | 1 | 1 | 1 | 0 |
| x | x | x | x | x | x | x | x | x | x | x | x |   | x | x | x |

15 fallos
