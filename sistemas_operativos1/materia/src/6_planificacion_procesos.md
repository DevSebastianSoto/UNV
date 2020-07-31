# Planificación de procesos

-   Ejecución de secuencias CPU y espera
-   Objetivos
    -   Equidad
    -   Eficiencia
    -   Bajo tiempo de repuesta
    -   Rendimiento alto
    -   Minimizar tiempo de espera
-   Objetivos pueden conseguirse simultáneamente

## Planificadores (schedulers)

-   Largo plazo
    -   Grado de multiprogramación
-   Corto plazo
    -   Elige entre trabajos en memoria y que preparados para ejecutarse en la CPU
    -   Este debe ser muy rápido ya que entra en juego recientemente

## Criterios de planificación

-   Utilización de la CPU

    -   Maximizar el rendimiento de la CPU

-   Rendimiento ("Throughput")

    -   Trabajos completados por unidad de tiempo

-   Tiempo de estancia ("Turnaroundtime")

    -   Tiempo de retorno, es el intervalo de tiempo desde que un proceso es
        cargado hasta que este finaliza su ejecución

-   Tiempo de espera (Waitingtime)

    -   Es la suma de los intervalos de tiempo que un proceso estuvo en la cola de
        procesos listos (readyqueue)

-   Tiempo de respuesta (Response time)

    -   Es el intervalo de tiempo desde que un proceso es cargado hasta que brinda
        su primer respuesta.
    -   Es útil en sistemas interactivos

## Categorías de algoritmos de planificación

### Entornos

-   Todos (_BAE_)
    -   Equidad: Cada proceso, parte justa de la CPU
    -   Aplicación de políticas: Validar que se cumplen políticas establecidas
    -   Balance: Mantener ocupadas todas las partes del sistema
-   Procesamiento por lotes (_RUT_)
    -   Rendimiento: Maximizar número de trabajos por hora
    -   Tiempo de retorno: Minimizar tiempo de entrega y terminación
    -   Utilización de la CPU: Mantener CPU ocupada siempre
-   Interactivo (_PROTI_)
    -   Tiempo de respuesta: Rapidez
    -   Proporcionalidad: Cumplir expectativas de usuarios
-   De tiempo real (_IRCU_)
    -   Cumplir con los plazos: Evitar perder datos
    -   Predictibilidad: Evitar degradación de calidad en sistemas multimedia

## Algoritmos

### Algoritmos de prioridad

> Prioridad = CPU que se le asigna

1.  Internas
    -   Tiempo de CPU
    -   Memoria usada
    -   Recursos
2.  Externas
    -   Tiempo de usuario
    -   Tiempo de aplicación

#### FCFS (Primero en entrar, primero en salir)

-   No apropiativo
-   Como cola FIFO
-   Mas fácil de codificar
-   Depende de tipos de trabajo y del instante en que llegan

#### SJF (Shortest Job First)

-   No apropiativo
-   Asigna CPU a la ráfaga mas pequeña
-   Optimo para reducir tiempos de espera

### Algoritmos con expulsión

#### Round Robin

-   CPU se asigna durante un cuanto de tiempo
-   Cola FIFO
-   Regla: 80% de las ráfagas deben ser menores que el cuantum
