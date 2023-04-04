import pygame
import numpy as np

# Inicializa o pygame
pygame.init()

# Distância focal
d = 700

# Cores
RED = (255, 0, 0)

# Ângulo de rotação
angulo = np.deg2rad(1)

# Cria a tela
screen = pygame.display.set_mode((800, 600))

# Criando o cubo
cubo = np.array([[-150, -150, -150, 1], [150, -150, -150, 1], [150, 150, -150, 1], [-150, 150, -150, 1], [-150, -150, 150, 1], [150, -150, 150, 1], [150, 150, 150, 1], [-150, 150, 150, 1]]).T

# Matrizes de rotação
rotacao_x = np.array([[1, 0, 0, 0], [0, np.cos(angulo), -np.sin(angulo), 0], [0, np.sin(angulo), np.cos(angulo), 0], [0, 0, 0, 1]])
rotacao_y = np.array([[np.cos(angulo), 0, np.sin(angulo), 0], [0, 1, 0, 0], [-np.sin(angulo), 0, np.cos(angulo), 0], [0, 0, 0, 1]])
rotacao_z = np.array([[np.cos(angulo), -np.sin(angulo), 0, 0], [np.sin(angulo), np.cos(angulo), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

rotacao_total = rotacao_x @ rotacao_y @ rotacao_z

# Matrizes de translação no Z
translacao_z = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
translacao_centro = np.array([[1, 0, 0, 400], [0, 1, 0, 300], [0, 0, 1, 0], [0, 0, 0, 1]])

# Pinhole
m_pinhole = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,-d],[0,0,-(1/d),0]])

# Loop principal
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Diminuindo a velocidade das transformações
    pygame.time.delay(20)

    # Atualizando a rotação
    rotacao_total = rotacao_total @ rotacao_y @ rotacao_z @ rotacao_x

    # Juntando todas as transformações em uma matriz só chamada M
    M = translacao_centro @ m_pinhole @ translacao_z @ rotacao_total

    # Multiplicando a matriz M pelo cubo, gerando um novo cubo com as transformações
    final = M @ cubo

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        d += 10
        translacao_z = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
        M = translacao_centro @ m_pinhole @ translacao_z @ rotacao_total
        final = M @ cubo

    if pygame.key.get_pressed()[pygame.K_UP]:
        d -= 10
        translacao_z = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
        M = translacao_centro @ m_pinhole @ translacao_z @ rotacao_total
        final = M @ cubo

    # Preencher a tela com preto para não deixar rastro
    screen.fill((0, 0, 0))

    # Criar linhas que ligam os pontos do cubo -> Ao fazer a divisão, transforma o XpWp em Xp e/ou YpWp em Yp
    pygame.draw.line(screen, RED, (final[0, 0]/final[3, 0], final[1, 0]/final[3, 0]), (final[0, 1]/final[3, 1], final[1, 1]/final[3, 1]), 3)
    pygame.draw.line(screen, RED, (final[0, 1]/final[3, 1], final[1, 1]/final[3, 1]), (final[0, 2]/final[3, 2], final[1, 2]/final[3, 2]), 3)
    pygame.draw.line(screen, RED, (final[0, 2]/final[3, 2], final[1, 2]/final[3, 2]), (final[0, 3]/final[3, 3], final[1, 3]/final[3, 3]), 3)
    pygame.draw.line(screen, RED, (final[0, 3]/final[3, 3], final[1, 3]/final[3, 3]), (final[0, 0]/final[3, 0], final[1, 0]/final[3, 0]), 3)
    pygame.draw.line(screen, RED, (final[0, 4]/final[3, 4], final[1, 4]/final[3, 4]), (final[0, 5]/final[3, 5], final[1, 5]/final[3, 5]), 3)
    pygame.draw.line(screen, RED, (final[0, 5]/final[3, 5], final[1, 5]/final[3, 5]), (final[0, 6]/final[3, 6], final[1, 6]/final[3, 6]), 3)

    pygame.draw.line(screen, RED, (final[0, 6]/final[3, 6], final[1, 6]/final[3, 6]), (final[0, 7]/final[3, 7], final[1, 7]/final[3, 7]), 3)
    pygame.draw.line(screen, RED, (final[0, 7]/final[3, 7], final[1, 7]/final[3, 7]), (final[0, 4]/final[3, 4], final[1, 4]/final[3, 4]), 3)
    pygame.draw.line(screen, RED, (final[0, 0]/final[3, 0], final[1, 0]/final[3, 0]), (final[0, 4]/final[3, 4], final[1, 4]/final[3, 4]), 3)
    pygame.draw.line(screen, RED, (final[0, 1]/final[3, 1], final[1, 1]/final[3, 1]), (final[0, 5]/final[3, 5], final[1, 5]/final[3, 5]), 3)
    pygame.draw.line(screen, RED, (final[0, 2]/final[3, 2], final[1, 2]/final[3, 2]), (final[0, 6]/final[3, 6], final[1, 6]/final[3, 6]), 3)
    pygame.draw.line(screen, RED, (final[0, 3]/final[3, 3], final[1, 3]/final[3, 3]), (final[0, 7]/final[3, 7], final[1, 7]/final[3, 7]), 3)
    
    # Atualiza a tela
    pygame.display.update()

pygame.quit()

