#!/usr/bin/env python3

import openai
import sys

openai.api_key = "AQUI VA TU API KEY"

print("Bienvenido a ChatGPT")

cont = "s"
pregunta = sys.argv[1]

while(cont.lower() == "s"):
	
	
	#pregunta = input("\n¿Dime en qué puedo ayudarte?\n ")
		
	if pregunta == "exit":
		break
	
	completion = openai.Completion.create(engine = "text-davinci-003",
										  prompt = pregunta, 
										  max_tokens = 2048)										 
	print(completion.choices[0].text)
	
	cont = input("\n¿Tienes más dudas? [s para continuar/N] ")
	if cont == "s":
		pregunta = input("\n¿Dime en qué puedo ayudarte?\n ")
	else:
		break
		

