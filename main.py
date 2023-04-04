import pygame
import numpy as np

# Inicializa o pygame
pygame.init()

# Distância focal
d = 300

# Ângulo de rotação
angulo = np.deg2rad(1)

# Cria a tela
screen = pygame.display.set_mode((800, 600))

# Criando o cubo
cubo = np.array([[-100, -100, -100, 1], [100, -100, -100, 1], [100, 100, -100, 1], [-100, 100, -100, 1], [-100, -100, 100, 1], [100, -100, 100, 1], [100, 100, 100, 1], [-100, 100, 100, 1]]).T

# Matrizes de rotação
rotacao_x = np.array([[1, 0, 0, 0], [0, np.cos(angulo), -np.sin(angulo), 0], [0, np.sin(angulo), np.cos(angulo), 0], [0, 0, 0, 1]])
rotacao_y = np.array([[np.cos(angulo), 0, np.sin(angulo), 0], [0, 1, 0, 0], [-np.sin(angulo), 0, np.cos(angulo), 0], [0, 0, 0, 1]])
rotacao_z = np.array([[np.cos(angulo), -np.sin(angulo), 0, 0], [np.sin(angulo), np.cos(angulo), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

rotacao_total = rotacao_x @ rotacao_y @ rotacao_z

# Matrizes de translação no Z
translacao_z1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
translacao_centro = np.array([[1, 0, 0, 400], [0, 1, 0, 300], [0, 0, 1, 0], [0, 0, 0, 1]])

# Pinhole
m_pinhole = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,-d],[0,0,-(1/d),0]])

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    pygame.time.delay(10)

    rotacao_total = rotacao_total @ rotacao_y @ rotacao_z @ rotacao_x

    M = translacao_centro @ m_pinhole @ translacao_z1 @ rotacao_total
    proj = M @ cubo

    screen.fill((0, 0, 0))

    # Criar linhas
    pygame.draw.line(screen, (255, 0, 0), (proj[0, 0]/proj[3, 0], proj[1, 0]/proj[3, 0]), (proj[0, 1]/proj[3, 1], proj[1, 1]/proj[3, 1]), 5)
    pygame.draw.line(screen, (255, 0, 0), (proj[0, 1]/proj[3, 1], proj[1, 1]/proj[3, 1]), (proj[0, 2]/proj[3, 2], proj[1, 2]/proj[3, 2]), 5)
    pygame.draw.line(screen, (255, 0, 0), (proj[0, 2]/proj[3, 2], proj[1, 2]/proj[3, 2]), (proj[0, 3]/proj[3, 3], proj[1, 3]/proj[3, 3]), 5)
    pygame.draw.line(screen, (255, 0, 0), (proj[0, 3]/proj[3, 3], proj[1, 3]/proj[3, 3]), (proj[0, 0]/proj[3, 0], proj[1, 0]/proj[3, 0]), 5)

    pygame.draw.line(screen, (255, 0, 0), (proj[0, 4]/proj[3, 4], proj[1, 4]/proj[3, 4]), (proj[0, 5]/proj[3, 5], proj[1, 5]/proj[3, 5]), 5)
    pygame.draw.line(screen, (255, 0, 0), (proj[0, 5]/proj[3, 5], proj[1, 5]/proj[3, 5]), (proj[0, 6]/proj[3, 6], proj[1, 6]/proj[3, 6]), 5)
    pygame.draw.line(screen, (255, 0, 0), (proj[0, 6]/proj[3, 6], proj[1, 6]/proj[3, 6]), (proj[0, 7]/proj[3, 7], proj[1, 7]/proj[3, 7]), 5)
    pygame.draw.line(screen, (255, 0, 0), (proj[0, 7]/proj[3, 7], proj[1, 7]/proj[3, 7]), (proj[0, 4]/proj[3, 4], proj[1, 4]/proj[3, 4]), 5)

    pygame.draw.line(screen, (255, 0, 0), (proj[0, 0]/proj[3, 0], proj[1, 0]/proj[3, 0]), (proj[0, 4]/proj[3, 4], proj[1, 4]/proj[3, 4]), 5)
    pygame.draw.line(screen, (255, 0, 0), (proj[0, 1]/proj[3, 1], proj[1, 1]/proj[3, 1]), (proj[0, 5]/proj[3, 5], proj[1, 5]/proj[3, 5]), 5)
    pygame.draw.line(screen, (255, 0, 0), (proj[0, 2]/proj[3, 2], proj[1, 2]/proj[3, 2]), (proj[0, 6]/proj[3, 6], proj[1, 6]/proj[3, 6]), 5)
    pygame.draw.line(screen, (255, 0, 0), (proj[0, 3]/proj[3, 3], proj[1, 3]/proj[3, 3]), (proj[0, 7]/proj[3, 7], proj[1, 7]/proj[3, 7]), 5)
    
    # Atualiza a tela
    pygame.display.flip()

    pygame.display.update()

pygame.quit()

