import pygame
import math

pygame.init()

# Defina as dimensões da janela
width = 500
height = 500

# Crie uma janela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cubo 3D')

# Defina as coordenadas dos vértices do cubo
vertices = [
    [-50, -50, -50],
    [50, -50, -50],
    [50, 50, -50],
    [-50, 50, -50],
    [-50, -50, 50],
    [50, -50, 50],
    [50, 50, 50],
    [-50, 50, 50]
]

# Defina as conexões entre os vértices para formar as arestas
edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]

# Defina a posição e a rotação do cubo
position = [width // 2, height // 2]
rotation = [0, 0, 0]

# Defina a velocidade de rotação do cubo
rotation_speed = 0.005
# Crie um loop principal
running = True
while running:

    # Desenhe um fundo preto
    screen.fill((0, 0, 0))

    # Calcule a matriz de rotação do cubo
    rotation_matrix = [
        [math.cos(rotation[1]) * math.cos(rotation[2]), math.cos(rotation[1]) * math.sin(rotation[2]), -math.sin(rotation[1]), 0],
        [math.sin(rotation[0]) * math.sin(rotation[1]) * math.cos(rotation[2]) - math.cos(rotation[0]) * math.sin(rotation[2]), math.sin(rotation[0]) * math.sin(rotation[1]) * math.sin(rotation[2]) + math.cos(rotation[0]) * math.cos(rotation[2]), math.sin(rotation[0]) * math.cos(rotation[1]), 0],
        [math.cos(rotation[0]) * math.sin(rotation[1]) * math.cos(rotation[2]) + math.sin(rotation[0]) * math.sin(rotation[2]), math.cos(rotation[0]) * math.sin(rotation[1]) * math.sin(rotation[2]) - math.sin(rotation[0]) * math.cos(rotation[2]), math.cos(rotation[0]) * math.cos(rotation[1]), 0],
        [0, 0, 0, 1]
    ]

    # Transforme cada vértice do cubo usando a matriz de rotação
    transformed_vertices = []
    for vertex in vertices:
        x = vertex[0] * rotation_matrix[0][0] + vertex[1] * rotation_matrix[1][0] + vertex[2] * rotation_matrix[2][0] + rotation_matrix[3][0]
        y = vertex[0] * rotation_matrix[0][1] + vertex[1] * rotation_matrix[1][1] + vertex[2] * rotation_matrix[2][1] + rotation_matrix[3][1]
       
        z = vertex[0] * rotation_matrix[0][2] + vertex[1] * rotation_matrix[1][2] + vertex[2] * rotation_matrix[2][2] + rotation_matrix[3][2]
        transformed_vertices.append([x, y, z])

    # Desenhe as arestas do cubo na tela
    for edge in edges:
        start = transformed_vertices[edge[0]]
        end = transformed_vertices[edge[1]]
        pygame.draw.line(screen, (255, 255, 255), (start[0] + position[0], start[1] + position[1]), (end[0] + position[0], end[1] + position[1]), 2)

    # Atualize a tela
    pygame.display.update()

    # Trate eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





    # Atualize a rotação do cubo
    rotation[0] += rotation_speed * math.pi / 360
    rotation[1] += rotation_speed * math.pi / 360
    rotation[2] += rotation_speed * math.pi / 360

# Encerre o Pygame
pygame.quit()
