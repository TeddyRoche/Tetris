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
    # top T shape
    [[0, 1, 1, 1],
     [0, 0, 1, 0]],
    # right stair shape
    [[0, 0, 2, 2],
     [0, 2, 2, 0]],
    # left stair shape
    [[0, 3, 3, 0],
     [0, 0, 3, 3]],
    # left L shape
    [[0, 4, 0, 0],
     [0, 4, 4, 4]],
    # bottom T shape
    [[0, 0, 5, 0],
     [0, 5, 5, 5]],
    # square shape
    [[0, 6, 6],
     [0, 6, 6]],
    # right L shape
    [[0, 0, 0, 7],
     [0, 7, 7, 7]]
]


# Define shape class
class Shape:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.choice([RED, BLUE, GREEN, YELLOW, ORANGE, CYAN])
        self.x = 4
        self.y = 1

    # Draws the shape on the board
    def draw(self, screen, block_size):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.shape[i][j] != 0:
                    pygame.draw.rect(screen, self.color, (self.x * block_size + j * block_size,
                                                          self.y * block_size + i * block_size, block_size, block_size))
                    pygame.draw.rect(screen, 'white', (self.x * block_size + j * block_size,
                                                       self.y * block_size + i * block_size, block_size, block_size), 1)

    # moves shape down 1
    def move_down(self):
        self.y += 1

    # moves shape up 1
    def move_up(self):
        self.y -= 1

    # Method for detecting Collision with other shapes
    def collides_with(self, other):
        shape_width = len(self.shape[0])
        shape_height = len(self.shape)
        for i in range(shape_height):
            for j in range(shape_width):
                if self.shape[i][j] == 1:
                    x_cor, y_cor = self.x + j, self.y + i
                    if y_cor >= len(other.shape) or x_cor < 0 or x_cor >= len(other.shape[0]) \
                            or (other.shape[y_cor][x_cor] == 1):
                        return True
        return False
    # def collides_with(self, other):
    #     shape_width = len(self.shape[0])
    #     shape_height = len(self.shape)
    #     for i in range(shape_height):
    #         for j in range(shape_width):
    #             if self.shape[i][j] != 0:
    #                 x_cor, y_cor = self.x + j, self.y + i
    #                 if y_cor >= len(other.shape) or x_cor < 0 or x_cor >= len(other.shape[0]) \
    #                         or (other.shape[y_cor][x_cor] != 0):
    #                     return True
    #     return False


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
# create empty shape array
shapes = []
# gets a random shape to start
current_shape = Shape(random.choice(SHAPES))

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Moves the shapes Left and Right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and current_shape.x > 0:
        current_shape.x -= 1
    if keys[pygame.K_RIGHT] and current_shape.x + len(current_shape.shape[0]) < 200 / block_size:
        current_shape.x += 1

    # Move current shape down
    current_shape.move_down()

    # This should be used to detect collision with other shapes
    for shape in shapes:
        if current_shape.collides_with(shape):
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

    # Create the Block board visual
    for x in range(1, 10):
        for y in range(1, 24):
            # First creates square with gray color. Second draws black border for square
            pygame.draw.rect(screen, 'light gray', (10 * x * 2, 10 * y * 2, 20, 20), 0)
            pygame.draw.rect(screen, 'black', (10 * x * 2, 10 * y * 2, 20, 20), 1)

    # Draws the previous shapes on the Board
    for shape in shapes:
        shape.draw(screen, block_size)

    current_shape.draw(screen, block_size)
    pygame.display.update()

    # Tick clock
    clock.tick(10)
