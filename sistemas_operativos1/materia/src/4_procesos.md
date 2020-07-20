# Definición de un proceso

## I

- Componentes: Un código y una estructura de datos
- Ejemplo:
  - El programa de Word no es un proceso.
  - El programa de Word ejecutándose será un proceso para el sistema operativo.
    - Le asigna recursos (CPU, memoria, etc.)
    - Controla su ejecución.

## II

- Actividad que se caracteriza por la ejecución de una secuencia de
  instrucciones, estado actual, y conjunto de recursos del sistema (Stallings)

- Proceso es instancia de un programa en ejecución, incluyendo valores actuales
  de contador de programa, registros y variables (Tannenbaum)

- Imagen:

  - Memoria en uso
  - Valores de registros generales
  - Estado de archivos abiertos
  - Directorio por defecto

- Proceso compite por el CPU y recursos del sistema con otros procesos.

# Diagrama de estados (básico)

Estructura de datos (Process Control Block - PCB)

> Imagen

## Estados

1.  Ejecución
2.  Listo
3.  Bloqueado (Espera)
    - Procesos entran en espera si duran mucho o faltan recursos

# Cola de procesos

> Imagen

1.  Se selecciona un proceso a ejecutar
2.  Se ejecuta
    - Si faltan datos entonces se bloquea y se pasa al siguiente proceso
    - Si se consiguen los datos, se regresa proceso a la cola
3.  Se termina el proceso (listo)

# Bloque de control de procesos

Si hay un proceso, existe un bloque de control de procesos

Almacena:

    * Estado
    * Id
    * Prioridad
    * Puntero a memoria
    * Puntero a recursos asociados
    * Puntero al siguiente PCB

# Jerarquía de procesos

El origen de los procesos define su hierarquía

> Imagen

| Unix        | Windows                   |
| ----------- | ------------------------- |
| PID         | PID                       |
| UID (USER)  | SID (Security Identifier) |
| GID (GROUP) | SID (Security Identifier) |

# Modelo de proceso

Concepto de proceso es heredado de la multiprogramación

PC = Program Counter

# Estructura de un proceso

Cuando se carga un proceso en memoria, tiene varias estructuras

Ejecutable solo tiene código, pero cuando se ejecuta (se carga en memoria),
este se infla (Ahora lee datos, aparta espacios para estructuras de datos que
va a necesitar: datos de sólo lectura)

1.  Pila

    El proceso Pila contiene los datos temporales, como los parámetros de método
    función, la dirección de retorno y las variables locales.

2.  Heap

    Esta es memoria asignada dinámicamente a un proceso durante su tiempo de ejecución.

> Imagen

# Hilos (Threads)

Compartir recursos entre procesos

Hilo = lightweight process (LWP) = unidad fundamental de uso de CPU

Se compone de:

    * registros
    * área en la pila

Cada hilo:

    * Comparte con otros, datos y recursos del SO
    * Pertenece a una sola tarea
    * Se puede ejecutar en un procesador (son adecuados para sistemas
        distribuidos y multiprocesador)

Proceso pesado = una tarea con un hilo de ejecución

Pueden ser implementados de las siguientes maneras:

- Usuario

  - Pros:
    - Conmutación entre hilos se realiza rápidamente sin ayuda del SO
  - Contras:
    - Si el SO no conoce de su existencia, el bloqueo de un hilo, detiene
      los hilos de esa misma tarea
  - Principales librerías para manejar threads a nivel usuario:
    - POSIX Pthreads
    - Win32 threads
    - Java thread

- Nivel de Sistema operativo
  - Pros:
    - Si el SO soporta hilos, el bloqueo de uno, no afecta al resto
  - Contras:
    - Conmutación de un hilo se hace vía interrupciones (mayor sobrecarga)
  - Ambos casos, planificación puede tener resultados desagradables

> Imagen
