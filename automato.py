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
    'q0',
    askName,
    [Transition('a', 'q1'), Transition('b', 'q0')],
    False
)

q1 = State(
    'q1',
    myAction,
    [Transition('a', 'q0'), Transition('b', 'q1')],
    True
)


myAut = Automato([q0,q1], ['a','b'], 'q0')

myAut.readWord('abbaaa')
