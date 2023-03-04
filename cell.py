import pygame


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
        self.status = 0

    def draw(self, screen, cell_size, color):
        rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size - 1, cell_size - 1)
        pygame.draw.rect(screen, color, rect, border_radius=2)
