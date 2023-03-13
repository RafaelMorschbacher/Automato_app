def menu():
    print("MENU INICIAL")
    print("Pressione b para iniciar uma nova história")
    print("Pressione q para sair do jogo")

def quit_game():
    print("Você saiu do jogo")

def entry_hall():
    print("Você está no hall de entrada de uma casa sombria. Você não se lembra como chegou até aqui e a porta está trancada.")
    print("À sua esquerda, há uma escada para o segundo andar da casa.")
    print("À sua direita, há um corredor mal iluminado.")
    print("e: subir a escada")
    print("c: andar pelo corredor")

def second_floor():
    print("Você está no segundo andar da casa: mais um corredor do qual você não vê o final.")
    print("Não é possível ver muito bem, mas há uma porta semiaberta para o que parece ser um quarto.")
    print("w: entrar no quarto")
    print("c: explorar mais o corredor")
    print("r: dar meia volta e descer as escadas")

def bedroom():
    print("Você abre a porta e está em um quarto.")
    print("Parece um quarto normal: uma cama, uma TV, espelho e uma mesa.")
    print("Há uma garrafa de vidro em cima da mesa contendo um líquido preto")
    print("g: tomar o líquido preto da garrafa")
    print("t: ligar a TV")
    print("r: sair do quarto")

def bottle():
    print("Por algum motivo, você resolveu tomar uma garrafa de um líquido desconhecido em uma cada desconhecida.")
    print("Sua visão fica turva e você começa a ficar muito tonto")
    print("Você tenta se apoiar na mesa, mas não é o suficiente.")
    print("Caido no chão, você vê uma sombra lentamente entrando pela porta do quarto e se aproximando")
    print("GAME OVER")

def television():
    print("Você aperta o botão de ligar a TV; uma TV de tubo da década de 90.")
    print("Ao acender, a TV revela imagens de uma série de câmeras espalhadas pela casa.")
    print("A câmera do que parece ser um porão é a única com movimento.")
    print("Como a luz é fraca, não fica claro quem ou o que está lá. Talvez seja alguém que possa te ajudar")
    print("Pelas outras câmeras, é possível ver que há uma saída da casa: pelo corredor do hall de entrada, há uma porta para um quarto onde há uma janela.")
    print("r: desligar a TV")
    print("t: Olhar novamente para as câmeras")

def second_floor_hall():
    print("Você segue andando pelo corredor, e é possível ver algo:")
    print("Há uma mesinha com um abajour que está com mal contato; a luz é fraca e está piscando.")
    print("É possível ver que, embaixo do abajour, há um pedaço de papel.")
    print("Há mais uma porta no corredor, de onde parece vir um pouco de luz")
    print("p: abrir a porta e entrar no quarto")
    print("n: pegar o pedaço de papel")

def paper_note():
    print("Você levanta o abajour e pega o pedaço de papel: é um bilhete")
    print("É dificl entender o que está escrito, provavelmente quem escreveu fez isso com muita pressa.")
    print("Após algum tempo, você consegue ler a frase: NÃO ENTRE NO PORÃO")
    print("r: largar o bilhete")

def door_second_floor():
    print("Você abre a porta, entra no quarto e uma luz quase cega seus olhos: é uma janela para o exterior. Talvez dê para sair por ali.")
    print("Você se aproxima da janela e consegue abrir o vidro. Do lado de fora, há um jardim aparentemente abandonado.")
    print("No jardim, há uma árvore onde você poderia se agarrar ao pular para fugir; e ao lado da janela, há uma calha que passa por ali e vai até o chão.")
    print("Enquanto você observa as possibilidades, é possível ouvir passos no corredor, cada vez mais próximos. É preciso pensar rápido.")
    print("h: se agarrar na calha para descer")
    print("s: pular em direção à árvore e tentar se descer por ela")

def window_jump():
    print("Você pula da janela e tenta se agarrar em um galho da árvore, mas ele quebra no mesmo instante.")
    print("Você caiu de costas no chão e ficou incapaz de se mover")
    print("Antes de desmaiar, você vê um vulto entrando no jardim e se aproximando de você.")
    print("GAME OVER")

def first_floor_hall():
    print("Você decide seguir pelo corredor.")
    print("É possível ver um alçapão, que deve ir levar ao porão da casa.")
    print("No final do corredor, há uma porta fechada.")
    print("É possível ouvir, ao fundo, o som de passos, que parecem vir de trás da porta.")
    print("a: abrir o alçapão e descer")
    print("p: seguir no corredor e abrir a porta")
    print("r: voltar para o hall de entrada")