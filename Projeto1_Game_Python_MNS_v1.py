# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

# Import random para a escolha aleatória da palavra a ser advinhada
# Import os para operar a função de limpar a tela após a execução do programa de acordo com o sistema operacional
# Import unicodedata para normalização de palavras acentuadas

import random
from os import system, name
import unicodedata

# Função para limpar a tela

def limpar_tela():
	# Windows
	if name == 'nt':
		_ = system('cls')
	# Mac / Linux
	else:
		_ = system('clear')

# Função para remover os acentos
def remover_acento(txt):
    return ''.join(
        c for c in unicodedata.normalize('NFD', txt)
        if unicodedata.category(c) != 'Mn'
	)
    
# Função do jogo

def game():
	limpar_tela()

	print("\nBoas-vindas ao jogo da Palavra Secreta, versão Dados!\n")
	print("Será que você consegue advinhar o termo da área de Dados a seguir antes que as chances esgotem?\n")

	# Lista de palavras a serem advinhadas (EM LETRA MAIÚSCULA)
	palavras = ['ALGORITMO', 'MEDIANA', 'AMOSTRAGEM', 'PROBABILIDADE', 'ESTIMATIVA', 'VARIÂNCIA', 'HIPÓTESE', 'ESTATÍSTICA', 'INFERÊNCIA', 'CORRELAÇÃO', 'FREQUÊNCIA', 'DISTRIBUIÇÃO']

	# Escolhe a palavra de forma aleatória
	palavra = random.choice(palavras)

	# Remove os acentos da palavra sorteada
	palavra_norm = remover_acento(palavra)

	# List comprehension
	letras_descobertas = ['_' for letra in palavra]

	# Lista para armazenar as tentativas de letras incorretas
	letras_erradas = []

	# Número de chances
	chances = 10

	
	while chances > 0:

		print(" ".join(letras_descobertas))
		print("\nChances restantes:", chances)
		print("Letras erradas:", " ".join(letras_erradas))

		tentativa = input("\nDigite uma letra: ").upper()

		if len(tentativa) != 1 or not tentativa.isalpha():
			print("Por favor, digite apenas um único caractere de letra.")
			continue 
		
		if tentativa in palavra_norm:
			index = 0

			for letra in palavra_norm:
				if tentativa == letra:
					letras_descobertas[index] = palavra[index]
				index += 1
		else:
			chances -= 1
			letras_erradas.append(tentativa)
		
		if "_" not in letras_descobertas:
			print("\nVocê venceu, a palavra é:", palavra)
			break
	
	if "_" in letras_descobertas:
		print("\nVocê perdeu, a palavra é:", palavra)

# Bloco main
if __name__ == "__main__":
	game()
	print("\nObrigada por jogar!\nPor: Maryana Nascimento")