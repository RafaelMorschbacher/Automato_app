from classes import State, Transition
import actions

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
    actions.entry_hall,
    [Transition('e', 'q3'), Transition('c', 'q11'), Transition('m', 'q0'),  Transition('z', 'q19')],
    False
)
q3 = State(
    'q3',  # 'Andar de cima',
    actions.second_floor,
    [Transition('w', 'q4'), Transition('c', 'q7'), Transition('r', 'q2'), Transition('m', 'q0')],
    False
)
q4 = State(
    'q4',  # Quarto',
    actions.bedroom,
    [Transition('g', 'q5'), Transition('t', 'q6'), Transition('r', 'q3'), Transition('m', 'q0')],
    False
)
q5 = State(
    'q5',  # 'Garrafa de veneno',
    actions.bottle,
    [],
    True
)
q6 = State(
    'q6',  # 'Televisão: câmera de segurança',
    actions.television,
    [Transition('t', 'q6'), Transition('r', 'q4'), Transition('m', 'q0')],
    False
)
q7 = State(
    'q7',  # 'Corredor do andar de cima',
    actions.second_floor_hall,
    [Transition('n', 'q8'), Transition('p', 'q9'), Transition('m', 'q0')],
    False
)
q8 = State(
    'q8',  # 'Papel com recado',
    actions.paper_note,
    [Transition('r', 'q7'), Transition('m', 'q0')],
    False
)
q9 = State(
    'q9',  # 'Porta',
    actions.door_second_floor,
    [Transition('h', 'q10'), Transition('s', 'q17'), Transition('m', 'q0')],
    False
)
q10 = State(
    'q10',  # 'Pulou da janela e morreu',
    actions.window_jump,
    [],
    True
)
q11 = State(
    'q11',  # 'q11',
    actions.first_floor_hall,
    [Transition('a', 'q12'), Transition('p', 'q15'), Transition('r', 'q2'), Transition('m', 'q0')],
    False
)
q12 = State(
    'q12',  # 'Alçapão',
    actions.trapdoor,
    [Transition('c', 'q13'), Transition('r', 'q12'), Transition('m', 'q0')],
    False
)
q13 = State(
    'q13',  # 'Corredor do alçapão',
    actions.loft_hall,
    [Transition('p', 'q14'), Transition('r', 'q12'), Transition('m', 'q0')],
    False
)
q14 = State(
    'q14',  # 'Preso no alçapão',
    actions.door_prision,
    [Transition('r', 'q14'), Transition('m', 'q0')],
    True
)
q15 = State(
    'q15',  # 'Viu a luz da janela',
    actions.door_first_floor,
    [Transition('l', 'q16'), Transition('r', 'q18'), Transition('m', 'q0')],
    False
)
q16 = State(
    'q16',  # 'Foge para o jardim pela janela',
    actions.window_first_floor,
    [Transition('j', 'q17'), Transition('m', 'q0')],
    False
)
q17 = State(
    'q17',  # 'Jardim de saída',
    actions.garden_of_freedom,
    [],
    True
)

q18 = State(
    'q18', #Tentativa de voltar pela porta
    actions.door_is_locked,
    [Transition('r', 'q18'), Transition('l', 'q16'), Transition('m', 'q0')],
    False
)
q19 = State(
    'q19', #Tentativa de sair da casa pela porta principal 
    actions.main_door_is_locked,
    [Transition('e', 'q3'), Transition('c', 'q11'), Transition('m', 'q0')],
    False
)