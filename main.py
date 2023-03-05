import math
import time
import tkinter as tk
import pygame
import numpy

# Setup
window_height = 630
window_width = 1140
cell_size = 15
cols = math.ceil(window_width / cell_size)
rows = math.ceil(window_height / cell_size)
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Game of Life")

# Colors
BLACK = (0, 0, 0)
GRAY = (33, 37, 41)
WHITE = (255, 255, 255)
DARK_BLUE = (36, 73, 89)
WHITE_TINT = (170, 170, 170)


# Functions
def draw(screen, row, col, color):
    rect = pygame.Rect(row * cell_size, col * cell_size, cell_size - 1, cell_size - 1)
    pygame.draw.rect(screen, color, rect, border_radius=2)


def next_generation(cells_grid, sum_alive_neighbors, row, col, updated_cells, next):
    cell = cells_grid[row, col]
    cell_color = WHITE if cell == 1 else GRAY
    if cell == 1:
        if 2 <= sum_alive_neighbors <= 3:
            updated_cells[row, col] = 1
            if next:
                cell_color = WHITE
        else:
            if next:
                cell_color = WHITE_TINT
    else:
        if sum_alive_neighbors == 3:
            updated_cells[row, col] = 1
            if next:
                cell_color = WHITE

    draw(screen, row, col, cell_color)
    return updated_cells


def count_alive_neighbors(row, col, cells):
    sum_alive_neighbors = numpy.sum(cells[row - 1:row + 2, col - 1: col + 2]) - cells[row, col]
    return sum_alive_neighbors


def update(cells, next=False):
    updated_grid_cells = numpy.zeros((cols, rows))
    for r, c in numpy.ndindex(cells.shape):
        sum_neighbors = count_alive_neighbors(r, c, cells)
        updated_grid_cells = next_generation(cells, sum_neighbors, r, c, updated_grid_cells, next)

    return updated_grid_cells


def start():
    cells_grid = numpy.zeros((cols, rows))
    update(cells_grid)
    pygame.display.flip()
    pygame.display.update()

    start = False
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = not start
                    cells_grid = update(cells_grid, True)
                    pygame.display.update()

            if event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                if event.buttons[0]:
                    a = x // cell_size
                    b = y // cell_size
                    cells_grid[a, b] = 1
                    update(cells_grid)
                    pygame.display.update()

        screen.fill(BLACK)
        if start:
            cells_grid = update(cells_grid, True)
            pygame.display.update()

        time.sleep(0.0001)


if __name__ == "__main__":
    pygame.init()
    start()
    pygame.quit()
