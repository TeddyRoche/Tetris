import pygame
import random

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)

# Define shapes
SHAPES = [
    # T Shape
    [[0, 1, 1, 1],
     [0, 0, 1, 0]],
    # Stair Shape
    [[0, 0, 2, 2],
     [0, 2, 2, 0]],
    # Stair Shape 2
    [[0, 3, 3, 0],
     [0, 0, 3, 3]],
    # L Shape Left
    [[0, 4, 0, 0],
     [0, 4, 4, 4]],
    [[0, 0, 5, 0],
     [0, 5, 5, 5]],
    # Square
    [[6, 6],
     [6, 6]],
    # L Shape Right
    [[0, 0, 0, 7],
     [0, 7, 7, 7]],
    # Line Shape
    [[8, 8, 8, 8]]
]


# Define shape class
class Shape:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.choice([RED, BLUE, GREEN, YELLOW, ORANGE, CYAN])
        self.x = (WINDOW_WIDTH // 2) // block_size - len(self.shape[0]) // 2
        self.y = 1

    def draw(self, screen, block_size):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.shape[i][j] != 0:
                    pygame.draw.rect(screen, self.color, (self.x * block_size + j * block_size, self.y * block_size + i * block_size, block_size, block_size))
                    pygame.draw.rect(screen, 'white', (self.x * block_size + j * block_size, self.y * block_size + i * block_size, block_size, block_size), 1)

    def move_down(self):
        self.y += 1

    def move_up(self):
        self.y -= 1

    def collides_with(self, other):
        shape_width = len(self.shape[0])
        shape_height = len(self.shape)
        for i in range(shape_height):
            for j in range(shape_width):
                if self.shape[i][j] != 0:
                    x_cor = self.x - other.x + j
                    y_cor = self.y - other.y + i
                    if (0 <= y_cor < len(other.shape)
                            and 0 <= x_cor < len(other.shape[0])
                            and other.shape[y_cor][x_cor] != 0):
                        return True
        return False


# Initialize Pygame
pygame.init()

# Set up window
WINDOW_WIDTH = 220
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tetris')

# Set up clock
clock = pygame.time.Clock()

# Set up game variables
block_size = 20
shapes = []
current_shape = Shape(random.choice(SHAPES))

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and current_shape.x + len(current_shape.shape[0]) > 4:
        current_shape.x -= 1
    if keys[pygame.K_RIGHT] and current_shape.x + len(current_shape.shape[0]) < 10:
        current_shape.x += 1

    # Move current shape down
    current_shape.move_down()

    for shape in shapes:
        if current_shape.collides_with(shape):
            current_shape.move_up()
            if current_shape.y <= 0:
                pygame.quit()
                quit()
            else:
                shapes.append(current_shape)
                current_shape = Shape(random.choice(SHAPES))
            break

    # Check if current shape has collided with another shape or reached the bottom
    if current_shape.y + len(current_shape.shape) >= 24:
        shapes.append(current_shape)
        current_shape = Shape(random.choice(SHAPES))

    # Draw current shape and all other shapes on screen
    screen.fill('dark gray')

    for x in range(1, 10):
        for y in range(1, 24):
            # First creates square with gray color. Second draws black border for square
            pygame.draw.rect(screen, 'light gray', (10 * x * 2, 10 * y * 2, 20, 20), 0)
            pygame.draw.rect(screen, 'black', (10 * x * 2, 10 * y * 2, 20, 20), 1)

    for shape in shapes:
        shape.draw(screen, block_size)

    current_shape.draw(screen, block_size)
    pygame.display.update()

    # Tick clock
    clock.tick(10)
