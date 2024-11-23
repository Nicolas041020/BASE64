**Base 64 y Curl**

Este proyecto se basa en hacer peticiones a una base de datos, meter los datos a sqlite en binario y cuando hagamos la peticion los pasamos a base 64 para que al hacer la peticion desde la terminal de linux nos aparezca la imagen en base 64 y si hacemos la peticion en la web nos aparezca la imagen normal

**Consideración**

La carpeta que dice cgi-binl en este repositorio hace como si fuera el directrio de linux /usr/lib/cgi-bin por lo tanto para que este proyecto funcione lo que esta dentro de esa carpeta debe estar en el directorio anteriormente mencionado.

El script de python de base_datos.py crea la base de datos y agrega las imagenes que estan dentro de la carpeta y el consultas.py es el archivo que hace las consultas en la base de datos.
