import pygame
import random
import time
import os



pygame.init()  # função para iniciar o pygame


def clean():
    os.system('cls')
clean()


nome = input('Digite seu nome: ')
email = input('Digite seu E-mail: ')
arquivo = open('E-mail_e_Senha.txt', 'a')
arquivo.write(f'Nome: "{nome}".  E-mail: {email}!'+'\n')
clean()


pygame.init()  # função para iniciar o pygame
espirroSound = pygame.mixer.Sound("jogo_Educativo/espirro.mp3")
champion = pygame.mixer.Sound("jogo_Educativo/vitoria.mp3")
icone = pygame.image.load("jogo_Educativo/icon.ico")
pygame.display.set_caption("Anti_covid_Game")
pygame.display.set_icon(icone)
largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()
fundo = pygame.image.load("jogo_Educativo/fundo_lua.jpg")
nariz = pygame.image.load("jogo_Educativo/nariz.png")
corona = pygame.image.load("jogo_Educativo/coronavirus.png")
mascara = pygame.image.load("jogo_Educativo/mascara.png")
# [ini] cores em RGB (https://www.rapidtables.com/web/color/RGB_Color.html)
preto = (0, 0, 0)
branco = (255, 255, 255)





#defs:
def vitoria():
    pygame.mixer.Sound.play(champion)
    pygame.mixer.music.stop()
    message_display("Parabés você venceu o covid!")



def text_objects(texto, fonte):
    textSurface = fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()
def message_display(text):
    fonte = pygame.font.Font("freesansbold.ttf",50)
    TextSurf, TextRect = text_objects(text, fonte)
    TextRect.center = ((largura/2), (altura/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    jogo()
def dead(desvios):
    pygame.mixer.Sound.play(espirroSound)
    pygame.mixer.music.stop()
    message_display("Você contraiu covid =/")

def escrevendoPlacar(desvios):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Desvios:"+str(desvios), True, branco)
    display.blit(texto, (0, 0))
    
def jogo():
    pygame.mixer.music.load('jogo_Educativo/covidTrap.mp3')
    pygame.mixer.music.play(-1) # -1 é loopig infinito
    narizPosicaoX = largura * 0.45
    narizPosicaoY = altura * 0.8
    narizLargura = 100
    movimentoX = 0
    coronaPosicaoX = largura * 0.45
    coronaPosicaoY = -220
    coronaLargura = 30
    coronaAltura = 30
    coronaVelocidade = 9
    mascaraPosicaoX = largura * 0.80
    mascaraPosicaoY = -100
    mascaraLargura = 60
    mascaraAltura = 60
    mascaraVelocidade = 3

    desvios = 0
# iniciando o game:
    while True:
        # [ini] bloco de comando para verificar interação do usuário:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()  # break para executar o fim do código
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -10
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 10
            if evento.type == pygame.KEYUP:
                movimentoX = 0

        # [fim] bloco de comando para verificar interação do usuário:
        display.fill(branco)  # função para mudar a cor de fundo da tela
        display.blit(fundo, (0, 0))  # inserir imagem da tela
        narizPosicaoX = narizPosicaoX + movimentoX
        if narizPosicaoX < 0:
            narizPosicaoX = 0
        elif narizPosicaoX > 680:
            narizPosicaoX = 680
        # inserir imagem da tela
        display.blit(nariz, (narizPosicaoX, narizPosicaoY))
        display.blit(corona, (coronaPosicaoX, coronaPosicaoY))
        display.blit(mascara, (mascaraPosicaoX, mascaraPosicaoY))
        coronaPosicaoY = coronaPosicaoY + coronaVelocidade
        mascaraPosicaoY = mascaraPosicaoY + mascaraVelocidade
        # [ini] quando ele ultrapassa a barreira (fundo), começa em um lugar novo
        if coronaPosicaoY > altura:
            coronaPosicaoY = -220
            coronaVelocidade += 2
            coronaPosicaoX = random.randrange(0, largura-50)
            desvios = desvios + 1

        if mascaraPosicaoY > altura:
            mascaraPosicaoY = -220
            mascaraVelocidade += 1
            mascaraPosicaoX = random.randrange(0, largura-50)

            
        # [fim] quando ele ultrapassa a barreira (fundo), começa em um lugar novo
        escrevendoPlacar(desvios)
        # [ini]análise de colisão:
        if narizPosicaoY < coronaPosicaoY + coronaAltura:
            if narizPosicaoX < coronaPosicaoX and narizPosicaoX+narizLargura > coronaPosicaoX or coronaPosicaoX+coronaLargura > narizPosicaoX and coronaPosicaoX+coronaLargura < narizPosicaoX+narizLargura:
                dead(desvios)

        if narizPosicaoY < mascaraPosicaoY + mascaraAltura:
            if narizPosicaoX < mascaraPosicaoX and narizPosicaoX+narizLargura > mascaraPosicaoX or mascaraPosicaoX+mascaraLargura > narizPosicaoX and mascaraPosicaoX+mascaraLargura < narizPosicaoX+narizLargura:
                vitoria()
                pygame.quit()


        # [fim]análise de colisão:
        pygame.display.update()
        fps.tick(60)
jogo()
#fim do game