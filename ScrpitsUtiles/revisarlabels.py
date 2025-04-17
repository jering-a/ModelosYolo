import os

# Rutas
images_dir = 'obj_train_data/images/train'        # Cambia esta ruta
labels_dir = 'obj_train_data/labels/train'       # Cambia esta ruta

# Extensiones de imagen aceptadas
image_extensions = ('.jpg', '.jpeg', '.png')

# Listar nombres base de imágenes
image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(image_extensions)]
image_names = [os.path.splitext(f)[0] for f in image_files]

# Verificar si cada imagen tiene un archivo de etiqueta correspondiente
missing_labels = []
for name in image_names:
    label_path = os.path.join(labels_dir, f"{name}.txt")
    if not os.path.exists(label_path):
        missing_labels.append(name)

# Mostrar resultados
if missing_labels:
    print("Imágenes sin etiqueta:")
    for name in missing_labels:
        print(name)
else:
    print("Todas las imágenes tienen su archivo de etiqueta.")
