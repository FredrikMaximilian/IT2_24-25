import pygame
import sys

# Configuration
CELL_SIZE = 10       # Size of each grid cell
GRID_WIDTH = 80      # Number of cells horizontally
GRID_HEIGHT = 60     # Number of cells vertically
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 60             # Frames per second for rendering

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ANT_COLOR = (255, 0, 0)

# Directions: 0=up, 1=right, 2=down, 3=left
DIRECTIONS = [
    (0, -1),  # up
    (1, 0),   # right
    (0, 1),   # down
    (-1, 0),  # left
]

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # 0 = white, 1 = black
        self.cells = [[0 for _ in range(height)] for _ in range(width)]

    def flip(self, x, y):
        self.cells[x][y] ^= 1

    def get(self, x, y):
        return self.cells[x][y]

class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = 0  # start facing up

    def step(self, grid: Grid):
        # Determine turn based on cell color
        cell = grid.get(self.x, self.y)
        if cell == 0:
            # white: turn right
            self.dir = (self.dir + 1) % 4
        else:
            # black: turn left
            self.dir = (self.dir - 1) % 4
        # Flip the cell
        grid.flip(self.x, self.y)
        # Move forward
        dx, dy = DIRECTIONS[self.dir]
        self.x = (self.x + dx) % grid.width
        self.y = (self.y + dy) % grid.height

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Langtons Maur')
        self.clock = pygame.time.Clock()
        self.grid = Grid(GRID_WIDTH, GRID_HEIGHT)
        # Start ant in center
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.ant = Ant(start_x, start_y)
        self.running = True
        self.paused = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r:
                    # Reset grid and ant
                    self.grid = Grid(GRID_WIDTH, GRID_HEIGHT)
                    self.ant = Ant(GRID_WIDTH // 2, GRID_HEIGHT // 2)

    def update(self):
        if not self.paused:
            # One step per frame; you can control speed by FPS
            self.ant.step(self.grid)

    def draw(self):
        # Draw cells
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                color = BLACK if self.grid.get(x, y) else WHITE
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, color, rect)
        # Draw ant
        ant_rect = pygame.Rect(
            self.ant.x * CELL_SIZE,
            self.ant.y * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
        pygame.draw.rect(self.screen, ANT_COLOR, ant_rect)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()
