import pygame
import sys
import random

# Configuration
CELL_SIZE = 30
COLS = 10
ROWS = 20
WIDTH = CELL_SIZE * COLS
HEIGHT = CELL_SIZE * ROWS
FPS = 60
DROP_SPEED = 500  # milliseconds between automatic drops

# Colors
BLACK = (0, 0, 0)
GREY = (40, 40, 40)
WHITE = (255, 255, 255)
COLORS = {
    'I': (0, 240, 240),
    'J': (0, 0, 240),
    'L': (240, 160, 0),
    'O': (240, 240, 0),
    'S': (0, 240, 0),
    'T': (160, 0, 240),
    'Z': (240, 0, 0)
}

SHAPES = {
    'I': [
        [(0,1),(1,1),(2,1),(3,1)],
        [(2,0),(2,1),(2,2),(2,3)]
    ],
    'J': [
        [(0,0),(0,1),(1,1),(2,1)],
        [(1,0),(2,0),(1,1),(1,2)],
        [(0,1),(1,1),(2,1),(2,2)],
        [(1,0),(1,1),(0,2),(1,2)]
    ],
    'L': [
        [(2,0),(0,1),(1,1),(2,1)],
        [(1,0),(1,1),(1,2),(2,2)],
        [(0,1),(1,1),(2,1),(0,2)],
        [(0,0),(1,0),(1,1),(1,2)]
    ],
    'O': [
        [(1,0),(2,0),(1,1),(2,1)]
    ],
    'S': [
        [(1,1),(2,1),(0,2),(1,2)],
        [(1,0),(1,1),(2,1),(2,2)]
    ],
    'T': [
        [(1,0),(0,1),(1,1),(2,1)],
        [(1,0),(1,1),(2,1),(1,2)],
        [(0,1),(1,1),(2,1),(1,2)],
        [(1,0),(0,1),(1,1),(1,2)]
    ],
    'Z': [
        [(0,1),(1,1),(1,2),(2,2)],
        [(2,0),(1,1),(2,1),(1,2)]
    ]
}

class Piece:
    def __init__(self, shape):
        self.shape = shape
        self.rotations = SHAPES[shape]
        self.rotation = 0
        self.color = COLORS[shape]
        # Start position above the grid
        self.x = COLS // 2 - 2
        self.y = -2

    def get_cells(self):
        return [(self.x + x, self.y + y) for x, y in self.rotations[self.rotation]]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.rotations)

    def rotate_back(self):
        self.rotation = (self.rotation - 1) % len(self.rotations)

class Board:
    def __init__(self):
        self.grid = [[BLACK for _ in range(COLS)] for _ in range(ROWS)]

    def is_valid(self, piece, dx=0, dy=0):
        for x, y in piece.get_cells():
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= COLS or ny >= ROWS:
                return False
            if ny >= 0 and self.grid[ny][nx] != BLACK:
                return False
        return True

    def add_piece(self, piece):
        for x, y in piece.get_cells():
            if 0 <= y < ROWS and 0 <= x < COLS:
                self.grid[y][x] = piece.color

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(col == BLACK for col in row)]
        cleared = ROWS - len(new_grid)
        for _ in range(cleared):
            new_grid.insert(0, [BLACK for _ in range(COLS)])
        self.grid = new_grid
        return cleared

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.current = self.next_piece()
        self.next = self.next_piece()
        self.score = 0
        self.game_over = False
        pygame.time.set_timer(pygame.USEREVENT, DROP_SPEED)

    def next_piece(self):
        return Piece(random.choice(list(SHAPES.keys())))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.game_over:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.__init__()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.board.is_valid(self.current, dx=-1):
                            self.current.x -= 1
                    elif event.key == pygame.K_RIGHT:
                        if self.board.is_valid(self.current, dx=1):
                            self.current.x += 1
                    elif event.key == pygame.K_DOWN:
                        if self.board.is_valid(self.current, dy=1):
                            self.current.y += 1
                    elif event.key == pygame.K_UP:
                        self.current.rotate()
                        if not self.board.is_valid(self.current):
                            self.current.rotate_back()
                if event.type == pygame.USEREVENT:
                    self.drop()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    while self.board.is_valid(self.current, dy=1):
                        self.current.y += 1
                    self.drop()

    def drop(self):
        if self.board.is_valid(self.current, dy=1):
            self.current.y += 1
        else:
            # lock piece
            self.board.add_piece(self.current)
            cleared = self.board.clear_lines()
            self.score += cleared * 100
            self.current = self.next
            self.next = self.next_piece()
            # check game over
            if not self.board.is_valid(self.current):
                self.game_over = True

    def draw_grid(self):
        for x in range(COLS):
            for y in range(ROWS):
                rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, GREY, rect, 1)

    def draw(self):
        self.screen.fill(BLACK)
        # draw locked blocks
        for y in range(ROWS):
            for x in range(COLS):
                color = self.board.grid[y][x]
                if color != BLACK:
                    rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(self.screen, color, rect)
        # draw current piece
        for x, y in self.current.get_cells():
            if y >= 0:
                rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, self.current.color, rect)
        # grid lines
        self.draw_grid()
        # score
        font = pygame.font.SysFont(None, 30)
        score_surf = font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(score_surf, (5, 5))
        # game over
        if self.game_over:
            over_surf = font.render('Game Over! Press R to restart', True, WHITE)
            self.screen.blit(over_surf, (WIDTH//4, HEIGHT//2))
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.draw()
            self.clock.tick(FPS)


def main():
    Game().run()

if __name__ == '__main__':
    main()
