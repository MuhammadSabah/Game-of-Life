import pygame
import numpy

cells_grid = numpy.zeros((10, 10))
rows, cols = cells_grid.shape


# def draw(self, screen, box_size, color):
#     rect = pygame.Rect(x * box_size, y * box_size, box_size - 1, box_size - 1)
#     pygame.draw.rect(screen, color, rect, border_radius=2)
def next_generation(sum_alive_neighbors):
    updated_grid_cells = numpy.empty((rows, cols))


def count_alive_neighbors(row, col):
    sum_alive_neighbors = numpy.sum(cells_grid[row - 1:row + 2, col - 1: col + 2]) - cells_grid[row][col]
    return sum_alive_neighbors


def main():
    cells_grid[8, 9] = 1
    cells_grid[8, 8] = 1

    for r, c in numpy.ndindex(cells_grid.shape):
        sum_neighbors = count_alive_neighbors(r, c)
        next_generation(sum_neighbors)

    print(cells_grid)


main()
