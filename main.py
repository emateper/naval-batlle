import pygame
import sys
from Dado import Dado


pygame.init()


width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Black Industries Naval Battle")


black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
cell_size = width // 10

#Clase barcos

class ships:
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30), pygame.SRCALPHA)  
        pygame.draw.polygon(self.image, (255, 0, 0), [(0, 30), (25, 0), (50, 30)])  
        self.rect = self.image.get_rect()
    
    def draw(self, surface, pos):
        self.rect.topleft = pos
        surface.blit(self.image, self.rect)
    
    def attack(self):
        pass
    
ship = ships()    
ship_position = None    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:  #esto esta bien, pero vamos a tener que sacarlo de aca despues.
            mouse_x, mouse_y = event.pos
            col = mouse_x // cell_size
            row = mouse_y // cell_size
            
            
            ship_position = (col * cell_size + (cell_size - ship.rect.width) // 2,
                             row * cell_size + (cell_size - ship.rect.height) // 2)    

   
        for col in range(10): ##hice una clase aparte para el tablero, creo que va a ser mejor pensarlo asi porque hay que manejar  tableros diferentes, o al menos dos con diferentes visibilidades para cada jugador. Cuando tenga un ratito saco el tablero de aca y lo armo en su archivo.
            for row in range(10):
             
                color = blue
            
            
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
    
    # Dibujar bordes negros, se libre en cambiar los colores
    for row in range(20):
        pygame.draw.line(screen, white, (0, row * cell_size), (width, row * cell_size), 1)
    for col in range(20):
        pygame.draw.line(screen, white, (col * cell_size, 0), (col * cell_size, height), 1)

    if ship_position:
        ship.draw(screen, ship_position)
    
    
    pygame.display.flip()

pygame.quit()