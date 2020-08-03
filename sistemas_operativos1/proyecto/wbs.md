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
   - Definir página inicial de internet explorer el sitio de la intranet
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
   - Material relacionado a plataforma de virtuaización seleccionada
     (VirtualBox)

## Requerimientos del profesor

1. Software de virtuaización

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
   - Desarrollo de virtuaización
   - Material de seguimiento del proyecto
     - WBS
     - Cronograma
     - Matriz de responsabilidades
     - etc
   - Bitácora
   - Conclusiones
   - Recomendaciones
