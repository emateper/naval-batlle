import pygame
from Ships import Ships

class Board:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.blue = (0, 0, 255)  
        self.white = (255, 255, 255)  

    def dibujar(self, screen, ship_position=None):
        for col in range(10):
            for row in range(10):
                color = self.blue  
                pygame.draw.rect(screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

        # Dibujar bordes negros
        for row in range(20):
            pygame.draw.line(screen, self.white, (0, row * self.cell_size), (self.width, row * self.cell_size), 1)
        for col in range(20):
            pygame.draw.line(screen, self.white, (col * self.cell_size, 0), (col * self.cell_size, self.height), 1)

        if ship_position:
            ship.draw(screen, ship_position)  
