import pygame
import sys
from Ships import Ships
from Board import Board

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Black Industries Naval Battle")

black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
cell_size = width // 10

tablero = Board(width, height, cell_size)
ship = Ships()    
ship_position = None    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                ship.size = 2
                ship.draw_ship()  # Redibujar el barco con el nuevo tamaño
            elif event.key == pygame.K_3:
                ship.size = 3
                ship.draw_ship()
            elif event.key == pygame.K_4:
                ship.size = 4
                ship.draw_ship()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            col = mouse_x // cell_size
            row = mouse_y // cell_size
            
            # Asegúrate de que el barco quepa en el tablero
            if 0 <= col < 10 and 0 <= row < 10:
                # Asegurarte de que no se salga del tablero
                if col + ship.size <= 10:
                    ship_position = (
                        col * cell_size + (cell_size - ship.rect.width) // 2,
                        row * cell_size + (cell_size - ship.rect.height) // 2
                    )
            ship.draw_ship() 

    screen.fill(black)  # Limpia la pantalla
    tablero.dibujar(screen)  # Llama al método de dibujo del tablero
    
    # Dibuja el barco si tiene una posición válida
    if ship_position:
        ship.draw(screen, ship_position)
    
    pygame.display.flip()  # Actualiza la pantalla

pygame.quit()
