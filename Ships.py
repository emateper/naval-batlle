import pygame

class Ships:
    def __init__(self, size=1):
        super().__init__()
        self.size = size
        self.image = pygame.Surface((80, 50), pygame.SRCALPHA)
        self.draw_ship()

    def draw_ship(self):
        self.image.fill((0, 0, 0, 0))  # Limpiar la superficie
        # Cuerpo del barco
        pygame.draw.rect(self.image, (255, 0, 0), (10, 20, 60 + (self.size - 1) * 20, 30))  # Cuerpo principal
        pygame.draw.rect(self.image, (0, 0, 0), (10, 40, 60 + (self.size - 1) * 20, 5))  # Base del barco
        pygame.draw.rect(self.image, (0, 0, 0), (20, 15, 40 + (self.size - 1) * 20, 10))  # Cubierta superior

        # Chimenea
        pygame.draw.rect(self.image, (150, 150, 150), (30, 5, 10, 15))  # Chimenea
        pygame.draw.circle(self.image, (200, 200, 200), (35, 0), 5)  # Humo

        # Ventanas
        pygame.draw.rect(self.image, (255, 255, 255), (15, 25, 10, 5))  # Ventana delantera
        pygame.draw.rect(self.image, (255, 255, 255), (55, 25, 10, 5))  # Ventana trasera
        pygame.draw.rect(self.image, (255, 255, 255), (35, 25, 10, 5))  # Ventana central

        self.rect = self.image.get_rect()

    def draw(self, surface, pos):
        self.rect.topleft = pos
        surface.blit(self.image, self.rect)


    def attack(self):
       pass
