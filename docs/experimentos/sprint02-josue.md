# Sprint 02 - Preparación del dataset

## Objetivo

Preparar la estructura de datos para entrenamiento,
validación y pruebas.

## Clases

| ID | Clase |
|---|---|
| 0 | person |
| 1 | cell phone |

## Estructura

data/dataset/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
└── labels/
    ├── train/
    ├── val/
    └── test/

## Validaciones realizadas

- Carpetas inexistentes
- Imágenes con extensiones inválidas
- Imágenes sin etiqueta
- Etiquetas sin imagen correspondiente
- Etiquetas vacías
- Clases diferentes de 0 y 1
- Valores fuera del rango permitido

## Problemas encontrados

Por el momento ninguno, la estructura y scripts se generaron correctamente.

## Conclusiones

La estructura de datos YOLO y las herramientas de validación están listas para la incorporación del dataset.
