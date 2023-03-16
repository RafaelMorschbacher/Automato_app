# Definições

from states import *
from classes import State, Automato, Transition


# Testes:


myAut = Automato([q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17],
                 ['q', 'b', 'e', 'r', 'c', 'w', 'g', 't', 'p', 'n', 'h', 's', 'j', 'l', 'a'], 'q0')

#myAut.readWord('bcprlj')
myAut.playGame()