from states import *
from classes import State, Automato, Transition
from time import sleep

def get_word_from_file(file):
    lines = file.readlines()
    word = []
    for line in lines:
        word.append(line.strip())
    word_string = ''
    for i in word:
        word_string = word_string + i
    return word_string

myAut = Automato([q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19],
                 ['q', 'b', 'e', 'r', 'c', 'w', 'g', 't', 'p', 'n', 'h', 's', 'j', 'l', 'a', 'm', 'z'], 'q0')

print('\n')
print('-------------------------------------')
print('ESCAPE ROOM COM AUTÔMATO FINITO')
print('-------------------------------------')
sleep(2)


user_input = ''
while user_input != 'off':
    sleep(0.5)
    print('-------------------------------------')
    print("Digite 'j' para jogar o jogo")
    sleep(0.5)
    print("Digite 'a' para ler um arquivo com palavra de entrada.")
    sleep(0.5)
    print("Digite 'p' para entrar com uma palavra")
    sleep(0.5)
    print("Digite 'off' para fechar o programa")
    print('-------------------------------------')
    user_input = input("Sua escolha: ").lower()
    sleep(1)

    if user_input == 'j':
        output_automato = myAut.playGame()

        print("\nPalavra completa: " + output_automato.final_word)
        print(output_automato.message)


    elif user_input == 'a':
        
        file_name = input("Digite o nome do arquivo sem a extensão: ") + '.txt'
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

    else:
        if user_input != 'off':
            sleep(0.5)
            print("Opção inválida. Por favor, selecione uma das opções listadas")
            sleep(1)
