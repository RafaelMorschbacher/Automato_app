from states import *
from classes import State, Automato, Transition
from time import sleep

def get_word_from_file(file):
    lines = file.readlines()
    word = []
    for line in lines:
        word.append(line.strip())

    return word

myAut = Automato([q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17],
                 ['q', 'b', 'e', 'r', 'c', 'w', 'g', 't', 'p', 'n', 'h', 's', 'j', 'l', 'a'], 'q0')

print('--------------------')
print('JOGO DE ESCOLHAS COM AUTÔMATO FINITO')
print('--------------------')
sleep(1)
print("Digite 'j' para jogar o jogo")
sleep(0.5)
print("Digite 'a' para ler um arquivo com palavra de entrada.")
sleep(0.5)
print("Digite 'p' para entrar com uma palavra")
sleep(0.5)
print('--------------------')

user_input = input("Sua escolha: ").lower()

if user_input == 'j':
    output_automato = myAut.playGame()

    print(output_automato.message)


elif user_input == 'a':
    file_name = input("Digite o nome do arquivo:")
    try:
        input_file = open(file_name, 'r')
        word = get_word_from_file(input_file)
        output_automato = myAut.readWord(word)
        print('\n')
        print(output_automato.message)
    except:
        print("ERRO: Arquivo não encontrado.")


elif user_input == 'p':
    word = input("Digite a palavra que você deseja ler: ")
    output_automato = myAut.readWord(word)
    print(output_automato.message)
