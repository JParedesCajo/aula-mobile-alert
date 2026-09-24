# aula-mobile-alert
Sistema acádemico de percepción computacional para la detección y análisis del uso de dispositivos móviles en aulas.

### Entorno de desarrollo

El proyecto utiliza Python 3.11 dentro de un entorno virtual `.venv`.

Instalación de dependencias:

```powershell
python -m pip install -r requirements.txt
```

### Progreso Sprint 1

- [x] Entorno Python 3.11 configurado
- [x] Dependencias iniciales instaladas
- [x] Fuente de video externa configurada
- [x] Flujo del celular validado con OpenCV
- [ ] YOLO probado sobre imagen
- [ ] YOLO probado sobre cámara
- [ ] Detección de `person` y `cell phone`

### Cámara utilizada durante el desarrollo

Debido a que el equipo utilizado para las pruebas iniciales no dispone
de una webcam física, se utiliza temporalmente un teléfono móvil mediante
DroidCam.

El flujo de video es recibido por OpenCV mediante una dirección HTTP
configurada localmente a través de la variable de entorno `CAMERA_URL`.

Ejemplo:

```powershell
$env:CAMERA_URL="http://IP_DEL_DISPOSITIVO:4747/video"
python ai/inference/camera_test.py