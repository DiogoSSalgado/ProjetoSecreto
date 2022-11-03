# -*- coding: utf-8 -*-
import random
import os 

os.system('clear')
val = True
print("Digite seu nome:")
nome = input("->")
nome = nome.capitalize()
os.system('clear')

while True:
	num = random.randint(0,20)
	if val:
		print("8", end = '')
		for i in range(0, num):
			print ("=", end = '')
		if num == 1:
			print ("D\n" + nome+", o seu pênis é de", num, "centímetro!\n")
		else:
			if num == 0:
				print ("D\n" + nome+", o seu pênis é inexistente.\n")
			else:
				print ("D\n" + nome+", o seu pênis é de", num, "centímetros!\n")
		val = False
	else:
		print("Calcular novamente?(S/N)")
		pergunta = input("->")
		if pergunta == "S" or pergunta == "s":
			print("\nTrocar nome?(S/N)")
			newnome = input("->")
			newnome = newnome.capitalize()
			os.system('clear')
			
			if newnome == "S" or newnome == "s":
				print("Digite o novo nome:")
				nome = input("->")
			else:
				if newnome == "N" or newnome == "n":
					print('')
				else:
					print("Opção inválida!")
			val = True
			os.system('clear')
			continue
		else:
			if pergunta == "N" or pergunta == "n":
				os.system('clear')
				break
			else:
				os.system('clear')
				continue

print("Programa encerrado. </3")

