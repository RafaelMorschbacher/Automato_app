from time import sleep

# Aviso de transição indefinida
def undef_transition_warning():
    print("Transição indefinida\n")
    sleep(1)
    return None

# Classe de estado, guardando as transições e booleano que indca ser final u não, um ID de identificação e uma ação. 
#Cada estado representa um ambiente em que o jogador se encontra
class State:
    def __init__(self, id, action, transitions, isFinal):
        self.id = id
        self.action = action
        self.transitions = transitions
        self.isFinal = isFinal

    def getTransition(self, symbol):
        for transition in self.transitions:
            if transition.symbol == symbol:
                return transition
        return False

#Instâncias da classe Transição é guardada em uma lista dentro de cada estado
# Cada transição representa uma ação do jogador
class Transition:
    def __init__(self, symbol, dst):
        self.symbol = symbol
        self.dst = dst


# Classe que reppresenta a SAÍDA do autômato, com mensagem, booleano de aceita/rejeita e palavra final
class Output:
    def __init__(self, is_accepted, message, final_word):
        self.is_accepted = is_accepted
        self.message = message
        self.final_word = final_word

# CLasse do autômato em si, que guarda todos os seus estados com suas transições, alfabeto e um estado atual, que muda conforme a leitura
# A indefinição é tratada pela própria classe, tanto por transição indefinida quanto por símbolo fora do alfabeto.
class Automato:
    def __init__(self, states, alph, current_state_id):
        self.states = states
        self.alph = alph
        self.current_state = self.getState(current_state_id)

        # Criação de um 'trap state' em tempo de execução e envio de todas as transições indefinidas para ele.
        self.trap_state = State('qt', undef_transition_warning, [], False)
        self.states.append(self.trap_state)

        for state in self.states:
            for symbol in alph:
                if not state.getTransition(symbol):
                    undef_transition = Transition(symbol, 'qt')
                    state.transitions.append(undef_transition)

    #A partir de u ID, como 'q2', retorna o estado com aquele ID
    def getState(self, id):
        for state in self.states:
            if state.id == id:
                return state
        return False
    #Atualiza o estado atual do automato lendo um simbolo e sua respectiva transição no estado atual
    def readSymbol(self, symbol):
        if symbol not in self.alph:
            print("\nVocê quebrou as regras e digitou um símbolo fora do alfabeto definido!")
            sleep(1)
            self.current_state = self.trap_state

        else:
            transition = self.current_state.getTransition(symbol)
            self.current_state = self.getState(transition.dst)

    #Itera leitura de simbolo para uma palavra inteira
    # Retorna um OUtput com atributos definidos na classe
    def readWord(self, word):
        self.current_state = self.getState('q0')
        # self.current_state.action()
        for character in word:
            self.readSymbol(character)

        end_state = self.current_state
        if end_state.isFinal:
            return Output(True, f'Palavra {word} ACEITA', word)
        else:
            if end_state.id == 'qt':
                return Output(False, f'Palavra {word} REJEITADA por INDEFINIÇÃO', word)
            else:
                return Output(False, f'Palavra {word} REJEITADA por ESTADO NÃO-FINAL', word)
    #Recebe input do jogador (letra por letra) e realiza uma ação de cada estado por vez
    #O jogador decide as letras com base nas ações que ele quer realizar dentre as disponíveis, e no final recebe um Output da palavra completa
    def playGame(self):

        self.current_state = self.getState('q0')
        is_playing = True
        final_word = ""

        print('\n--------------')
        print('JOGO INICIADO')
        print('--------------\n')
        sleep(2)
        print('----------------------------------------------------------------------------------------------------------------')
        print('INSTRUÇÕES:') 
        print(" - Você deve digitar apenas um símbolo da sua palavra por vez;") 
        print(" - Cada símbolo representa uma AÇÃO do jogador;") 
        print(" - Para parar de digitar os símbolos, digite 'END';") 
        print(" - Digite apenas símbolos pertencentes ao alfabeto, senão a leitura será interrompida;") 
        print(" - Escolha a sua ação apenas entre as opções disponíveis, senão a leitura será interrompida;") 
        print(" - Sua gameplay só será aceita se você terminar em um FINAL da história ou se SAIR do jogo pelo menu inicial.")
        print('----------------------------------------------------------------------------------------------------------------')
        sleep(7)

        self.current_state.action()

        while is_playing:
            print('----------------------------------------------')
            user_input = input("Digite o próximo símbolo: ")
            sleep(1)
            if user_input.lower() == 'end':
                is_playing = False

            else:
                self.readSymbol(user_input)
                self.current_state.action()
                final_word = final_word + user_input
                #Se o user der quit game ou simbolo indefinido, parar o jogo
                if self.current_state == self.trap_state or user_input.lower() == 'q' or self.current_state.isFinal:
                    is_playing = False

        end_state = self.current_state

        if end_state.isFinal:
            return Output(True, f'Palavra {final_word} ACEITA', final_word)
        else:
            if end_state.id == 'qt':
                return Output(False, f'Palavra {final_word} REJEITADA por INDEFINIÇÃO', final_word)
            else:
                return Output(False, f'Palavra {final_word} REJEITADA por ESTADO NÃO-FINAL', final_word)
