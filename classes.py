
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
        transition = self.current_state.getTransition(symbol)
        self.current_state = self.getState(transition.dst)
        # print(self.current_state)
        # import pdb
        # pdb.set_trace()
        #self.current_state.action()

    def readWord(self, word):
        self.current_state = self.getState('q0')
        #self.current_state.action()
        for character in word:
            self.readSymbol(character)
        if self.current_state.isFinal:
            print("ACEITA")
        else:
            print("REJEITA")


    def playGame(self):

        self.current_state = self.getState('q0')
        is_playing = True

        print('\n--------------------')
        print('JOGO INICIADO')
        print('INSTRUÇÕES: ')
        print(" - Cada símbolo da sua palavra será digitado de uma vez")
        print(" - Cada símbolo equivale a uma AÇÃO do jogador")
        print(" - Para parar de digitar símbolos, digite END")
        print(" - Sua gameplay só será aceita se você terminar em um FINAL da história ou SAIR pelo menu")
        print('--------------------')

        self.current_state.action()

        while is_playing:
            user_input = input("Digite o próximo símbolo:")
            if user_input.lower() == 'end':
                is_playing = False
            else:
                self.readSymbol(user_input)
                self.current_state.action()
        if self.current_state.isFinal:
            print("ACEITA")
        else:
            print("REJEITA")