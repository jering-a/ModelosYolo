import cv2
from ultralytics import YOLO

# Cargar modelo YOLO en formato .pt
model = YOLO("bestGunFinalFinalAhoraSiQueFinalMegaPREMIUM.pt")

# Iniciar captura de video desde la cámara (0 = webcam principal)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar detección
    results = model(frame)

    # Obtener nombres de las clases
    class_names = model.names  # Diccionario de nombres de clases

    # Filtrar detecciones con confianza > x
    high_conf_detections = []
    for result in results:
        for box in result.boxes:
            if box.conf[0] > 0.6:  # Confianza de la detección
                high_conf_detections.append(box)

    # Crear una imagen con solo las detecciones filtradas
    annotated_frame = frame.copy()
    for box in high_conf_detections:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas de la caja
        cls_id = int(box.cls[0])  # ID de la clase detectada
        class_label = class_names.get(cls_id, "Desconocido")  # Obtener el nombre de la clase
        confidence = box.conf[0]  # Confianza de la detección

        label = f"{class_label}: {confidence:.2f}"  # Etiqueta con clase y confianza
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Dibujar caja
        cv2.putText(annotated_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.5, (0, 255, 0), 2)  # Dibujar etiqueta

    # Mostrar el video con detecciones filtradas
    cv2.imshow("Detección en Vivo", annotated_frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
