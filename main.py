import pygame
import random

pygame.init()

win_width = 600
win_height = 850
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Tetris")

square_size = 40

shapes = [
    # I shape
    [[1, 1, 1, 1]],
    # O shape
    [[0, 1, 1, 0],
     [0, 1, 1, 0]],
    # T shape
    [[0, 0, 1, 0],
     [0, 1, 1, 1]],
    # S shape
    [[0, 0, 1, 1],
     [0, 1, 1, 0]],
    # Z shape
    [[0, 1, 1, 0],
     [0, 0, 1, 1]],
    # J shape
    [[0, 1, 0, 0],
     [0, 1, 1, 1]],
    # L shape
    [[0, 0, 0, 1],
     [0, 1, 1, 1]],
]

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
red = (255, 0, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
purple = (128, 0, 128)
shape_colors = [cyan, yellow, purple, green, orange, blue, red]

shape_y = 0

frame_rate = 2
clock = pygame.time.Clock()
current_shape = random.choice(shapes)


def collision(x_cor, y_cor):
    pos_x = x_cor + 1
    pos_y = y_cor + 1
    if pos_x < 0 or pos_x >= 800 or pos_y >= 800:
        return True
    if pos_y >= 0 and (pos_x != 0 and pos_y != 0):
        return True
    return False


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill('dark gray')

    # Draws the squares by (x, y)
    for x in range(1, 10):
        for y in range(1, 20):
            # First creates square with gray color. Second draws black border for square
            pygame.draw.rect(window, 'light gray', (20 * x * 2, 20 * y * 2, square_size, square_size), 0)
            pygame.draw.rect(window, 'black', (20 * x * 2, 20 * y * 2, square_size, square_size), 1)

    # I shape
    shape = [[1, 1, 1, 1]]
    color = cyan
    shape_y += 40
    # Draw the shape on the screen
    for row in range(len(shapes[0])):
        for col in range(len(shapes[0][row])):
            if shapes[0][row][col] == 1:
                x = (col + 4) * square_size
                y = (row + 1) * square_size
                if collision(x, y):
                    pygame.draw.rect(window, color, (x, y + shape_y, square_size, square_size), 0)
                    pygame.draw.rect(window, black, (x, y + shape_y, square_size, square_size), 1)

    # Update the display
    pygame.display.update()

    clock.tick(frame_rate)

# Clean up
pygame.quit()
