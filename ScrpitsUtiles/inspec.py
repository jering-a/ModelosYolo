from ultralytics import YOLO

import importlib


# Cargar el modelo YOLO
model = YOLO("yolo11x.pt")

# Ver información del modelo
model.info()

# Ver las clases detectadas
print(model.names)






