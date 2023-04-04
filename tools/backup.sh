#!/bin/bash
 
# Directorio que quieres respaldar (origen)
origdir=~/Plantillas

# Directorio donde se quiere guardar el respaldo
destdir=~/backup

# Lista los archivos recientes en dir origen que se respaldarán
recentfiles=$(find $origdir -mtime -1 -type f)
 
# Comprobar que el directorio origen existe
if [[ -d $origdir ]] ; then
        # Comprobar que el directorio destino existe
    if [[ -d $destdir ]] ; then
         # Hace la copia de seguridad en dest dir de los archivos recientes
         tar -czvf $destdir/backup.tar.gz $recentfiles
            echo
            echo "Copia de seguridad realizada correctamente"
    else
            echo "El directorio destino no existe pero se creará en "$destdir" vuelve a ejecutar"
            mkdir /home/reithe/backup
    fi
 
else
    echo "El directorio origen no existe, verifica la ruta"
fi
