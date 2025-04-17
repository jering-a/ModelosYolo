# 🧠 Scripts utiles usados con gran frecuencia

## detect.py

Script para poder utilizar el modelo de detección con la camara integrada de tu computador.

Es la forma mas simple y rapida para probar un modelo recién entrenado

## inspec.py

Script para poder revisar las caractristicas de un modelo que no se le conoce la procedencia, versión de yolo y clases que detecta.

## revisarlabels.py

Scrpit para recorrer un dataset y confirmar que cada label tenga su imagen correspondiente (cambiar logica si se quiere al revés). 

Es de mucha utilidad cuando estas limpiando un dataset en local y eliminaste un label o una imagen pero no su correspondiente. Con él podemos tener la lista de los que no se encuentran emparejados.

## transformar.py

Script para poder transformar los indices de las categorías de las labels.

Sucede muchas veces que los indices no se corresponden con los indices que tiene el archivo .yaml, esto debido a que estamos juntando dos dataset en uno, lo importante es que solamente corresponda el numero del indice de la categoría, los nombres de las categorias no se trabajan al momento de procesar.