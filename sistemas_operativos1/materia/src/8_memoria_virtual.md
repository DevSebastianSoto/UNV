# Algoritmo optimo

- Cambia página que tardara más en ser usada
- Fallos más bajos posibles
- No es realizable
- Se usa como referencia

# FIFO (First In - First Out)

Cambia página que tiene más tiempo en memoria
más fácil de entender e implementar

- Inconvenientes:
  - Rendimiento pobre (páginas frecuentes pueden ser sustituidas)
  - **Anomalía de Belady** muchos fallos de página al aumentar número de
    macros

# LRU (Last Recently Used)

- Aproximación al reemplazo optimó
- Usar pasado reciente como predicción del futuro próximo
- Cambia página menos usada en el pasado inmediato
- Carece de **Anomalía de Belady**
- Requiere más hardware
  - Campo en las entradas de tabla de páginas
  - Pila de las páginas en memoria

## Algoritmos de aproximacion al LRU

- Reloj Global
- FIFO con segunda oportunidad
- NFU

# Casos de estudio

- **Working Set** (Conjunto de trabajo): numero de páginas que el proceso tiene
  garantizadas en memoria mientras se esa ejecutando

  > En este documento se hara referencia a esto como "ws"

## Windows

- Utiliza algoritmo de reemplazo de páginas local tipo FIFO
- Cambia página más antigua

## W2K

- Asigna tamaño mínimo del ws a nuevos procesos
- Gestor varia tamaño según requerimientos en memoria
- Incrementa memoria libre de un proceso si su tamaño es mayor que el mínimo
- Si proceso requiere más páginas, se eliminan del Working Set empleando FIFO
  - Permanecen en memoria:
    - Standby: proceso utiliza macro de pagina pero ha sido eliminada
    - Modificada: = Standby pero proceso ha escrito en la pagina sin
      actualizar el disco
  - Páginas eliminadas pueden verse sin realizar lectura de disco
