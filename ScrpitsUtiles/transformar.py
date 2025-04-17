import os

# Define la carpeta donde están los archivos .txt
annotations_folder = "labels"

# Mapea los índices actuales a los nuevos índices
class_mapping = {
    0: 1,  # Ejemplo: cambiar clase 0 a 1
    1: 0  # Ejemplo: cambiar clase 1 a 2 
}

# Procesar todos los archivos .txt en la carpeta
for filename in os.listdir(annotations_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(annotations_folder, filename)

        with open(file_path, "r") as file:
            lines = file.readlines()

        updated_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) > 0:
                class_index = int(parts[0])  # Índice de la clase actual
                if class_index in class_mapping:
                    parts[0] = str(class_mapping[class_index])  # Reemplazo
                updated_lines.append(" ".join(parts))

        # Sobreescribe el archivo con los índices actualizados
        with open(file_path, "w") as file:
            file.write("\n".join(updated_lines) + "\n")

print("Índices de clases actualizados correctamente.")
