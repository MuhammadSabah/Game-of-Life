import math
import pygame
import numpy
import cell

# Setup
pygame.init()
window_height = 630
window_width = 1080
cell_size = 18
cols = math.ceil(window_width / cell_size)
rows = math.ceil(window_height / cell_size)
# cells_grid = numpy.zeros((cols, rows))
cells_grid = []
# updated_grid_cells = numpy.zeros((cols, rows))
updated_grid_cells = []
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Game of Life")

for i in range(rows):
    sub_arr = []
    for j in range(cols):
        sub_arr.append(cell.Cell(i, j))
    cells_grid.append(sub_arr)

# Colors
BLACK = (0, 0, 0)
GRAY = (33, 37, 41)
WHITE = (255, 255, 255)
DARK_BLUE = (36, 73, 89)


# Functions


def next_generation(sum_alive_neighbors, row, col):
    cell = cells_grid[row][col]
    if cell == 1:
        if 2 == sum_alive_neighbors == 3:
            cell.status = 1
        elif sum_alive_neighbors > 3 or sum_alive_neighbors < 2:
            cell.status = 0
    else:
        if sum_alive_neighbors == 3:
            cell.status = 1
        else:
            cell.status = 0

    cell_color = WHITE if cell.status == 0 else GRAY


def count_alive_neighbors(row, col):
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue
            if 0 <= i < len(cells_grid) and 0 <= j < len(cells_grid[0]):
                if cells_grid[i][j] == 1:
                    count += 1
    return count


def update(cells):
    for r in range(rows):
        for c in range(cols):
            sum_neighbors = count_alive_neighbors(r, c)
            next_generation(sum_neighbors, r, c)


def main():
    cells_grid[8][9].status = 1
    cells_grid[8][8].status = 1
    cells_grid[8][7].status = 1
    cells_grid[7][8].status = 1
    cells_grid[7][9].status = 1
    cells_grid[7][7].status = 1
    cells_grid[6][8].status = 1
    cells_grid[6][7].status = 1
    cells_grid[6][9].status = 1

    update(cells_grid)

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
                    cells_grid[a][b].status = 1
                    # update(cells_grid)

        for x in range(rows):
            for y in range(cols):
                cell = cells_grid[x][y]
                if cell.status == 1:
                    cell.draw(screen, cell_size, WHITE)

                if cell.status == 0:
                    cell.draw(screen, cell_size, GRAY)

        screen.fill(BLACK)
        pygame.display.flip()
        # else:
        #     update(cells_grid)


main()
