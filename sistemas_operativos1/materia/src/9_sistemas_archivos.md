# Tabla de contenido

<!-- vim-markdown-toc Marked -->

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
        * [Implementación del sistema de archivos](#implementación-del-sistema-de-archivos)
        * [Implementación de archivos](#implementación-de-archivos)
        * [Implementación de directorios](#implementación-de-directorios)
        * [Archivos compartidos](#archivos-compartidos)
        * [Administración del espacio en disco](#administración-del-espacio-en-disco)
        * [Confiabilidad del sistema de archivos](#confiabilidad-del-sistema-de-archivos)
        * [Copias de seguridad](#copias-de-seguridad)
        * [Sistemas de archivos modernos](#sistemas-de-archivos-modernos)
    * [Sistemas de archivos en windows](#sistemas-de-archivos-en-windows)
    * [Sistemas de archivos en Unix-Like](#sistemas-de-archivos-en-unix-like)

<!-- vim-markdown-toc -->

# Sistemas de archivos

Almacenamiento secundario (necesario para manejar datos):

- Gran cantidad
- Persistentes
- Compartidos

Deben proporcionar una interfaz sencilla para acceder a dichos dispositivos

**Solución** sistema de archivos, basado en archivos y directorios

## Archivos o Ficheros

### Concepto de archivos

> Archivo = unidad lógica de almacenamiento (se identifica con un nombre)

### Estructura de un archivo

- secuencia de bytes (+ genérica)
- secuencia de registros
- árbol

### Tipos de archivos

- Archivos normales o regulares (ASCII o binarios)
- Directorios
- Archivos especiales de caracteres
- Archivos especiales de bloques

### Acceso a un archivos

- Secuencial
- Aleatorio o directo

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

- Directorio unicode
- Sistema jerárquico de Directorios
- Un directorio por usuario

### Nombre de ruta de acceso

- Absoluta
  - Camino desde el root dir
- Relativa
  - Dir actual
  - Directorios especiales
    - .
    - ..

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

- Secuencia de bloques
  - múltiplo del tamaño del sector
  - bloque = cluster / unidad de tamaño de asignación
  - sector = 512 bytes

### Implementación de archivos

- Asignación continua

  - bloques están contiguos
  - Pros
    - Fácil implementación
    - Buen rendimiento
  - Contras - Fragmentación externa - Irreal (si no se sabe el tamaño del archivo)
    > Útil para CD-ROMs y DVDs

- Asignación con lista enlazada

  - bloques con punteros
  - Pros
    - Fácil implementación
    - Todos los bloques del disco se aprovechan
  - Contra
    - Acceso aleatorio es lento
    - El espacio de almacenamiento de un bloque deja de ser potencia de 2

- Asignación con lista enlazada e indicé

  - Misma idea que antes, pero punteros almacenan en estructura aparte de
    indice (se almacena en disco y se lee cuando se usa el sistema, se
    escribe cuando cambia)
  - No hay desventajas anteriores
  - Tamaño de la tabla (desventaja)
  - Ejemplos:
    - FAT
    - MS-DOS

- Asignación con nodos-i
  - existe nodo por archivo, nodo contiene atributos y direcciones de los
    bloques del mismo
  - nodo se guarda en disco y se lee **cuando se abre el archivo**
  - para archivos grandes hay bloques indirectos (almacenan direcciones de
    bloques)

### Implementación de directorios

- **Principal Función** asocian nombre del archivo con la información del mismo

- Aspecto relacionado es donde se guardan los atributos:
  - entrada del directorio
  - estructura aparte apuntada por la entrada del directorio

### Archivos compartidos

### Administración del espacio en disco

- Tamaño de bloque lógico

  - múltiplo del tamaño del bloque
  - buscar equilibrio entre **eficiencia y tasa de transferencia**

- Registro de bloques libres

  - ligada a bloques libres agrupados
  - mapa de bits (FAT en MS-DOS, Ext2/Ext3 in Linux, NETFS en Windows, etc.)

- Cuotas de disco (Evitan que el usuario se apodere de todo el espacio del
  disco)

  - Limita:
    - numero de archivos usados
    - numero de bloques usados

- Administrador establece cuotas de usuario y grupo

  - Configuración se guarda en archivos especiales y de grupo
  - nivel suave y duro

### Confiabilidad del sistema de archivos

FS no puede ofrecer protección contra destrucción física, pero puede ayudar a
proteger información

Mejor confiabilidad de sistema de archivos:

- Evitar bloques defectuosos
- Evitar pérdida de datos cuando se estropean bloques sanos o un usuario los
  daña
- Recuperar consistencia del sistema de archivos cuando el sistema se cae
- Manejo de bloques defectuosos
  - Solución de hardware
    - Sectores de reserva en disco y mapa que asocia bloques defectuosos a
      bloques sanos
  - Solución de software
    - FS identifica bloques defectuosos y evita su uso
      - En Ext2 y NTFS: archivo inaccesible al que pertenecen bloques
        defectuosos
      - MS-DOS: se marca el bloque en la FAT como defectuoso
- Consistencia del sistema de archivos
  - FS leen bloques del disco, modifican la memoria y los escriben luego en
    el disco
  - Si el sistema falla cuando están escribiendo bloques:
    - FS queda en estado inconsistente
    - **Problema se agrava** si bloques que no se escriben son de
      meta datos(nodos-i, bloques indirectos, directorios...)
    - _Solución_ ejecutar programa cuando se reinicie sistema para
      comprobar consistencia de bloques y archivos

### Copias de seguridad

> Tratan de solucionar 2 problemas potenciales:

<!--Diapositiva #8 09.2 sistemas de archivos-->

### Sistemas de archivos modernos

## Sistemas de archivos en windows

## Sistemas de archivos en Unix-Like
