### Prueba de fuente de video externa

Inicialmente se intentó acceder a una cámara local mediante índices de
OpenCV (`VideoCapture(0-5)`), pero el equipo utilizado no contaba con
una cámara física disponible.

Como alternativa se configuró un teléfono móvil con DroidCam como fuente
de video. El flujo se transmite mediante la red local y es recibido por
OpenCV utilizando una URL HTTP.

Esta configuración permitirá realizar las pruebas iniciales de percepción
sin requerir hardware adicional.

### Prueba 01 - Captura de video

**Objetivo:** validar una fuente de video compatible con OpenCV.

**Condición inicial:** el equipo de desarrollo no dispone de una webcam
física.

**Solución aplicada:** se utilizó un teléfono móvil mediante DroidCam,
transmitiendo el flujo de video a través de la red local.

**Resultado:** OpenCV recibió y visualizó correctamente los frames en
tiempo real.

**Observaciones:** fue necesario corregir la orientación del frame debido
a la posición física del teléfono.