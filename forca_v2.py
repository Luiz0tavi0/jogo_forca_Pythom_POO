# -*- coding: utf-8 -*-
# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos


# Import
import random


# Board (tabuleiro)

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
	|
	|
	|
	|
=========''', '''

+---+
|   |
O   |
	|
	|
	|
=========''', '''

+---+
|   |
O   |
|   |
	|
	|
=========''', '''

 +---+
 |   |
 O   |
/|   |
	 |
	 |
=========''', ''' +---+
 |   |
 O   |
/|\  |
	 |
	 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
	 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
	 |
=========''']


# Classe
class Hangman:

	# Método Construtor

	def __init__(self, word):
		self.word = word
		self.secret_word = self.hide_word()
		self.wrong_letter = []
		self.accept_letter = []

	# Método para advinhar a letra
	def guess(self):
#		print('emtrou no guess')
		letter = str(input())
		if not letter in self.word:
			self.wrong_letter.append(letter)
#			print('entrou errado21')
		else:
			self.accept_letter.append(letter)
			positions = [indice for indice,valor in enumerate(self.word) if valor == letter]
			self.secret_word = list(self.secret_word)
			for pos in positions: self.secret_word[pos] = letter
			self.secret_word = ''.join(self.secret_word)
########print('entrou errado')


	# Método para verificar se o jogo terminou
	def hangman_over(self):
		# se ganhou ou perdeu, respectivamente
		return self.hangman_won() or len(self.wrong_letter) > 5

	# Método para verificar se o jogador venceu
	def hangman_won(self):
		return self.secret_word == self.word

	# Método para não mostrar a letra da palavra correta no board
	def hide_word(self):
		return '_' * len(self.word)

	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[len(self.wrong_letter)])
		print('Palavra: {}'.format(self.secret_word))
		print('Letras erratas:')
		print('\n'.join(self.wrong_letter))
		print('Letras corretas:')
		print('\n'.join(self.accept_letter))


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
	with open("palavras.txt", "rt") as f:
		bank = f.readlines()
		return bank[random.randint(0, len(bank) - 1)].strip()


# Função Main - Execução do Programa
def main():
	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over():
		# Verifica o status do jogo
		game.print_game_status()
		game.guess()

	game.print_game_status()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print('\nParabéns! Você venceu!!')
	else:
		print('\nGame over! Você perdeu.')
		print('A palavra era ' + game.word)

	print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
	main()
