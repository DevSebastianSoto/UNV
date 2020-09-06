# Tabla de contenido

<!-- vim-markdown-toc GFM -->

* [Sistemas de archivos](#sistemas-de-archivos)
    * [Archivos o Ficheros](#archivos-o-ficheros)
        * [Concepto de archivos](#concepto-de-archivos)
        * [Estructura de un archivo](#estructura-de-un-archivo)
        * [Tipos de archivos](#tipos-de-archivos)
        * [Acceso a un archivos](#acceso-a-un-archivos)
        * [Atributos de un archivo](#atributos-de-un-archivo)
        * [Operaciones con archivos](#operaciones-con-archivos)
    * [Directorios o carpetas](#directorios-o-carpetas)
        * [Sistemas jerárquicos de directorios](#sistemas-jerárquicos-de-directorios)
        * [Nombre de ruta de acceso](#nombre-de-ruta-de-acceso)
        * [Operaciones con directorios](#operaciones-con-directorios)
    * [Implementación del sistema de Archivos](#implementación-del-sistema-de-archivos)
        * [Implementación del sistema de archivos](#implementación-del-sistema-de-archivos-1)
        * [Implementación de archivos](#implementación-de-archivos)
        * [Implementación de directorios](#implementación-de-directorios)
        * [Archivos compartidos](#archivos-compartidos)
        * [Administración del espacio en disco](#administración-del-espacio-en-disco)
        * [Confiabilidad del sistema de archivos](#confiabilidad-del-sistema-de-archivos)
        * [Copias de seguridad](#copias-de-seguridad)
            * [Tratan de solucionar 2 problemas potenciales:](#tratan-de-solucionar-2-problemas-potenciales)
            * [Objetivos principales](#objetivos-principales)
            * [Respaldos adaptados al tipo de datos](#respaldos-adaptados-al-tipo-de-datos)
            * [Software de respaldos](#software-de-respaldos)
            * [Limitaciones](#limitaciones)
            * [Tipos de respaldo](#tipos-de-respaldo)
            * [Medios de respaldo](#medios-de-respaldo)
            * [RAID](#raid)
                * [Paridad](#paridad)
                * [Niveles](#niveles)
                * [Niveles Anidados](#niveles-anidados)
        * [Sistemas de archivos modernos](#sistemas-de-archivos-modernos)
            * [Journaling Filesystems](#journaling-filesystems)
* [Montaje de sistemas de archivos](#montaje-de-sistemas-de-archivos)
* [FAT](#fat)
* [Implementación de directorios](#implementación-de-directorios-1)
    * [MS-DOS](#ms-dos)
* [Conceptos fundamentales de Windows](#conceptos-fundamentales-de-windows)
* [NTFS](#ntfs)

<!-- vim-markdown-toc -->

# Sistemas de archivos

Almacenamiento secundario (necesario para manejar datos):

-   Gran cantidad
-   Persistentes
-   Compartidos

Deben proporcionar una interfaz sencilla para acceder a dichos dispositivos

**Solución** sistema de archivos, basado en archivos y directorios

## Archivos o Ficheros

### Concepto de archivos

> Archivo = unidad lógica de almacenamiento (se identifica con un nombre)

### Estructura de un archivo

-   secuencia de bytes (+ genérica)
-   secuencia de registros
-   árbol

### Tipos de archivos

-   Archivos normales o regulares (ASCII o binarios)
-   Directorios
-   Archivos especiales de caracteres
-   Archivos especiales de bloques

### Acceso a un archivos

-   Secuencial
-   Aleatorio o directo

### Atributos de un archivo

| Campo                          | Significado                                        |
| ------------------------------ | -------------------------------------------------- |
| Protección                     | Quién debe tener acceso y de qué forma             |
| Contraseña                     | Contraseña necesaria para tener acceso al archivo  |
| Creador                        | Identicador de la persona que creó el archivo      |
| Propietario                    | Propietario actual                                 |
| Bandera «sólo lectura»         | 0 Lectura/escritura, 1 para lectura exclusivamente |
| Bandera de ocultación          | 0 normal, 1 para no exhibirse en listas            |
| Bandera de sistema             | 0 archivo normal, 1 archivo del sistema            |
| Bandera de biblioteca          | 0 ya se ha respaldado, 1 necesita respaldo         |
| Bandera ASCII/binario          | 0 archivo en ASCII, 1 archivo en binario           |
| Bandera de acceso aleatorio    | 0 sólo acceso secuencial, 1 acceso aleatorio       |
| Bandera temporal               | 0 normal, 1 eliminar al terminar el proceso        |
| Bandera de cerradura           | 0 no bloqueado, 6= 0 bloqueado                     |
| Longitud de registro           | Número de bytes en un registro                     |
| Posición de la clave           | Ajuste de la clave dentro de cada registro         |
| Longitud de la clave           | Número de bytes en el campo clave                  |
| Tiempo de creación             | Fecha y hora de creación del archivo               |
| Tiempo del último acceso       | Fecha y hora del último acceso al archivo          |
| Tiempo de la última modicación | Fecha y hora de la última modicación del archivo   |
| Tamaño actual                  | Número de bytes en el archivo                      |
| Tamaño máximo                  | Tamaño máximo al que puede crecer el archivo       |

### Operaciones con archivos

|  Operación | Acción                                                    |
| ---------: | --------------------------------------------------------- |
|     create | -                                                         |
|     delete | -                                                         |
|       open | -                                                         |
|      close | -                                                         |
| read/write | -                                                         |
|     append | escribe al final                                          |
|       seek | especifica punto de lectura de datos en archivo           |
|    get/set | obtiene/establece atributos asociados a un archivo        |
|     rename | -                                                         |
|   truncate | elimina contenido de un archivo a partir de posición dada |

## Directorios o carpetas

### Sistemas jerárquicos de directorios

Almacenan información de otros archivos

-   Directorio unicode
-   Sistema jerárquico de Directorios
-   Un directorio por usuario

### Nombre de ruta de acceso

-   Absoluta
    -   Camino desde el root directorio
-   Relativa
    -   Directorio actual
    -   Directorios especiales
        -   .
        -   ..

### Operaciones con directorios

| Operación | Acción                                  |
| --------: | --------------------------------------- |
|    create | -                                       |
|    delete | -                                       |
|   opendir | -                                       |
|  closedir | -                                       |
|   raeddir | -                                       |
|    rename | -                                       |
|      link | enlace fisico para un archivo existente |
|    unlink | revert ^                                |

## Implementación del sistema de Archivos

### Implementación del sistema de archivos

-   Secuencia de bloques
    -   múltiplo del tamaño del sector
    -   bloque = cluster / unidad de tamaño de asignación
    -   sector = 512 bytes

### Implementación de archivos

-   Asignación continua

    -   bloques están contiguos
    -   Pros
        -   Fácil implementación
        -   Buen rendimiento
    -   Contras - Fragmentación externa - Irreal (si no se sabe el tamaño del archivo)
        > Útil para CD-ROMs y DVDs

-   Asignación con lista enlazada

    -   bloques con punteros
    -   Pros
        -   Fácil implementación
        -   Todos los bloques del disco se aprovechan
    -   Contra
        -   Acceso aleatorio es lento
        -   El espacio de almacenamiento de un bloque deja de ser potencia de 2

-   Asignación con lista enlazada e indicé

    -   Misma idea que antes, pero punteros almacenan en estructura aparte de
        indice (se almacena en disco y se lee cuando se usa el sistema, se
        escribe cuando cambia)
    -   No hay desventajas anteriores
    -   Tamaño de la tabla (desventaja)
    -   Ejemplos:
        -   FAT
        -   MS-DOS

-   Asignación con nodos-i
    -   existe nodo por archivo, nodo contiene atributos y direcciones de los
        bloques del mismo
    -   nodo se guarda en disco y se lee **cuando se abre el archivo**
    -   para archivos grandes hay bloques indirectos (almacenan direcciones de
        bloques)

### Implementación de directorios

-   **Principal Función** asocian nombre del archivo con la información del mismo

-   Aspecto relacionado es donde se guardan los atributos:
    -   entrada del directorio
    -   estructura aparte apuntada por la entrada del directorio

### Archivos compartidos

### Administración del espacio en disco

-   Tamaño de bloque lógico

    -   múltiplo del tamaño del bloque
    -   buscar equilibrio entre **eficiencia y tasa de transferencia**

-   Registro de bloques libres

    -   ligada a bloques libres agrupados
    -   mapa de bits (FAT en MS-DOS, Ext2/Ext3 in Linux, NETFS en Windows, etc.)

-   Cuotas de disco (Evitan que el usuario se apodere de todo el espacio del
    disco)

    -   Limita:
        -   numero de archivos usados
        -   numero de bloques usados

-   Administrador establece cuotas de usuario y grupo

    -   Configuración se guarda en archivos especiales y de grupo
    -   nivel suave y duro

### Confiabilidad del sistema de archivos

FS no puede ofrecer protección contra destrucción física, pero puede ayudar a
proteger información

Mejor confiabilidad de sistema de archivos:

-   Evitar bloques defectuosos
-   Evitar pérdida de datos cuando se estropean bloques sanos o un usuario los
    daña
-   Recuperar consistencia del sistema de archivos cuando el sistema se cae
-   Manejo de bloques defectuosos
    -   Solución de hardware
        -   Sectores de reserva en disco y mapa que asocia bloques defectuosos a
            bloques sanos
    -   Solución de software
        -   FS identifica bloques defectuosos y evita su uso
            -   En Ext2 y NTFS: archivo inaccesible al que pertenecen bloques
                defectuosos
            -   MS-DOS: se marca el bloque en la FAT como defectuoso
-   Consistencia del sistema de archivos
    -   FS leen bloques del disco, modifican la memoria y los escriben luego en
        el disco
    -   Si el sistema falla cuando están escribiendo bloques:
        -   FS queda en estado inconsistente
        -   **Problema se agrava** si bloques que no se escriben son de
            meta datos(nodos-i, bloques indirectos, directorios...)
        -   _Solución_ ejecutar programa cuando se reinicie sistema para
            comprobar consistencia de bloques y archivos

### Copias de seguridad

#### Tratan de solucionar 2 problemas potenciales:

1.  Recuperarse de un desastre (bloque o disco que se estropee)
2.  Recuperarse de los errores de los usuarios (accidentes)

#### Objetivos principales

1.  Permitir restauración de archivos individuales

    -   Borrado accidental de un archivo
    -   Fácilmente repetible y más frecuente

2.  Restauración completa de sistemas de archivos complejos
    -   Menos frecuente
    -   Mas compleja

#### Respaldos adaptados al tipo de datos

-   Respaldo = instantánea de datos respaldados (momento en tiempo)
-   Menos cambios = menos respaldos = menos frecuencia
-   Sistemas Operativos: cambian con actualizaciones, reparaciones y
    modificaciones
-   Aplicaciones: instalación, actualización o remoción
    -   Datos: según la aplicación
-   Datos de usuarios: patrones de la comunidad del usuario

#### Software de respaldos

-   ¿Qué hacen?:

    -   Planifica respaldos para que se ejecuten en el momento adecuado
    -   Maneja la ubicación, rotación y uso de la media de respaldo
    -   Funciona con operadores (y/o cargadores robóticos) para asegurarse de que
        la media apropiada está disponible
    -   Asiste a los operadores en ubicar la media que contiene un respaldo específico de un archivo dado

-   Soluciones:

    -   Comprar una solución desarrollada comercialmente
    -   Desarrollar una solución casera de sistema de respaldo desde el principio (posiblemente integrando una o más tecnologías de código

-   Considerar:
    -   Cambiar el software de respaldo es complicado; una vez implementado
    -   100% confiable
    -   Complejidad de respaldo y recuperación

#### Limitaciones

Un esquema de respaldos efectivo tendrá en cuenta las siguientes
limitaciones

-   Ventana de respaldo

    -   Es el tiempo en el que el sistema se respalda
    -   Ocurre cuando el sistema es menos activo

-   Impacto al rendimiento

-   Ancho de banda de red

-   Costos (hardware, software, mano de obra)

#### Tipos de respaldo

> DOS/WINDOWS existe el atributo "A" indica que se modifico el archivo

-   Completo

    -   -   básico
    -   Duración O(n)
    -   -   ventana de respaldo

-   Diferencial

    -   Solo respalda los archivos modificados desde le último respaldo completo

-   Incremental

    -   Solo respalda los archivos modificados desde le último respaldo

-   Snapshot
    -   Instantánea
    -   Eficaz

#### Medios de respaldo

-   Cintas (D2T)

    -   barato
    -   removible

-   Discos (D2D)

    -   rápido
    -   caro
    -   sensible al transporte

-   Híbrido (D2D2T)

    -   Mejoras justifican inversión

-   Red (Sitio alterno)

#### RAID

> Redundant Array of Inexpensive Disks -> Re... Independent Disks
>
> Mirror es un bloque en 2 discos diferentes

Consiste en combinar varios discos pequeños como un grupo para alcanzar mejor
rendimiento que in disco grande y caro

Existen configuraciones de RAID _niveles_

Beneficios de un RAID respecto a un único disco son:

-   Mayor integridad
-   Mayor tolerancia a fallos
-   Mayor throughput(rendimiento)
-   Mayor capacidad

-   Combinar dispositivos de bajo coste y diversas tecnologías

-   Varios discos en una unidad logica (sistema operativo observa como su fuese
    uno solo)
-   Servidores e implementan unidad es de disco de la misma
    capacidad.

-   Existen RAIDs por hardware y software\*\*

    -   Hardware
        -   Corre en CPU de la RAID controller
        -   No ocupa memoria del equipo y no depende del sistema operativo
    -   Software
        -   CPU del servidores
            -   Degrada rendimiento de servidor por este motivo
        -   Depende del CPU del servidor y de su carga

##### Paridad

-   Bit extra (detectar errores de almacenamiento o transmisión)
-   Es impar (paridad)
-   Un bit de paridad encuentra errores de un solo bit
-   No se sabe cual bit es incorrecto
    -   Función XOR puede usarse para ese fin

##### Niveles

|  RAID  | Redundancia                                                  |  Discos  |
| :----: | ------------------------------------------------------------ | :------: |
|        | - No hay redundancia                                         |          |
|    0   | - No fallos                                                  |   (2?)   |
|        | - Alto rendimiento para leer y escribir datos en paralelo    |          |
| ------ | ------------------------------------------------------------ | -------- |
|        | - Datos duplicados (alta redundancia / tolerancia a fallos)  |          |
|    1   | - Escribe fisicamente en cada disco                          |     2    |
|        | - Lee mas rapido (lee del disco menos ocupado)               |          |
| ------ | ------------------------------------------------------------ | -------- |
|        | - No comercial                                               |          |
|    4   | - Disco dedicado a paridad                                   |     3    |
|        | - Bajo rendimiento, cada cambio en bloque escribe al disco   |          |
| ------ | ------------------------------------------------------------ | -------- |
|        | - Soporta perdida de 1 disco                                 |          |
|    5   | - Bloque de paridad no se lee en operaciones de lectura      |     3    |
|        | - Mas populares (buen rendimiento espacio vs proteccion)     |          |
| ------ | ------------------------------------------------------------ | -------- |
|        | - Es RAID 5 pero con un bloque extra de paridad              |          |
|    6   | - Discos: 2 (datos) y 2 (d1+d2=x2 paridad)                   |     4    |
|        | - Soporta perdida de 2 discos                                |          |
| ------ | ------------------------------------------------------------ | -------- |
|        | - Mas populares                                              |          |
|   1+0  | - Division de espejos                                        |     4    |
|        | - Soporta perdida de 2 discos                                |          |

-   RAID 1

    -   Mayor nivel de redundacia
        -   Guarda el doble de los datos
    -   Mirror
    -   Tolera fallos
        -   trabaja si un disco falla
    -   Escritura
        -   físicamente en cada disco
    -   Lectura
        -   Puede leer de ambos o el menos ocupado
        -   duplica velocidad de lectura

-   RAID 4

    -   Acceso independiente de discos dedicados a paridad
    -   Cada stripe = bloque extra paridad
    -   Mínimo 3 discos
    -   Disco de paridad puede ser el cuello de botella

-   RAID 5

    -   Cada stripe tiene un bloque extra, pero distribuida entre discos
    -   Bloque de paridad no se lee en operaciones de lectura
    -   Soporta perdida de un discos
    -   Mínimo 3 discos físicos

-   RAID 6

    -   RAID 5 + 1 bloque de paridad
    -   Soporta perdida de 2 discos físicos
    -   Mínimo 4 discos

##### Niveles Anidados

> Implementar 1+0 es mas facil que 0+1, ademas es mas popular (segun la
> experiencia del profe)

-   RAID 1+0

    > LLamado raid 10

    -   Espejos
    -   Buena elección para bases de datos (no calcula paridad = mayor velocidad de escritura)
    -   Mínimo 4 discos físicos

-   RAID 0+1
    > LLamado raid 01
    >
    > -   Espejo de divisiones
    > -   Mínimo 4 discos físicos

### Sistemas de archivos modernos

-   Los sistemas de archivos modernos se enfrentan a dos grandes problemas:

    -   La gran capacidad de los dispositivos de almacenamiento
    -   Su lentitud

-   La gran capacidad de almacenamiento obliga a dichos FS a utilizar estructuras
    de datos escalables (árboles B+, principalmente) y transaccionespara poder
    recuperar rápidamente la consistencia tras una caída

-   La lentitud determina, en gran medida, la estructura global del sistema de
    archivos y su funcionamiento interno ) se deben optimizar las lectura y
    escrituras que deben ser secuenciales y en grandes grupos si es posible

-   Como ejemplo, veamos el mecanismo de transacciones

#### Journaling Filesystems

-   Para no perder la consistencia del FS las modificaciones tienen que ser
    atómicas:

    1.  Las modificaciones se guardan primero en un fichero especial, llamado
        registro, bitácora o journal

    2.  Cuando dicho fichero está a salvo en disco, se escriben en disco las
        modificaciones del propio sistema de archivos

    3.  Si el sistema cae en el primer punto se pierden modificaciones (pero
        ninguna queda a medio)

    4.  Si cae en el segundo, se rehacen las modificaciones del registro (que
        deben ser idempotentes)

-   El tiempo de recuperación depende del tamaño del registro, que suele ser muy
    pequeño (32 MB, 64 MB, etc.)

-   Ejemplos de sistemas de archivos transaccionales: Ext3, ReiserFS, XFS, JFS y
    NTFS

# Montaje de sistemas de archivos

>   BIOS pueden usar varios dispositivos de almacenamiento a la vez
>   Para usar dispositivo, es necesario crear el sistema de archivos

-   Disco
-   Particion
    -   División del disco
    -   Parte que actúa como un disco independiente
    -   Info en tabla de particiones, en primer sector del Disco duro (MBR)
        -   Master Boot Record
            -   Contiene código de arranque del computador
    -   Para usar una partición, se le debe asignar un sistema de archivos
    -   Cuando se arranca del disco duro, MBR determina partición activa, carga
        el código de su bloque de arranque y cede el control
-   Volumen
    -   Partición formateada (espacio libre)

# FAT

> File Allocation Table

-   Creada por Bill Gates en el 77 (manejo de discos BASIC)
-   QDOS la uso en los 80
-   Propósito, diskettes
-   Versiones
    -   12
    -   16
    -   32
-   VFAT (soporta largos nombres)
-   exFAT (no es compatible)

# Implementación de directorios

## MS-DOS

directorio = file that stores ul entries (32 bytes)

-   Características
    -   Bit en atributos distingue al directorio
    -   Directorio puede tener subdirectorios
        -   Árbol de directorios
    -   Directorio raíz tiene tamaño máximo

# Conceptos fundamentales de Windows

-   Windows 200 permite tener varios sistemas de archivos a la vez.
-   Principal sistema NTFS
-   Limite de nombre 255 para archivos
-   Limite ruta completa 32.767
-   API Win32 no diferencia case (NTFS si)
-   Handles  
    -   entrada
    -   salida
    -   salida de error

# NTFS

-   Nombres largos
-   Formato UNICODE
-   Archivos multiflujo (un archivos es uno o más flujos de 
    bytes a los que se puede acceder de manera 
    individual)
-   Direcciones de bloque lógico de 8 bytes y tamaños de bloque logico entre
    512 btyes y 64 Kbytes
-   Compresion transparente de archivos
-   Cifrado de archivos
-   Rendimiento adecuado
-   Archivo NTFS
    -   minimo 2 atributos [nombre y flujo (maximo 2^64 bytes)]
-   Tabla maestra de archivos MASTER FILE TABLE
