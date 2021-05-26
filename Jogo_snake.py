#=================== Inicialização ===============
import pygame
import random
import os

pygame.init()

# Definindo medidas
tamanho = 10 
largura = 480
altura = 320

# Definindo cores
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
branco = (255, 255, 255)
preto = (0, 0, 0)
cinzaClaro=(220,220,220)

# Criando guia princípal e nome do jogo
fps = pygame.time.Clock()
janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Snake Retrô')

# Musicas e imagens 
musica_inicio =os.path.join('assets','musicas','musica_inicial.mp3')
musica_final=os.path.join('assets','musicas', 'musica_fim.mp3') 
pygame.mixer.music.load(musica_inicio)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
fundo_jogo = pygame.image.load('assets/Imagens/Fundo.jpeg').convert()
menu = pygame.image.load('assets/Imagens/Untitled.jpg').convert()

#maça aparecendo em lugar aleatorio 

class Cobra:
    def __init__(self):
        self.x = random.randint(0,(largura-tamanho)/10)*10
        self.y = random.randint(0,(altura-tamanho)/10)*10
        self.velocidade_em_x = 0
        self.velocidade_em_y = 0
        self.cobra_xy = []
        self.cobra_comprimento = 1
        self.cobra_inicial = []
        self.pontuacao = 0
        self.fimdejogo = False
    def movimentos_possiveis(self):
        self.cobra_0 = [self.x,self.y]
        self.cobra_xy.append(self.cobra_inicial) 
    def crescimento_cobra(self):
        self.cobra_comprimento += 1
    def imagem_cobra(self):
        for XY in self.cobra_xy:
            pygame.draw.rect(fundo_jogo,branco,[XY[0],XY[1],tamanho,tamanho])
    def resto(self):
        if len(self.cobra_xy) > self.cobra_comp:
            del self.cobra_xy[0]
    def morte(self):
        if any(Bloco == self.cobra_0 for Bloco in self.cobra_xy[:-1]):
            self.fimdejogo = True

    def reinicio(self):
            self.x = random.randint(0,(largura-tamanho)/10)*10
            self.y = random.randint(0,(altura-tamanho)/10)*10
            self.vel_x = 0
            self.vel_y = 0
            self.cobra_xy = []
            self.cobra_comp = 1
            self.cobra_0 = []
            self.pontos = 0
            self.fimdejogo = False 

#==== Define Maça ===== 
class Maca:
    def __init__(self):
        self.pos_x = random.randint(0,(largura-tamanho)/10)*10
        self.pos_y = random.randint(0,(altura-tamanho)/10)*10
        self.w = 18
        self.h = 18
        self.img = pygame.image.load('assets/Imagens/maca_Mine.png').convert()
        self.convercao = pygame.transform.scale(self.img, (self.w, self.h))
        

class textos:
    def __init__(self, msg, cor, tam):
            self.font = pygame.font.SysFont(None, tam)
            self.texto = self.font.render(msg, True, cor)

    def mostra(self, x, y):
            janela.blit(self.texto, [x, y])

# encerramento do jogo

jogo = False
fim_do_jogo = False
inicio_do_jogo = True

palavra = textos("Game Over", vermelho, 37)
palavra2 = textos("Pontuação: " , branco, 27)
palavra3 = textos("aperte Q", branco,27)
palavra4 = textos("Deseja continuar?", branco,27)
palavra5 = textos("Snake Retrô", branco,35)
palavra6 = textos("Escolha o nível de dificuldade do jogo:", vermelho,27)


maca = Maca()


#========Menu==============
while inicio_do_jogo:
    janela.blit(menu,(0,0)) 
    
    # escolha da dificuldade 
    pygame.draw.rect(janela, cinzaClaro, [23, 160, 139, 31])
    pygame.draw.rect(janela, preto, [25, 162, 135, 27])
    facil = textos("Fácil(1)", branco, 30)
    facil.mostra(60, 166)

    pygame.draw.rect(janela, cinzaClaro, [173, 160, 139, 31])
    pygame.draw.rect(janela, preto, [175, 162, 135, 27])
    medio = textos("Médio(2)", branco, 30)
    medio.mostra(199, 166)

    pygame.draw.rect(janela, cinzaClaro, [323, 160, 139, 31])
    pygame.draw.rect(janela, preto, [325, 162, 135, 27])
    dificil = textos("Díficil(3)", vermelho, 30)
    dificil.mostra(353, 166)

    #Escolha da dificuldade do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inicio_do_jogo=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                fps.tick(10)
                jogo = True
            elif event.key == pygame.K_2:
                fps.tick(20)
                jogo = True
            elif event.key == pygame.K_3:
                fps.tick(35)
                jogo = True       
    

    # loop principal
    contador = 0
    while jogo:
        janela.blit(fundo_jogo,(0,0)) 
        palavra2.mostra(340, 0)
        contador = str(contador)
        cont = textos(contador,branco,27)
        cont.mostra(445,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo = False
                inicio_do_jogo = False

        janela.blit(maca.convercao, (maca.pos_x,maca.pos_y))
        pygame.display.update()

        contador = int(contador) + 1
        if contador == 1000:
            contador = 100


    pygame.display.update()

pygame.quit()