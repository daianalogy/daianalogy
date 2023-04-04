#!/usr/bin/env python3

import openai
import config
import typer
import sys
from gtts import gTTS
from playsound import playsound
from rich import print
from rich.table import Table
import time


#pregunta = sys.argv[1]

def main():
	openai.api_key = config.api_key
	cont = "s"
	play = "n"
	def tts(fileaudio):
		tts = gTTS(fileaudio, lang='es', tld='com.mx', slow=False)
		tts.save("output.mp3")
		return


	print("[bold green]¡Hola! Soy tu asistente, aprende a interactuar conmigo[/bold green]")
	table = Table("Comando", "Descripcion")
	table.add_row("exit", "Salir de la app")
	print(table)


	# Contexto del asistente

	messages = [{"role":"system",
	"content": "Eres un asistente de traducción y programación en Python y Linux Bash Shell, con amplios conocimientos en DevOps y sus herramientas, así como también de criptomonedas y tecnología en general."}]

	while(cont.lower() == "s"):
	
	
		content = typer.prompt("¿Dime en qué puedo ayudarte?\n ")
	
		if content == "exit":
			confir = typer.confirm('Seguro?')
			if confir == False:
				continue
			else: 
				print("[bold green]Saliendo del asistente...[/bold green]")
				break
	
		print("[gray]Pensando...[/gray]")
	
		messages.append({"role": "user", "content": content})
	
		completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
											  messages=messages)
	
														
		respuesta = completion.choices[0].message.content
		messages.append({"role": "assistant", "content": respuesta})	
		tts(respuesta)
		print(f'[bold purple] >> [/bold purple][bold blue]{respuesta}[/bold blue]')
	
		play = input("\n¿Escuchar?[s/N] : ")
		if play == "s":
			playsound('output.mp3')
		elif play == "exit":
			typer.Abort()
			print("[bold green]Saliendo del asistente...[/bold green]")
			break
		else:
			pass


if __name__ == "__main__":
	typer.run(main)




