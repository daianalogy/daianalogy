import os
import re
import mutagen
import sys

def autotag(path, album):
    for filename in os.listdir(path):
        try:
            
 # La condición siguiente utiliza el método match() para verificar si el inicio de la cadena de caracteres "filename" coincide con un patrón específico.
            if re.match(r'^\d+', filename) and filename.endswith('.mp3'):
                file_path = os.path.join(path, filename)
                audio = mutagen.File(file_path)
                song_number = re.search(r'\d+', filename).group()
                song_name =os.path.splitext(filename)[0].replace(song_number + '.','').strip()
        
                # Aquí reemplaza el titulo de la canción por el nombre del archivo
                audio.tags['TIT2'] = mutagen.id3.TIT2(encoding=2, text=[song_name])
                # Aquí se establece el nombre del álbum entero
                audio.tags['TALB'] = mutagen.id3.TALB(encoding=2, text=[album])
                #Aquí se guarda los nuevos metadatos del archivo.
                audio.save()
            else: 
                print("La carpeta no contiene archivos en formato .mp3,\nasegúrese de añadir las canciones en el formato correcto.")
                break
        except Exception as e:
            print("Cambia los permisos de tu carpeta e intenta nuevamente.")
            break
        else:
            print(F"Se actualizó metadatos de la canción: {song_name} correctamente.")
            sys.exit()

def collect():
    global path
    global album
    path = str(input("Proporcione la ruta de la carpeta: "))
    #Comprueba que la ruta exista sino pide corregir y cierra
    if os.path.exists(path):
        print("El directorio es válido...")
    # Comprueba que el directorio esté lleno.
        if len(os.listdir(path)) <= 0:
            print("...pero está vacío, por favor, agregue las canciones en formato .mp3 e intente nuevamente")   
            sys.exit()
        else:
            album = str(input("Ahora proporcione el nombre del álbum: "))        
    else:
        print("Por favor copie y pegue la ruta completa desde C: ")
        sys.exit()

collect()
autotag(path, album)
