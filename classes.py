from time import sleep

def undef_transition_warning():
    print("Transição indefinida")


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


class Transition:
    def __init__(self, symbol, dst):
        self.symbol = symbol
        self.dst = dst


class Output:
    def __init__(self, is_accepted, message):
        self.is_accepted = is_accepted
        self.message = message


class Automato:
    def __init__(self, states, alph, current_state_id):
        self.states = states
        self.alph = alph
        self.current_state = self.getState(current_state_id)

        self.trap_state = State('qt', undef_transition_warning, [], False)
        self.states.append(self.trap_state)

        for state in self.states:
            for symbol in alph:
                if not state.getTransition(symbol):
                    undef_transition = Transition(symbol, 'qt')
                    state.transitions.append(undef_transition)

    def getState(self, id):
        for state in self.states:
            if state.id == id:
                return state
        return False

    def readSymbol(self, symbol):
        if symbol not in self.alph:
            print("Você quebrou as regras e digitou um símbolo fora do alfabeto definido!")
            self.current_state = self.trap_state

        else:
            transition = self.current_state.getTransition(symbol)
            self.current_state = self.getState(transition.dst)


    def readWord(self, word):
        self.current_state = self.getState('q0')
        # self.current_state.action()
        for character in word:
            self.readSymbol(character)

        end_state = self.current_state
        if end_state.isFinal:
            return Output(True, 'Palavra ACEITA')
        else:
            if end_state.id == 'qt':
                return Output(False, 'Palavra REJEITADA por INDEFINIÇÃO')
            else:
                return Output(False, 'Palavra REJEITADA por ESTADO NÃO-FINAL')

    def playGame(self):

        self.current_state = self.getState('q0')
        is_playing = True

        print('\n--------------')
        print('JOGO INICIADO')
        print('--------------\n')
        sleep(2)
        print('-------------------------------------------------------------------------------------------')
        print('INSTRUÇÕES: ')
        print(" - Você deverá digitar apenas um símbolo da sua palavra por vez;")
        print(" - Cada símbolo equivale a uma AÇÃO do jogador;")
        print(" - Para parar de digitar os símbolos, digite 'END';")
        print(" - Digite apenas palavra pertencentes ao alfabeto.")
        print(" - Sua gameplay só será aceita se você terminar em um FINAL da história ou SAIR pelo menu.")
        print('-------------------------------------------------------------------------------------------')
        print("\n")
        sleep(7)

        self.current_state.action()

        while is_playing:
            user_input = input("Digite o próximo símbolo: ")
            if user_input.lower() == 'end':
                is_playing = False
            else:
                self.readSymbol(user_input)
                self.current_state.action()

        end_state = self.current_state

        if end_state.isFinal:
            return Output(True, 'Palavra ACEITA')
        else:
            if end_state.id == 'qt':
                return Output(False, 'Palavra REJEITADA por INDEFINIÇÃO')
            else:
                return Output(False, 'Palavra REJEITADA por ESTADO NÃO-FINAL')
