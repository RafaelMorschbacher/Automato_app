from time import sleep

#q0
def menu(): 
    print("---------------MENU INICIAL---------------")
    print("Pressione b para iniciar uma nova história")
    print("Pressione q para sair do jogo")
    print('--------------------------------------------')

#q1
def quit_game(): 
    print("Você saiu do jogo.")

#q2
def entry_hall(): 
    print("Você está no hall de entrada de uma casa sombria. Você não se lembra como chegou até aqui e a porta está trancada.")
    sleep(5)
    print("À sua esquerda, há uma escada para o segundo andar da casa.")
    sleep(3)
    print("À sua direita, há um corredor mal iluminado.")
    sleep(3)
    print('--------------------------------------------')
    print("e: subir a escada")
    print("c: andar pelo corredor")
    print('--------------------------------------------')

#q3
def second_floor():
    print("Você está no segundo andar da casa: mais um corredor do qual você não vê o final.")
    sleep(3)
    print("Não é possível ver muito bem, mas há uma porta semiaberta para o que parece ser um quarto.")
    sleep(3)
    print('--------------------------------------------')
    print("w: entrar no quarto")
    print("c: explorar mais o corredor")
    print("r: dar meia volta e descer as escadas")
    print('--------------------------------------------')

#q4
def bedroom():
    print("Você abre a porta e está em um quarto.")
    sleep(3)
    print("Parece um quarto normal: uma cama, uma TV, espelho e uma mesa.")
    sleep(3)
    print("Há uma garrafa de vidro em cima da mesa contendo um líquido preto.")
    sleep(3)
    print('--------------------------------------------')
    print("g: tomar o líquido preto da garrafa")
    print("t: ligar a TV")
    print("r: sair do quarto")
    print('--------------------------------------------')

#q5
def bottle():
    print("Por algum motivo, você resolveu tomar uma garrafa de um líquido desconhecido em uma cada desconhecida.")
    sleep(4)
    print("Sua visão fica turva e você começa a ficar muito tonto")
    sleep(3)
    print("Você tenta se apoiar na mesa, mas não é o suficiente.")
    sleep(3)
    print("Caido no chão, você vê uma sombra lentamente entrando pela porta do quarto e se aproximando.")
    sleep(5)
    print("GAME OVER")

#q6
def television():
    print("Você aperta o botão de ligar a TV; uma TV de tubo da década de 90.")
    sleep(3)
    print("Ao acender, a TV revela imagens de uma série de câmeras espalhadas pela casa.")
    sleep(3)
    print("A câmera do que parece ser um porão é a única com movimento.")
    sleep(3)
    print("Como a luz é fraca, não fica claro quem ou o que está lá. Talvez seja alguém que possa te ajudar.")
    sleep(4)
    print("Pelas outras câmeras, é possível ver que há uma saída da casa: pelo corredor do hall de entrada, há uma porta para um quarto onde há uma janela.")
    sleep(5)
    print('--------------------------------------------')
    print("r: desligar a TV")
    print("t: olhar novamente para as câmeras")
    print('--------------------------------------------')

#q7
def second_floor_hall():
    print("Você segue andando pelo corredor, e é possível ver algo:")
    sleep(3)
    print("Há uma mesinha com um abajour que está com mal contato; a luz é fraca e está piscando.")
    sleep(3)
    print("É possível ver que, embaixo do abajour, há um pedaço de papel.")
    sleep(3)
    print("Há mais uma porta no corredor, de onde parece vir um pouco de luz.")
    sleep(3)
    print('--------------------------------------------')
    print("p: abrir a porta e entrar no quarto")
    print("n: pegar o pedaço de papel")
    print('--------------------------------------------')

#q8
def paper_note():
    print("Você levanta o abajour e pega o pedaço de papel: é um bilhete")
    sleep(3)
    print("É dificl entender o que está escrito, provavelmente quem escreveu fez isso com muita pressa.")
    sleep(4)
    print("Após algum tempo, você consegue ler a frase: NÃO ENTRE NO PORÃO")
    sleep(3)
    print('--------------------------------------------')
    print("r: largar o bilhete")
    print('--------------------------------------------')

#q9
def door_second_floor():
    print("Você abre a porta, entra no quarto e uma luz quase cega seus olhos: é uma janela para o exterior. Talvez dê para sair por ali.")
    sleep(5)
    print("Você se aproxima da janela e consegue abrir o vidro. Do lado de fora, há um jardim aparentemente abandonado.")
    sleep(4)
    print("No jardim, há uma árvore onde você poderia se agarrar ao pular para fugir; e ao lado da janela, há uma calha que passa por ali e vai até o chão.")
    sleep(5)
    print("Enquanto você observa as possibilidades, é possível ouvir passos no corredor, cada vez mais próximos. É preciso pensar rápido.")
    sleep(5)
    print('--------------------------------------------')
    print("h: se agarrar na calha para descer")
    print("s: pular em direção à árvore e tentar se descer por ela")
    print('--------------------------------------------')

#q10
def window_jump():
    print("Você pula da janela e tenta se agarrar em um galho da árvore, mas ele quebra no mesmo instante.")
    sleep(4)
    print("Você caiu de costas no chão e ficou incapaz de se mover")
    sleep(3)
    print("Antes de desmaiar, você vê um vulto entrando no jardim e se aproximando de você.")
    sleep(5)
    print("GAME OVER")

#q11
def first_floor_hall():
    print("Você decide seguir pelo corredor.")
    sleep(3)
    print("É possível ver um alçapão, que deve levar ao porão da casa.")
    sleep(3)
    print("No final do corredor, há uma porta fechada.")
    sleep(3)
    print("É possível ouvir, ao fundo, o som de passos que parecem vir de trás da porta.")
    sleep(4)
    print('--------------------------------------------')
    print("a: abrir o alçapão e descer")
    print("p: seguir no corredor e abrir a porta")
    print("r: voltar para o hall de entrada")
    print('--------------------------------------------')

#q12
def trapdoor():
    print("Você desceu pela passagem do alçapão.")
    sleep(3)
    print("A sua frente existe apenas um coredor para seguir em frente")
    sleep(3)
    print("Ao final do corredor, há uma porta fechada.")
    sleep(3)
    print("Esse porta, por sua vez, parece diferente das demais portas")
    sleep(3)
    print('--------------------------------------------')
    print("c: continuar embaixo, seguindo pelo corredor")
    print("r: subir e voltar pelo alçapão para o primeiro andar")
    print('--------------------------------------------')

#q13
def loft_hall():
    print("Você optou por seguir em frente, e agora chegou até a porta")
    sleep(3)
    print("Essa porta apresenta ranhuras, marcas de sangue e uma fechadura enferrujada.")
    sleep(3)
    print("Um barulho vindo do alçapão é ouvido")
    sleep(3)
    print('--------------------------------------------')
    print("p: abrir a porta misteriosa")
    print("r: retornar pelo corredor para o alçapão")
    print('--------------------------------------------')

#q14
def door_prision():
    print("Você passa pela porta")
    sleep(3)
    print("Você se depara com um cativeiro, com correntes, ossos, moscas e sangue espalhado.")
    sleep(3)
    print("Alguém entra na sala nesse instante e o apunhá-la pelas costas, deixando-o desacordado")
    sleep(3)
    print("Você acorda e percebe que está acorrentado. Começa a ouvir uma espécie de animal correndo na sua direção")
    sleep(5)
    print("GAME OVER")

#q15
def door_first_floor():
    print("Você abre a porta.")
    sleep(3)
    print("Você se depara com uma luz muito intensa vindo da janela")
    sleep(3)
    print("Parece ser uma saída da casa")
    sleep(3)
    print('--------------------------------------------')
    print("l: andar até a janela")
    print('--------------------------------------------')

#q16
def window_first_floor():
    print("Chegando perto da janela, você olha para fora e percebe que consegue chegar ao jardim")
    sleep(4)
    print("Basta pular a janela que você chega ao jardim e consegue escapar da casa")
    sleep(3)
    print('--------------------------------------------')
    print("j: pular pela janela")
    print('--------------------------------------------')

#q17
def garden_of_freedom():
    print("Você conseguiu escapar da casa!")
    sleep(3)
    print("Sinta o cheiro da liberdade, o Sol, a vida!")
    sleep(3)
    print("PARABÉNS!!")