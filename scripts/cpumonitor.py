#!/usr/bin/#!/usr/bin/env python3
'''
Esta es la creación de mi script que servirá para monitorear
el estado de salud de mi CPU por un tiempo y guardar los resultados
dentro de una carpeta llamada "health cpu"

'''
import psutil
import os
import time


def nueva_carpeta(carpeta, archivo): #    Se define la función
    if os.path.isdir(carpeta) == False:  # Se comprueba si la carpeta existe
        os.mkdir(carpeta)  #    Si no existe la crea
    os.chdir(carpeta) #  Si existe, abrirá la crear_carpeta_archivo
    secs = 300
    hora = time.strftime('%H.%M', time.localtime())
    fecha = time.strftime('%Y-%m-%d', time.localtime())
    uso = psutil.cpu_percent(secs)
    aviso = f"Se ha guardado correctamente los datos porcentuales del uso de su CPU en la carpeta HEALTH CPU "
    with open (archivo, "a") as archivo: #    Aquí se creará el archivo, si existe sólo añadirá una línea
        archivo.write(f"\nEl CPU estuvo usándose hoy {fecha} un {uso}% desde las {hora}hrs")
#  En la línea de arriba, dependiendo del tipo de archivo y requerimientos, escribimos dentro archivo.
    os.chdir('..')# Ésta linea nos saca de la carpeta creada
    return aviso # Imprime que la tarea se completó satisfactoriamente.

global mins
global archivo
#ext = ".txt"
#saludo = "Hola, ¿por cuántos minutos deseeas monitorear tu CPU?: "
notif = "Estamos procesando su petición, por favor espera que transcurra el tiempo"
#print(saludo)
#mins = int(input())
print(notif)
archivo = time.strftime('%Y-%m-%d ', time.localtime())+ '.txt'
print(nueva_carpeta("health cpu", archivo))
time.sleep(5)
