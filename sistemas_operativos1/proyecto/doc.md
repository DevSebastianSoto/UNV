% test

# Portada

# Indices

# Introducción

# Desarrollo de virtualización

## Software de virtualización

### Ventajas

### Desventajas

### Historia

### Características

### Otros detalles relevantes

## Instalación

### Maquina virtual Windows 10

### Maquina virtual Windows Server 2019

## Configuración del sistema operativo

### (De acuerdo al sistema operativo)

## Pruebas

### Validar servicios funcionan adecuadamente

### Copiar archivos al servidor

### Cambiar permisos de archivos / carpetas

# Work Bearkdown Structure (Estructura de índice)

> Material de referencia para realizar este documento, en este [sitio](http://biblus.accasoftware.com/es/wbs-workbreakdownstructure-que-es-y-como-se-usa/)

## Requerimientos de la empresa

1. Documentación

   - Autenticación centralizada (Active Directory)
   - Carpetas compartidas desde el servidor (grupales y personales)
   - DFS (utilización de un namespace para el acceso a recursos compartidos)
   - DHCP (Debe ser instalado y configurado utilizando powershell)
   - DNS (con resolución de nombres externos)
   - Implementación de políticas de grupo
   - Intranet utilizando http y https
   - Certificate Authority (CA) para certificado de la intranet
   - Folder redirection del directorio “Mis Documentos” perfil del usuario en las estaciones.
   - WSUS (actualización de parches de clientes)

2. Pagina web básica

   - 3 paginas
   - Relación entre páginas

3. Políticas de grupo (Permitir al usuario)

   - Cambiar fondo de pantalla (FondoEmpresarial.jpg)
   - Deshabilitar panel de control para usuarios no administradores de dominio
   - Definir página inicial de Internet explorer el sitio de la intranet
   - Deshabilitar ejecución de notepad.exe y regedit.exe
   - Mapear recurso de red usando DFS para uso personal (a cada usuario se le
     mapeará unidad P: para uso personal y dicha carpeta se accede mediante
     una ruta DFS)
   - Renombrar administrador (administrator), invitado (guest)
   - Política para aplicar actualizaciones del sistema operativo
   - Ubicar Folder Redirection para usuarios del dominio
   - Configurar firewall de Windows para permitir ping entre equipos de
     dominio

4. Vídeos

   - Instalación de plataforma
   - Configuración de plataforma
   - Hosting de streaming
     - Indice
     - Material de referencia (Vídeos, documentos, artículos)

5. Presentación

   - Bitácora
     - decisiones de diseño
     - situaciones que se presenten
     - detalles de las reuniones (minutas)
     - detalles relevantes para el proyecto
   - Material relacionado a plataforma de virtualización seleccionada
     (VirtualBox)

## Requerimientos del profesor

1. Software de virtualización

   - Seleccionar uno
   - Investigar
     - Ventajas
     - Desventajas
     - Historia
     - Características
     - Otros detalles relevantes

2. Instalación

   - Maquina virtual Windows 10
   - Maquina virtual Windows Server 2019

3. Configuración del sistema operativo

   - (De acuerdo al sistema operativo)

4. Pruebas

   - Validar servicios funcionan adecuadamente
   - Copiar archivos al servidor
   - Cambiar permisos de archivos / carpetas

5. Documento (Paginas: 20 - 60)
   - Portada
   - Indices
   - Introducción
   - Desarrollo de virtualización
   - Material de seguimiento del proyecto
     - WBS
     - Cronograma
     - Matriz de responsabilidades
     - etc
   - Bitácora
   - Conclusiones
   - Recomendaciones

# Cronograma

# Matriz de responsabilidades

# Servicios

## Autenticación centralizada (Active Directory)

### Qué es?

Active Directory es un producto de Microsoft que consiste de varios servicios
de Windows Server. Le permite a los administradores manejar permisos y acceso
a recursos de red.

Active Directory almacena datos como objetos. Un objeto es un elemento único,
como un usuario, grupo, aplicación o dispositivo, como una impresora. Los
objetos se definen normalmente como recursos, como impresoras o computadoras, o
directores de seguridad, como usuarios o grupos. Active Directory clasifica los
objetos por nombre y atributos. Por ejemplo, el nombre de un usuario puede
incluir la cadena del nombre, junto con la información asociada con el usuario,
como contraseñas y claves de Secure Shell (SSH).

El servicio principal en Active Directory son los Servicios de dominio (AD DS),
que almacena información de directorio y maneja la interacción del usuario con
el dominio. AD DS verifica el acceso cuando un usuario inicia sesión en un
dispositivo o intenta conectarse a un servidor a través de una red. AD DS
controla qué usuarios tienen acceso a cada recurso. Por ejemplo, un
administrador suele tener un nivel de acceso a los datos diferente al de un
usuario final.

Un dominio es un grupo de objetos, como usuarios o dispositivos, que comparten
la misma base de datos de AD. Los dominios tienen una estructura de sistema de
nombres de dominio (DNS)

### Ventajas

- Organización: Gestión centralizada de identidades y accesos (IAM).

  - Administradores pueden manejar toda su red de TI
    basada en Windows desde una ubicación central, en lugar de hacerlo
    localmente por sistema.

- Autenticación: Debido a que todo se maneja de forma centralizada, el usuario
  final solo debe verificar su identidad 1 vez, debido a que el "Active
  Directory domain controller" se encarga de manejar la verificación de las
  entidades

  - Aplicaciones del mercado se integran con el directorio activo para
    facilitar la autenticación.

- Escalabilidad: Se puede manejar un sistema tan grande o pequeño como sea
  necesario

- Permisos y Políticas: Dar o negar acceso a usuarios sobre recursos de la red, lo cual
  da control total al administrador sobre la manera en que se utiliza el
  sistema.

### Desventajas

- IAM centralizado con AD solo se puede lograr en un entorno centrado en
  Windows.

- También requiere una cantidad significativa de infraestructura local
  para implementar y mantener el sistema.

- Las empresas también quieren eliminar la mayor parte de su infraestructura de TI local en
  favor de alternativas en la nube. Entonces, la AD heredada puede ser
  limitante.

## Carpetas compartidas desde el servidor (grupales y personales)

### Qué es?

El servidor provee la capacidad a sus usuarios de acceder un sistema de
carpetas que se comparte en el servidor, esos sistemas pueden tener permisos y
políticas para que cada persona tenga diferentes actividades disponibles.

Existe por ejemplo, una carpeta por persona, en la cual guarda sus documentos
de trabajo, y también existe una carpeta para su equipo y otra para su
departamento. Como es de esperar, en la carpeta personal solo el usuario dueño
puede alterar su contenido, en el caso del equipo solo los miembros del mismo
pueden realizar actividades en la carpeta del mismo, y así para cada posible
implementación de las carpetas compartidas

> En el ejemplo anterior se hace referencia a el uso de carpetas grupales (equipo,
> departamento) y personales (por usuario).

### Ventajas

- La facilidad de uso
- Acceso a los archivos desde cualquier dispositivo que pertenezca al servidor
- Seguridad con la realización y sincronización de respaldos
- Se facilita la colaboración entre los usuarios
- Reducción de gasto en la compra de en equipos físicos

### Desventajas

- Permisos mal definidos pueden crear fallas de seguridad en el sistema debido
  a que cualquier persona podría alterar el contenido de alguna carpeta
- La información, al estar centralizada, depende altamente de los centros donde
  se este guardando la misma. Si algo ocurre en estos dispositivos de
  almacenamiento, se pierde todo el contenido que en ellos se encuentra, para
  todos los usuarios del servidor.
- Nuevos gastos de seguridad y cuidados del sistema de almacenamiento para
  evitar que ocurran imprevistos.
- No se puede trabajar simultáneamente en los documentos o archivos.

## DFS (utilización de un namespace para el acceso a recursos compartidos)

### Qué es?

### Ventajas

### Desventajas

## DHCP (Debe ser instalado y configurado utilizando powershell)

### Qué es?

### Ventajas

### Desventajas

## DNS (con resolución de nombres externos)

### Qué es?

### Ventajas

### Desventajas

## Implementación de políticas de grupo

### Qué es?

### Ventajas

### Desventajas

## Intranet utilizando http y https

### Qué es?

### Ventajas

### Desventajas

## Certificate Authority (CA) para certificado de la intranet

### Qué es?

### Ventajas

### Desventajas

## Folder redirection del directorio “Mis Documentos” perfil del usuario en las estaciones.

### Qué es?

### Ventajas

### Desventajas

## WSUS (actualización de parches de clientes)

### Qué es?

### Ventajas

### Desventajas

# Bitácora

# Conclusiones

# Recomendaciones

# Bibliografía

https://searchwindowsserver.techtarget.com/definition/Active-Directory
https://jumpcloud.com/blog/active-directory-pros-cons
https://securityboulevard.com/2019/03/active-directory-pros-and-cons/
https://www.tecnozero.com/blog/directorio-activo-de-microsoft-que-es-que-ventajas-tiene-para-la-empresa/
