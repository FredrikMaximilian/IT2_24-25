import pygame
import sys
import random

# Configuration
CELL_SIZE = 60            # Size of each grid cell
GRID_SIZE = 10            # 10x10 grid
MARGIN = 60               # Space at bottom for messages
SCREEN_WIDTH = CELL_SIZE * GRID_SIZE
SCREEN_HEIGHT = CELL_SIZE * GRID_SIZE + MARGIN
FPS = 30                  # Frame rate

# Colors (R, G, B)
BG_COLOR = (230, 230, 230)
GRID_COLOR = (50, 50, 50)
LADDER_COLOR = (0, 200, 0)
SNAKE_COLOR = (200, 0, 0)
TEXT_COLOR = (20, 20, 20)
PLAYER_COLORS = [(0, 0, 200), (200, 200, 0)]

# Snakes and Ladders mapping: start -> end
TRANSITIONS = {
    # Ladders
    2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44,
    51: 67, 71: 91, 78: 98, 87: 94,
    # Snakes
    16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53,
    89: 68, 92: 88, 95: 75, 99: 80
}

pygame.init()
FONT = pygame.font.SysFont(None, 36)
SMALL_FONT = pygame.font.SysFont(None, 24)


def num_to_coords(num):
    """Convert board number (1-100) to pixel coordinates (top-left of cell)."""
    idx = max(1, min(100, num)) - 1
    row = idx // GRID_SIZE
    col = idx % GRID_SIZE
    # zig-zag on alternate rows
    if row % 2 == 1:
        col = GRID_SIZE - 1 - col
    x = col * CELL_SIZE
    # row 0 is bottom
    y = SCREEN_HEIGHT - MARGIN - (row + 1) * CELL_SIZE
    return x, y

class Player:
    def __init__(self, idx):
        self.idx = idx
        self.position = 1
        self.color = PLAYER_COLORS[idx]

    def move(self, steps):
        target = self.position + steps
        if target <= 100:
            self.position = target
            # check for snake or ladder
            if self.position in TRANSITIONS:
                self.position = TRANSITIONS[self.position]

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Stigespill')
        self.clock = pygame.time.Clock()
        self.players = [Player(0), Player(1)]
        self.current = 0
        self.dice_roll = 0
        self.message = 'Trykk MELLOMROM for å kaste terning'
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.game_over:
                    self.roll()
                elif event.key == pygame.K_r and self.game_over:
                    self.reset()

    def roll(self):
        self.dice_roll = random.randint(1, 6)
        player = self.players[self.current]
        player.move(self.dice_roll)
        self.message = f'Spiller {self.current+1} kastet {self.dice_roll}'
        if player.position == 100:
            self.message = f'Spiller {self.current+1} vant! Trykk R for ny runde.'
            self.game_over = True
        else:
            self.current = (self.current + 1) % len(self.players)

    def reset(self):
        for p in self.players:
            p.position = 1
        self.current = 0
        self.dice_roll = 0
        self.message = 'Trykk MELLOMROM for å kaste terning'
        self.game_over = False

    def draw_board(self):
        # background
        self.screen.fill(BG_COLOR)
        # grid lines
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT - MARGIN))
        for y in range(0, SCREEN_HEIGHT - MARGIN, CELL_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))
        # draw transitions
        for start, end in TRANSITIONS.items():
            sx, sy = num_to_coords(start)
            ex, ey = num_to_coords(end)
            # centers
            sx += CELL_SIZE // 2
            sy += CELL_SIZE // 2
            ex += CELL_SIZE // 2
            ey += CELL_SIZE // 2
            color = LADDER_COLOR if end > start else SNAKE_COLOR
            width = 6 if end > start else 4
            pygame.draw.line(self.screen, color, (sx, sy), (ex, ey), width)
            # arrowhead
            dx, dy = ex - sx, ey - sy
            dist = max((dx**2 + dy**2)**0.5, 1)
            ux, uy = dx/dist, dy/dist
            # two side points
            perp = (-uy, ux)
            arrow_size = 10
            p1 = (ex, ey)
            p2 = (ex - ux*arrow_size + perp[0]*arrow_size/2,
                  ey - uy*arrow_size + perp[1]*arrow_size/2)
            p3 = (ex - ux*arrow_size - perp[0]*arrow_size/2,
                  ey - uy*arrow_size - perp[1]*arrow_size/2)
            pygame.draw.polygon(self.screen, color, [p1, p2, p3])

    def draw_players(self):
        for p in self.players:
            x, y = num_to_coords(p.position)
            # draw token as small square
            pad = CELL_SIZE // 4
            rect = pygame.Rect(x+pad, y+pad, CELL_SIZE//2, CELL_SIZE//2)
            pygame.draw.rect(self.screen, p.color, rect)

    def draw_ui(self):
        # draw message
        text = FONT.render(self.message, True, TEXT_COLOR)
        self.screen.blit(text, (10, SCREEN_HEIGHT - MARGIN + 10))
        # draw current player indicator
        if not self.game_over:
            indicator = SMALL_FONT.render(
                f"Tur: Spiller {self.current+1}", True, TEXT_COLOR)
            self.screen.blit(indicator, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - MARGIN + 15))

    def run(self):
        while True:
            self.handle_events()
            self.draw_board()
            self.draw_players()
            self.draw_ui()
            pygame.display.flip()
            self.clock.tick(FPS)


def main():
    Game().run()

if __name__ == '__main__':
    main()
