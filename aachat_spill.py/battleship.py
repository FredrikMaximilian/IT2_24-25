import pygame as pg
import sys
import random

# Configuration
CELL_SIZE = 40      # Size of each grid cell
GRID_SIZE = 10      # 10x10 grid
MARGIN = 50         # Space at bottom for messages
SCREEN_WIDTH = CELL_SIZE * GRID_SIZE
SCREEN_HEIGHT = CELL_SIZE * GRID_SIZE + MARGIN

# Colors (R, G, B)
SEA_COLOR = (0, 105, 148)
GRID_COLOR = (40, 40, 40)
HIT_COLOR = (255, 0, 0)
MISS_COLOR = (255, 255, 255)
TEXT_COLOR = (255, 255, 255)

SHIP_LENGTHS = [5, 4, 3, 3, 2]  # Standard Battleship lengths

class Ship:
    def __init__(self, positions):
        self.positions = positions  # list of (x, y)
        self.hits = set()

    def register_hit(self, pos):
        if pos in self.positions:
            self.hits.add(pos)
            return True
        return False

    def is_sunk(self):
        return set(self.positions) == self.hits

class Board:
    def __init__(self, size, ship_lengths):
        self.size = size
        self.ship_lengths = ship_lengths
        self.ships = []
        self.hits = set()
        self.misses = set()
        self.place_ships_randomly()

    def place_ships_randomly(self):
        taken = set()
        for length in self.ship_lengths:
            placed = False
            while not placed:
                horizontal = random.choice([True, False])
                if horizontal:
                    x = random.randint(0, self.size - length)
                    y = random.randint(0, self.size - 1)
                    positions = [(x + i, y) for i in range(length)]
                else:
                    x = random.randint(0, self.size - 1)
                    y = random.randint(0, self.size - length)
                    positions = [(x, y + i) for i in range(length)]
                if not any(pos in taken for pos in positions):
                    self.ships.append(Ship(positions))
                    taken.update(positions)
                    placed = True

    def receive_shot(self, pos):
        if pos in self.hits or pos in self.misses:
            return None  # already shot here
        for ship in self.ships:
            if ship.register_hit(pos):
                self.hits.add(pos)
                return ('hit', ship.is_sunk())
        self.misses.add(pos)
        return ('miss', False)

    def all_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('Slagskip')
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont(None, 36)
        self.reset()

    def reset(self):
        self.board = Board(GRID_SIZE, SHIP_LENGTHS)
        self.game_over = False
        self.message = 'Klikk for å skyte!'  # Click to shoot!

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN and not self.game_over:
                x, y = event.pos
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:
                    result = self.board.receive_shot((col, row))
                    if result:
                        if result[0] == 'hit':
                            if result[1]:
                                self.message = 'Senketr àt!'
                            else:
                                self.message = 'Treff!'
                        elif result[0] == 'miss':
                            self.message = 'Bom!'
                        if self.board.all_sunk():
                            self.game_over = True
                            self.message = 'Alle skip er senket! Trykk R for ny runde.'
            elif event.type == pg.KEYDOWN and self.game_over:
                if event.key == pg.K_r:
                    self.reset()

    def draw(self):
        self.screen.fill(SEA_COLOR)
        # Draw grid
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pg.draw.line(self.screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT - MARGIN))
        for y in range(0, SCREEN_HEIGHT - MARGIN, CELL_SIZE):
            pg.draw.line(self.screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))
        # Draw hits and misses
        for (col, row) in self.board.misses:
            rect = pg.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pg.draw.rect(self.screen, MISS_COLOR, rect)
        for (col, row) in self.board.hits:
            rect = pg.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pg.draw.rect(self.screen, HIT_COLOR, rect)
        # Draw message
        text_surf = self.font.render(self.message, True, TEXT_COLOR)
        self.screen.blit(text_surf, (10, SCREEN_HEIGHT - MARGIN + 10))
        pg.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.draw()
            self.clock.tick(30)


def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()
