#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  pdfgenerator.py
#  
#  Copyright 2023 reithe <reithe@GlaceOS>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie


# Se instancia el objeto "Estilos"
styles = getSampleStyleSheet()
# Se indica la ruta de guardado el archivo
report = SimpleDocTemplate("/home/reithe/pets.pdf")
# Se coloca el título del archivo junto a el tamaño de letra pasado como 2do parámetro.
report_title = Paragraph("A Complete Inventory of My Pets", styles["h1"])
# Se le da formato a la tabla
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
# Se instancia el objeto dibujo
report_chart = Drawing()
# Se instancia objeto Pie
report_pie = Pie()
# Se formatea el Pie
Pie.x = 150
Pie.y = 150
Pie.width = 100
Pie.height = 100
# Se añade objeto Pie en Dibujo
report_chart.add(report_pie)

# Esta es el diccionario de datos que se usará para ésta prueba
mascotas = {
	"Taroshi" : 1.4,
	"Minichee" : 2.4,
	"Figaro" : 1.4,
	"Cheetara II" : 0.5,
	"Turrón" : 0.5,
	"Pauline" : 0.5,
	"Vetti" : 0.5,
	
}

''' Convertir el diccionario en una lista de listas para que se pueda
mostrar en una tabla '''

tabla_pets = list()
for key, value in mascotas.items():
	tabla_pets.append([key, value])
print(tabla_pets)

# Convertir el dict en un formato para hacer un reporte en forma de pie

report_pie.data = list()
report_pie.labels = list()	
for pet_name in sorted(mascotas):
	report_pie.data.append(mascotas[pet_name])
	report_pie.labels.append(pet_name)
print(report_pie.data)
print(report_pie.labels)V

# Se pasa por parametro el contenido, estilo y alineación de la tabla.
report_table = Table(data=tabla_pets, style=table_style, hAlign="LEFT")
'''Se manda a generar el reporte en .pdf pasando como parametros una lista
con los objetos titulos, tabla, diagrama '''
report.build([report_title, report_table, report_chart])
