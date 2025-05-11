import pygame
import random
import itertools

# --- Konfigurasjon ---
GRID_WIDTH = 25
GRID_HEIGHT = 25
CELL_SIZE = 20
MARGIN = 2  # mellom celler

SCREEN_WIDTH = GRID_WIDTH * (CELL_SIZE + MARGIN) + MARGIN
SCREEN_HEIGHT = GRID_HEIGHT * (CELL_SIZE + MARGIN) + 100  # ekstra for UI
FPS = 5  # oppdateringer per sekund

# Fire spread og burn tidsparametre
MIN_BURN_TIME = 1  # runder
MAX_BURN_TIME = 2
INITIAL_FIRES = 1
FIREFIGHTERS = 6

# Farger (RGB)
COLOR_BG        = (30, 30, 30)
COLOR_GRID      = (50, 50, 50)
COLOR_TREE      = (34, 139, 34)    # grønn
COLOR_FIRE      = (255, 69, 0)     # oransje-rød
COLOR_BURNT     = (80, 80, 80)     # grå-sort
COLOR_EMPTY     = (139, 69, 19)    # brun
COLOR_FF        = (30, 144, 255)   # blå for brannmannskap
COLOR_TEXT      = (220, 220, 220)

# Celle-tilstander
EMPTY = 0
TREE = 1
FIRE = 2
BURNT = 3

pygame.init()
font = pygame.font.SysFont(None, 24)

class Firefighter:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, grid):
        fires = grid.get_fire_positions()
        if not fires:
            return
        # Finn nærmeste brann (Manhattan)
        nearest = min(fires, key=lambda pos: abs(pos[0]-self.x)+abs(pos[1]-self.y))
        dx = nearest[0] - self.x
        dy = nearest[1] - self.y
        # Hvis adjacent, slukk
        if abs(dx) + abs(dy) == 1:
            grid.extinguish(nearest)
            return
        # Beveg ett steg mot brannen
        step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
        step_y = 0 if dy == 0 else (1 if dy > 0 else -1)
        new_x = self.x + step_x
        new_y = self.y + step_y
        # Flytte kun om cellen er passable
        if grid.is_passable(new_x, new_y):
            self.x, self.y = new_x, new_y

    def draw(self, surface):
        px = MARGIN + self.x * (CELL_SIZE + MARGIN)
        py = MARGIN + self.y * (CELL_SIZE + MARGIN)
        pygame.draw.rect(surface, COLOR_FF, (px, py, CELL_SIZE, CELL_SIZE))

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Initialiser alle celler som trær
        self.state = [[TREE for _ in range(height)] for _ in range(width)]
        # Burn-timere for brennende trær
        self.burn_timer = {}
        # Brannmannskap
        self.firefighters = []
        # Sett random startbranner
        for _ in range(INITIAL_FIRES):
            x = random.randint(0, width-1)
            y = random.randint(0, height-1)
            self.ignite((x, y))
        # Plasser brannmannskap ved hjørnene
        '''
        corners = [(0,0), (width-1, 0), (0, height-1), (width-1, height-1)]
        for i in range(FIREFIGHTERS):
            cx, cy = corners[i % len(corners)]
            self.firefighters.append(Firefighter(cx, cy))'''

        taken = set((x, y) for x in range(width) for y in range(height) if self.state[x][y] == FIRE)
        while len(self.firefighters) < FIREFIGHTERS:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            if (x, y) not in taken:
                self.firefighters.append(Firefighter(x, y))
                taken.add((x, y))

    def ignite(self, pos):
        x, y = pos
        if self.state[x][y] == TREE:
            self.state[x][y] = FIRE
            # Sett nedteller for brenning
            self.burn_timer[(x,y)] = random.randint(MIN_BURN_TIME, MAX_BURN_TIME)

    def extinguish(self, pos):
        x, y = pos
        if self.state[x][y] == FIRE:
            self.state[x][y] = BURNT
            # Fjern burn timer
            self.burn_timer.pop((x,y), None)

    def get_fire_positions(self):
        return [(x,y) for (x,y), t in self.burn_timer.items()]

    def is_passable(self, x, y):
        # Brannmannskap kan gå gjennom tomme, utbrente og trær, men ikke brennende
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.state[x][y] != FIRE
        return False

    def update(self):
        # 1) Spre brann
        to_ignite = []
        for (x,y), t in list(self.burn_timer.items()):
            # Undersøk alle 8 naboceller
            for dx, dy in itertools.product([-1,0,1], repeat=2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x+dx, y+dy
                if (dx!=0 or dy!=0) and 0<=nx<self.width and 0<=ny<self.height:
                    if self.state[nx][ny] == TREE:
                        to_ignite.append((nx,ny))
        for pos in to_ignite:
            self.ignite(pos)
        # 2) Oppdater burn timere
        finished = []
        for pos in list(self.burn_timer.keys()):
            self.burn_timer[pos] -= 1
            if self.burn_timer[pos] <= 0:
                finished.append(pos)
        for pos in finished:
            x,y = pos
            self.state[x][y] = BURNT
            self.burn_timer.pop(pos, None)
        # 3) Oppdater brannmannskap
        for ff in self.firefighters:
            ff.update(self)

    def draw(self, surface):
        # Bakgrunn
        surface.fill(COLOR_BG)
        # Tegn celler
        for x in range(self.width):
            for y in range(self.height):
                px = MARGIN + x*(CELL_SIZE+MARGIN)
                py = MARGIN + y*(CELL_SIZE+MARGIN)
                st = self.state[x][y]
                if st == TREE:
                    color = COLOR_TREE
                elif st == FIRE:
                    color = COLOR_FIRE
                elif st == BURNT:
                    color = COLOR_BURNT
                else:
                    color = COLOR_EMPTY
                pygame.draw.rect(surface, color, (px, py, CELL_SIZE, CELL_SIZE))
        # Tegn brannmannskap
        for ff in self.firefighters:
            ff.draw(surface)

# --- Hovedløkke ---
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Skogbrann-simulering")
    clock = pygame.time.Clock()
    grid = Grid(GRID_WIDTH, GRID_HEIGHT)
    paused = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = not paused
        if not paused:
            grid.update()
        grid.draw(screen)
        # UI
        healthy = sum(1 for row in grid.state for st in row if st == TREE)
        burning = len(grid.get_fire_positions())
        burnt = sum(1 for row in grid.state for st in row if st == BURNT)
        info = font.render(f"Friskt: {healthy}   Brennende: {burning}   Utbrent: {burnt}   {'PAUSED' if paused else ''}", True, COLOR_TEXT)
        screen.blit(info, (10, SCREEN_HEIGHT - 80))
        inst = font.render("SPACE: pause/unpause    Lukk vindu for å avslutte", True, COLOR_TEXT)
        screen.blit(inst, (10, SCREEN_HEIGHT - 50))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()
