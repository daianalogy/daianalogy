#!/bin/bash
<< 'MULTILINE-COMMENT'

NOTE: Éste script renombrará todos los archivos que terminen en cierta extensión 
y estén contenidos dentro del directorio ACTUAL. Itera sobre los archivos que
terminan en .HTM y los renombra por .html, Antes ejecutar éste script es recomendable 
comprobar que se apliquen los resultados esperados, usar con precaución.

Reemplace .HTM por la extensión de sus archivos de origen.
Reemplace .html concatenada en la variable $name por la extensión nueva.

Mientras tengamos el comando echo al inicio de la línea 25 el script sólo mostrará
por pantalla la modificación que haría, si el resultado que muestra es el que 
deseas, para aplicar el cambio permanetemente, borra el comando echo de la línea 25.


MULTILINE-COMMENT


for file in *.HTM; do 

	name=$(basename "$file" .HTM) 

: 
	echo mv "$file" "$name.html"
done