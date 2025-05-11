import pygame
import sys
import random
import time

# Configuration
CELL_SIZE = 32
MAZE = [
    "###############",
    "#.............#",
    "#.###.###.###.#",
    "#o#.....#.....#o",
    "#.###.#.#.###.#",
    "#.....#.#.....#",
    "###.#.#.#.#.###",
    "#.....#.#.....#",
    "#.###.###.###.#",
    "#.............#",
    "###############"
]
ROWS = len(MAZE)
COLS = len(MAZE[0])
SCREEN_WIDTH = COLS * CELL_SIZE
SCREEN_HEIGHT = ROWS * CELL_SIZE + 40  # extra for score
FPS = 10
POWER_TIME = 10  # seconds power pellet lasts

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

GHOST_COLORS = [RED, PINK, CYAN, ORANGE]

# Directions
DIRS = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0)
}
OPPOSITE = {'UP':'DOWN','DOWN':'UP','LEFT':'RIGHT','RIGHT':'LEFT'}

class Maze:
    def __init__(self):
        self.grid = [list(row) for row in MAZE]
        self.pellets = set()
        self.power_pellets = set()
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == '.': self.pellets.add((x, y))
                elif cell == 'o': self.power_pellets.add((x, y))

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                px, py = x*CELL_SIZE, y*CELL_SIZE
                if cell == '#':
                    pygame.draw.rect(screen, BLUE, (px, py, CELL_SIZE, CELL_SIZE))
                if (x, y) in self.pellets:
                    r = CELL_SIZE // 8
                    pygame.draw.circle(screen, WHITE, (px+CELL_SIZE//2, py+CELL_SIZE//2), r)
                if (x, y) in self.power_pellets:
                    r = CELL_SIZE // 4
                    pygame.draw.circle(screen, WHITE, (px+CELL_SIZE//2, py+CELL_SIZE//2), r)

    def is_wall(self, x, y):
        return self.grid[y][x] == '#'

class Player:
    def __init__(self, maze):
        self.maze = maze
        self.start = (1, 1)
        self.x, self.y = self.start
        self.dir = 'LEFT'
        self.next_dir = None
        self.power = False
        self.power_time = 0

    def update(self):
        if self.next_dir:
            dx, dy = DIRS[self.next_dir]
            nx, ny = self.x+dx, self.y+dy
            if not self.maze.is_wall(nx, ny):
                self.dir = self.next_dir
        dx, dy = DIRS[self.dir]
        nx, ny = self.x+dx, self.y+dy
        if not self.maze.is_wall(nx, ny):
            self.x, self.y = nx, ny
        score = 0
        if (self.x, self.y) in self.maze.pellets:
            self.maze.pellets.remove((self.x, self.y))
            score += 10
        if (self.x, self.y) in self.maze.power_pellets:
            self.maze.power_pellets.remove((self.x, self.y))
            self.power = True
            self.power_time = time.time()
            score += 50
        return score

    def draw(self, screen):
        px, py = self.x*CELL_SIZE, self.y*CELL_SIZE
        pygame.draw.rect(screen, YELLOW, (px, py, CELL_SIZE, CELL_SIZE))

    def is_powered(self):
        if self.power and time.time() - self.power_time > POWER_TIME:
            self.power = False
        return self.power

class Ghost:
    def __init__(self, maze, pos, color):
        self.maze = maze
        self.x, self.y = pos
        self.dir = random.choice(list(DIRS.keys()))
        self.color = color

    def update(self, player):
        choices = []
        for d, (dx, dy) in DIRS.items():
            if d == OPPOSITE[self.dir]:
                continue
            nx, ny = self.x+dx, self.y+dy
            if not self.maze.is_wall(nx, ny): choices.append(d)
        if choices:
            self.dir = random.choice(choices)
        dx, dy = DIRS[self.dir]
        self.x += dx
        self.y += dy

    def draw(self, screen, frightened=False):
        px, py = self.x*CELL_SIZE, self.y*CELL_SIZE
        color = BLUE if frightened else self.color
        pygame.draw.rect(screen, color, (px, py, CELL_SIZE, CELL_SIZE))

    def pos(self):
        return (self.x, self.y)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pac-Man')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)
        self.reset()

    def reset(self):
        self.maze = Maze()
        self.player = Player(self.maze)
        self.ghosts = [Ghost(self.maze, (13,1), GHOST_COLORS[i%len(GHOST_COLORS)]) for i in range(4)]
        self.score = 0
        self.lives = 3
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_over:
                    self.reset()
                if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                    key_map = {pygame.K_UP:'UP', pygame.K_DOWN:'DOWN', pygame.K_LEFT:'LEFT', pygame.K_RIGHT:'RIGHT'}
                    self.player.next_dir = key_map[event.key]

    def update(self):
        if self.game_over:
            return
        self.score += self.player.update()
        powered = self.player.is_powered()
        for ghost in self.ghosts:
            ghost.update(self.player)
            if (ghost.x, ghost.y) == (self.player.x, self.player.y):
                if powered:
                    ghost.x, ghost.y = 13,1
                    self.score += 200
                else:
                    self.lives -= 1
                    if self.lives <= 0:
                        self.game_over = True
                    else:
                        self.player.x, self.player.y = self.player.start
                        self.player.power = False
                        time.sleep(1)
        if not self.maze.pellets and not self.maze.power_pellets:
            self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)
        self.maze.draw(self.screen)
        self.player.draw(self.screen)
        for ghost in self.ghosts:
            ghost.draw(self.screen, self.player.is_powered())
        score_surf = self.font.render(f'Score: {self.score}', True, WHITE)
        lives_surf = self.font.render(f'Lives: {self.lives}', True, WHITE)
        self.screen.blit(score_surf, (10, SCREEN_HEIGHT-30))
        self.screen.blit(lives_surf, (200, SCREEN_HEIGHT-30))
        if self.game_over:
            msg = 'You Win! Press R' if not self.maze.pellets and not self.maze.power_pellets else 'Game Over! Press R'
            msg_surf = self.font.render(msg, True, WHITE)
            rect = msg_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(msg_surf, rect)
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


def main():
    Game().run()

if __name__ == '__main__':
    main()