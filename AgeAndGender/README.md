# 🧠 Conformación de dataset para edad y género

Para la conformación de este dataset se utilizaron varias fuentes de imágenes. Como se tenia el problema de que se necesitaba tener una edad asociada a la imagen de una persona, muchos datasets no se correspondían con esta necesidad.

Primeramente se pidio a cnocidos y gente de la oficina que nos aportaran con fotos de sus caras, lo cual nos dio un prototipo de modelo que a pesar de tener muchos errores ya mostraba avances en la detección.

El principal problema de esta solución es la baja escala en la cantidad ee imagenes. Teniendo 8 categorías por describir, se recomienda que cada categoria en un modelo Yolo tenga por lo menos 500 imagenes para lograr una caracterización fidedigna.

Es debido a lo anterior que se comenzó a utilizar wikidata, el cual  es una base de datos libre y colaborativa que almacena datos estructurados para ser usados por Wikipedia y otros proyectos de la Fundación Wikimedia, así como por cualquier persona o software que necesite datos abiertos y organizados. Para consultas semánticas usando SPARQL en . [Wikidata Query Service](https://query.wikidata.org/).

Asi se contruyó una consulta en formato tabla en este portal para poder una enorme fuente de imagenes de gente con sus edades asocidas

```bash
SELECT ?human ?humanLabel ?birthDate ?image WHERE {
  ?human wdt:P31 wd:Q5;                 # Debe ser un humano
         wdt:P27 wd:Q414;               # Debe ser Argentino
         wdt:P569 ?birthDate;           # Debe tener una fecha de nacimiento
         wdt:P18 ?image;                # Debe tener una imagen
         wdt:P21 wd:Q6581072.           # Debe ser mujer

  FILTER(YEAR(?birthDate) >= 1962 && YEAR(?birthDate) <= 1964)  # Filtra por año de nacimiento entre 

  FILTER NOT EXISTS { ?human wdt:P106 wd:Q937857 }  # Excluir futbolistas

  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],es" }
}
LIMIT 210
```


Gracias a esta herramienta, se pobló el dataset con imagenes de chilenos y argetinos, logrando así tener un dataset con una cantidad destacable de imaganes por categoría, dejando asi al modelo en un mejor porcentaje de acierto