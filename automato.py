# Definições

import actions
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

        self.trap_state = State('qt', myAction, [], False)
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
        self.current_state.action()

    def readWord(self, word):
        self.current_state = self.getState('q0')
        self.current_state.action()
        for character in word:
            self.readSymbol(character)
        if self.current_state.isFinal:
            print("ACEITA")
        else:
            print("REJEITA")


# Testes:
def myAction():
    print('Action!')


def askName():
    name = input('Digite seu nome: ')
    print("Olá " + name + "!")


q0 = State(
    'q0',  # 'Menu inicial',
    actions.menu,
    [Transition('q', 'q1'), Transition('b', 'q2')],
    True
)
q1 = State(
    'q1',  # 'Quit game',
    actions.quit_game,
    [],
    True
)
q2 = State(
    'q2',  # 'Hall de entrada',
    myAction,
    [Transition('e', 'q3'), Transition('c', 'q11')],
    False
)
q3 = State(
    'q3',  # 'Andar de cima',
    myAction,
    [Transition('w', 'q4'), Transition('c', 'q7'), Transition('r', 'q2')],
    False
)
q4 = State(
    'q4',  # Quarto',
    myAction,
    [Transition('g', 'q5'), Transition('t', 'q6'), Transition('r', 'q3')],
    False
)
q5 = State(
    'q5',  # 'Garrafa de veneno',
    myAction,
    [],
    False
)
q6 = State(
    'q6',  # 'Televisão: câmera de segurança',
    myAction,
    [Transition('t', 'q6'), Transition('r', 'q4')],
    False
)
q7 = State(
    'q7',  # 'Corredor do andar de cima',
    myAction,
    [Transition('n', 'q8'), Transition('p', 'q9')],
    False
)
q8 = State(
    'q8',  # 'Papel com recado',
    myAction,
    [Transition('r', 'q7')],
    False
)
q9 = State(
    'q9',  # 'Porta',
    myAction,
    [Transition('h', 'q10'), Transition('s', 'q17')],
    False
)
q10 = State(
    'q10',  # 'Pulou da janela e morreu',
    myAction,
    [],
    False
)
q11 = State(
    'q11',  # 'q11',
    myAction,
    [Transition('a', 'q12'), Transition('p', 'q15'), Transition('r', 'q2')],
    False
)
q12 = State(
    'q12',  # 'Alçapão',
    myAction,
    [Transition('c', 'q13'), Transition('r', 'q12')],
    False
)
q13 = State(
    'q13',  # 'Corredor do alçapão',
    myAction,
    [Transition('p', 'q14'), Transition('r', 'q12')],
    False
)
q14 = State(
    'q14',  # 'Preso no alçapão',
    myAction,
    [Transition('r', 'q14')],
    False
)
q15 = State(
    'q15',  # 'Viu a luz da janela',
    myAction,
    [Transition('l', 'q16'), Transition('r', 'q15')],
    False
)
q16 = State(
    'q16',  # 'Foge para o jardim pela janela',
    myAction,
    [Transition('j', 'q17')],
    False
)
q17 = State(
    'q17',  # 'Jardim de saída',
    myAction,
    [],
    True
)

myAut = Automato([q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17],
                 ['q', 'b', 'e', 'r', 'c', 'w', 'g', 't', 'p', 'n', 'h', 's', 'j', 'l', 'a'], 'q0')

myAut.readWord('q')