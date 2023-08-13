import os
from config import carpetas_entrada, carpeta_salida
from pydub import AudioSegment
from mutagen.easyid3 import EasyID3

def obtener_metadatos_m4a(ruta):
    try:
        audio = EasyID3(ruta)
        return {
            "artist": audio.get("artist", [""])[0],
            "title": audio.get("title", [""])[0]
        }
    except:
        # Si no se pueden obtener metadatos, proporcionamos valores predeterminados
        return {
            "artist": "Artista desconocido",
            "title": "Título desconocido"
        }

def convertir_m4a_a_mp3(entradas):
    for carpeta in entradas:
        archivos = os.listdir(carpeta)
        for archivo in archivos:
            if archivo.endswith(".m4a"):
                archivo_m4a = os.path.join(carpeta, archivo)
                archivo_mp3 = os.path.join(carpeta_salida, os.path.splitext(archivo)[0] + ".mp3")
                
                # Verificar si el archivo .mp3 ya existe en la carpeta de salida
                if os.path.exists(archivo_mp3):
                    print(f"El archivo {archivo_m4a} ya ha sido convertido y existe en la carpeta de salida.")
                    continue

                # Leer el archivo .m4a y obtener los metadatos
                audio = AudioSegment.from_file(archivo_m4a, format="m4a")
                metadatos = obtener_metadatos_m4a(archivo_m4a)

                try:
                    # Guardar el archivo .mp3 con los metadatos originales
                    audio.export(archivo_mp3, format="mp3", tags=metadatos, bitrate="192k")
                    print(f"Canción convertida y guardada exitosamente: {archivo_mp3}")
                except Exception as e:
                    print(f"Error al convertir o guardar {archivo_m4a}: {e}")

# Llamada a la función convertir_m4a_a_mp3 utilizando las variables de config.py
convertir_m4a_a_mp3(carpetas_entrada)

