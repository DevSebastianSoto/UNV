# Que es?

Tabla de palabras con su propia dirección

# Partición de memoria

Segmento de la memoria con direcciones generalmente contiguas

- No se traslapan
- Memoria total se divide en particiones

1.  Partición de numero y tamaño fijo
    - Mismo tamaño
    - Diferente tamaño
2.  Particiones de tamaño variable

# Fragmentación

Es memoria desaprovechada

- Interna

  - Diferencia de tamaño entre partición y objeto residente en ella

- Externa
  - Desaprovechamiento de memoria entre particiones

# Direcciones

- Física

  - Lugar definido en hardware

- Lógica

  - Referencia a dirección física
    - por ejemplo variable x = 10, x es lógica

- Relativa (también es lógica)
  - referencia una posición en memoria
  - tiene un punto de referencia
    - por ejemplo, indice de un arreglo arr[1] es relativa debido a que hace referencia al origen del arreglo

# Reubicación

Trasladar procesos activos dentro y fuera de memoria principal para maximizar
utilización del procesador

- Estática

  - Antes o durante la carga del programa
  - Programas no se pueden mover una vez iniciados

- Dinámica
  - En ejecución
  - Direcciones relativa
  - Hardware adicional (MMU)

# Protección y uso compartido

- ¿Qué debemos proteger?

  - El propio sistema operativo
  - El resto de procesos

- Métodos:

  - Registros base y límite
  - Bits de protección en memoria (IBM 360)
  - Derechos de acceso en tablas de traducción

- Problema: Compartir memoria

## Maquina desnuda

- No existe gestor de memoria
- Usuario controla todo
- No proporciona ningún servicio

## Sin abstracción de memoria monoprogramado

Esquema sencillo, 1 programa a la vez, compartiendo memoria entre programa
y OS

## Monitor monolítico o residente

Protección sin abstracción de memoria monoprogramado

## Multiprogramación sin abstracción de memoria

- Varios programas en memoria aunque no se utilice abstracción de memoria
  alguna
- Protección por hardware:
  - IBM 360, bits de protección (4bits)
- OS Controla llaves
- Reubicación estática (desventaja)

## Multiprogramación con abstracción de memoria

Creación de abstracción de (Adress Space)

Cada espacio de direcciones inicia en 0 y tiene un límite

Protección mediante:

- Registros base + límite
- Límite inferior - límite superior

# Intercambio (swap)

- Lidiar con sobrecarga de memoria
- Llevar proceso completo a memoria, ejecutarlo y luego regresarlo al
  disco
- Procesos inactivos mayormente son almacenados en el disco

# Asignación con crecimiento

- Asignar un poco de memoria adicional cada vez que se intercambia o
  mueve un proceso

# Memoria particionada contigua

Partición para cada proceso:

- OS/MFT (Sistema multiprogramado con tamaño y numero de particiones
  **fijo**)
- OS/MVT (Sistema multiprogramado con tamaño y numero de particiones
  **variable**)

# Administración de memoria libre

- Mapas de bits
- Listas enlazadas

# Algoritmos de asignación de memoria libre

- Primer Ajuste: Primer espacio libre
- Siguiente Ajuste: Primer espacio libre desde la ultima asignación
- Mejor Ajuste: Menor desperdicio de memoria
- Peor Ajuste: Mayor residuo de memoria
- Ajuste rápido: varias listas de acuerdo a tamaños de uso frecuente

# Segmentación

- Esquema de gestion de memoria
  - Computadores 80X86 INTEL
  - Cada segmento inicia en direccion virtual de 0
  - Direcciones tienen 2 componentes [SET:DESP]
    - Nombre segmento
    - Desplazamiento dentro del segmento
  - Segmentos con tamaños diferentes

# Aspectos importantes

- Problema: Qué ocurre si la TDS (tabla de descriptores de segmento) es muy grande?
- Solución: <a name="seg_sol">se guarda en memoria apuntada por un registro base</a>
- Problema: se necesitan dos referencias por cada acceso
- Solución:•Memoria cache•Utilizar registros internos dentro de la CPU (Intel)

- Ventajas:
  - No fragmentación interna
  - Crecimiento dinámico de segmentos
  - Protección y uso compartido
  - Enlace y carga dinámicos
- Desventajas:
  - Compactación de memoria (requerida)
  - Tamaño máximo fijo para segmento (típico 64K)
  - Mas hardware

# Paginación

- Asignación de memoria no es contigua
- Espacio en direcciones virtuales, dividido en bloques de tamaño fijo
  llamados páginas
- Dirección virtual = número página y desplazamiento

## Consideraciones

Los marcos libres se suelen mantener en una lista enlazadas

Si el cociente anterior no es entero se produce la llamada fragmentación
de página

Solución: [esto](#seg_sol)

## Protección y uso compartido

- Basada en bits de acceso
- Compartir paginas es sencillo
- Gestionada por el sistema operativo
- elimina fragmentación externa pero no interna
- Pagina grande = + Fragmentación interna
