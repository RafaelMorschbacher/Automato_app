# Definições

from states import *
from classes import State, Automato, Transition
from time import sleep


# Testes:


myAut = Automato([q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17],
                 ['q', 'b', 'e', 'r', 'c', 'w', 'g', 't', 'p', 'n', 'h', 's', 'j', 'l', 'a'], 'q0')

print('--------------------')
print('JOGO DE ESCOLHAS COM AUTÔMATO FINITO')
print('--------------------')
sleep(1)
print("Digite 'a' para ler um arquivo com palavra de entrada.")
sleep(0.5)
print("Digite 'j' para jogar o jogo")
sleep(0.5)
print("Digite 'p' para entrar com uma palavra")
sleep(0.5)
print('--------------------')

user_input = input("Sua escolha: ").lower()
if user_input == 'a':
    print("arquivo")
elif user_input == 'j':
    myAut.playGame()
elif user_input == 'p':
    word = input("Digite a palavra que você deseja ler: ")
    myAut.readWord(word)
#myAut.readWord('bcprlj')
#myAut.playGame()