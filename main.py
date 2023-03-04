import math
import time

import pygame
import numpy

# Setup
window_height = 630
window_width = 1080
cell_size = 18
cols = math.ceil(window_width / cell_size)
rows = math.ceil(window_height / cell_size)
cells_grid = numpy.zeros((cols, rows))
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Game of Life")

# Colors
BLACK = (0, 0, 0)
GRAY = (33, 37, 41)
WHITE = (255, 255, 255)
DARK_BLUE = (36, 73, 89)


# Functions
def draw(screen, row, col, color):
    rect = pygame.Rect(row * cell_size, col * cell_size, cell_size - 1, cell_size - 1)
    pygame.draw.rect(screen, color, rect, border_radius=2)


def next_generation(sum_alive_neighbors, row, col, updated_cells):
    cell = cells_grid[row, col]
    cell_color = WHITE if cell == 1 else GRAY
    if cell == 1:
        if sum_alive_neighbors == 3 or sum_alive_neighbors == 2:
            updated_cells[row, col] = 1
            # cell_color = WHITE
        elif sum_alive_neighbors > 3 or sum_alive_neighbors < 2:
            cell_color = GRAY
    else:
        if sum_alive_neighbors == 3:
            updated_cells[row, col] = 1
            # cell_color = WHITE
        # else:
        #     cell_color = GRAY

    draw(screen, row, col, cell_color)
    return updated_cells


def count_alive_neighbors(row, col, cells):
    print(row, col)
    sum_alive_neighbors = numpy.sum(cells[row - 1:row + 2, col - 1: col + 2]) - cells[row][col]
    return sum_alive_neighbors


def update(cells):
    updated_grid_cells = numpy.zeros((cols, rows))
    for r, c in numpy.ndindex(cells.shape):
        sum_neighbors = count_alive_neighbors(r, c, cells)
        updated_grid_cells = next_generation(sum_neighbors, r, c, updated_grid_cells)

    return updated_grid_cells


def start(cells_grid):
    pygame.init()
    update(cells_grid)
    pygame.display.update()
    pygame.display.flip()

    start = False
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                if event.buttons[0]:
                    a = x // cell_size
                    b = y // cell_size
                    if cells_grid[a, b] == 0:
                        cells_grid[a, b] = 1
                        update(cells_grid)
                        pygame.display.update()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = not start
                    update(cells_grid)
                    pygame.display.update()

        screen.fill(BLACK)
        if start:
            cells_grid = update(cells_grid)
            pygame.display.update()

        time.sleep(0.0001)


if __name__ == "__main__":
    start(cells_grid)
    pygame.quit()
