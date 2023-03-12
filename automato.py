# Definições

class State:
    def __init__(self, id, action, transitions ,isFinal):
        self.id = id
        self.action = action
        self.transitions = transitions
        self.isFinal = isFinal

    def getTransition(self, symbol):
        for transition in self.transitions:
            if transition.symbol == symbol:
                return transition

class Transition:
    def __init__(self, symbol, dst):
        self.symbol = symbol
        self.dst = dst


class Automato:
    def __init__(self, states, alph, current_state_id):
        self.states = states
        self.alph = alph
        self.current_state = self.getState(current_state_id)
        
    def getState(self, id):
            for state in self.states:
                if state.id == id:
                    return state
            return False

    def readSymbol(self, symbol):
        transition = self.current_state.getTransition(symbol)
        self.current_state = self.getState(transition.dst)
        self.current_state.action()
    def readWord(self, word):
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
    'Menu inicial',
    askName,
    [Transition('q', 'q1'), Transition('b', 'q2')],
    False
)
q1 = State(
    'Quit game',
    myAction,
    [],
    True
)
q2 = State(
    'Hall de entrada',
    myAction,
    [Transition('e', 'q3'), Transition('c', 'q11')],
    False
)
q3 = State(
    'Andar de cima',
    myAction,
    [Transition('w', 'q4'), Transition('c', 'q7'), Transition('r', 'q2')],
    False
)
q4 = State(
    'Quarto',
    myAction,
    [Transition('g', 'q5'), Transition('t', 'q6'), Transition('r', 'q3')],
    False
)
q5 = State(
    'Garrafa de veneno',
    myAction,
    [],
    False
)
q6 = State(
    'Televisão: câmera de segurança',
    myAction,
    [Transition('t', 'q6'), Transition('r', 'q4')],
    False
)
q7 = State(
    'Corredor do andar de cima',
    myAction,
    [Transition('n', 'q8'), Transition('p', 'q9')],
    False
)
q8 = State(
    'Papel com recado',
    myAction,
    [Transition('r', 'q7')],
    False
)
q9 = State(
    'Porta',
    myAction,
    [Transition('h', 'q10'), Transition('s', 'q17')],
    False
)
q10 = State(
    'Pulou da janela e morreu',
    myAction,
    [],
    False
)
q11 = State(
    'Corredor do andar térreo',
    myAction,
    [Transition('a', 'q12'),  Transition('p', 'q15'), Transition('r', 'q2')],
    False
)
q12 = State(
    'Alçapão',
    myAction,
    [Transition('c', 'q13'), Transition('r', 'q12')],
    False
)
q13 = State(
    'Corredor do alçapão',
    myAction,
    [Transition('p', 'q14'), Transition('r', 'q12')],
    False
)
q14 = State(
    'Preso no alçapão',
    myAction,
    [Transition('r', 'q14')],
    False
)
q15 = State(
    'Viu a luz da janela',
    myAction,
    [Transition('l', 'q16'), Transition('r', 'q15')],
    False
)
q16 = State(
    'Foge para o jardim pela janela',
    myAction,
    [Transition('j', 'q17')],
    False
)
q17 = State(
    'Jardim de saída',
    myAction,
    [],
    True
)



myAut = Automato([q0,q1], ['a','b'], 'q0')

myAut.readWord('abbaaa')
