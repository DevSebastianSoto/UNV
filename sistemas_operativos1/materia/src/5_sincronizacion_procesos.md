# Independiente y cooperantes

| Independientes                     | Cooperantes              |
| ---------------------------------- | ------------------------ |
| estado no compartido               | estado compartido        |
| deterministas                      | no determinista          |
| reproducibles                      | puede ser irreproducible |
| pueden ser detenidos, rearrancados |                          |

# Productor Consumidor

Buffer circular, un proceso genera datos y otro los consume.

El productor no escribe si el buffer esta lleno

Consumidor y productor comparten buffer y contador de espacios

## Condiciones de carrera

Cuando se corrompe el contador, ya que tiene un valor que no debe ser debido a
ser manipulado por varios hilos

> Variable contador no es atómica

# Filósofos comensales

Mesa circular, N filósofos que comen o piensan de forma mutuamente excluyente
Necesitan 2 palillos para comer, pero no hay suficientes para que todos lo
hagan al mismo tiempo

> Imagen

# Puente estrecho

Solo pueden pasar carros de una dirección a la vez.

> Imagen

# Tipos de soluciones

> Suposiciones
>
> 1.  Se ejecutan una vez
> 2.  Velocidad relativa no influye

## Instrucciones maquina

## Primitivas

## Regiones criticas y monitores

## Semáforos

Introducidos por Dijstra en los 60's

- Tipo de variable que solo puede ser accedida por 2 primitivas P y V

  - P (semáforo) operación atómica que espera a que el semáforo sea positivo,
    decrementa variable en 1
  - V (semáforo) operación atómica que incrementa variable en 1

- Independientes de la máquina

- Simples

- Varios procesos

- Exclusión mutua

- Planificación

- Es una variable entera

- Puede ser llamada solo por 2 operaciones indivisibles
  - wait & signal (P & V)

## Variables de control

- Validas para varios procesadores
- Suposición: instrucciones de carga y almacenamiento atómicas

### Comunicación con mensajes

- Mensaje: parte de información que es pasada de un proceso a otro

- Buzón: lugar donde se depositan los mensajes desde el envío a la recepción

- Operaciones sobre mensajes:
  - Enviar
  - Recibir

#### Métodos de comunicación con mensajes

1.  Único sentido

    - Pipes
    - Streams
    - Productor-consumidor

2.  Bidireccional
    - RPC's
    - Cliente-servidor
    - Request-Response

#### Porqué usar mensajes

- Pros:
  - menos errores
  - procesos no confían entre si
  - distintos programadores y momento diferente
  - procesos en diversos procesadores

# Conceptos

## Atomicidad

- Operación es atómica cuando se ejecuta con interrupciones deshabilitadas (en
  sistema monoprocesador)

- Referencias y asignaciones son atómicas en la mayoría de los sistemas

- Si hardware no proporciona operaciones atómicas, no se pueden construir por
  Software

## Exclusión mutua

Mecanismo que asegura que solo se ejecute un proceso en un instante determinado

## Sección critica

Sección de código en que se actualizan variables comunes.

Solo puede haber un proceso en sección crítica a la vez

Toda solución cumple:

1.  Exclusión mutua
2.  Progreso
3.  Espera limitada
