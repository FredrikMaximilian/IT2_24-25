import pygame
import random
import math

# --- Konfigurasjon ---
GRID_WIDTH = 30
GRID_HEIGHT = 30
CELL_SIZE = 20
MARGIN = 1  # mellom celler

SCREEN_WIDTH = GRID_WIDTH * (CELL_SIZE + MARGIN) + MARGIN
SCREEN_HEIGHT = GRID_HEIGHT * (CELL_SIZE + MARGIN) + 100  # ekstra for UI

FPS = 3  # oppdateringer per sekund

# Farger
COLOR_BG = (30, 30, 30)
COLOR_GRID = (50, 50, 50)
COLOR_RED = (200, 50, 50)
COLOR_BLUE = (50, 50, 200)
COLOR_CORPSE = (100, 100, 100)
COLOR_HP_BG = (50, 50, 50)
COLOR_HP = (50, 200, 50)
COLOR_TEXT = (220, 220, 220)

# Soldat-parametere
INIT_HP = 10
ATTACK_POWER = 2
SIGHT_RANGE = 2
CORPSE_LIFETIME = FPS * 5  # sekunder i runder

NUM_RED = 50
NUM_BLUE = 50

pygame.init()
font = pygame.font.SysFont(None, 24)

# --- Klasser ---
class Soldier:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team  # 'red' eller 'blue'
        self.hp = INIT_HP
        self.alive = True

    def update(self, grid, enemies):
        if not self.alive:
            return
        # Sjekk fiender tett på #hm
        targets = [e for e in enemies if abs(e.x - self.x) + abs(e.y - self.y) == 1 and e.alive]
        if targets:
            # Angrip første
            target = targets[0] #min(targets, key=lambda e: e.hp)
            target.hp -= ATTACK_POWER
            if target.hp <= 0:
                target.alive = False
                grid.add_corpse(target.x, target.y)
        else:
            # Finn nærmeste fiende #hm
            if not enemies:
                return
            nearest = min(enemies, key=lambda e: abs(e.x - self.x) + abs(e.y - self.y) if e.alive else GRID_WIDTH+GRID_HEIGHT)
            dx = nearest.x - self.x
            dy = nearest.y - self.y
            # Ta ett steg
            step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
            step_y = 0 if dy == 0 else (1 if dy > 0 else -1)
            new_x = self.x + step_x
            new_y = self.y + step_y
            if grid.is_empty(new_x, new_y):
                grid.move_soldier(self, new_x, new_y)

    def draw(self, surface): #hm 
        px = MARGIN + self.x * (CELL_SIZE + MARGIN)
        py = MARGIN + self.y * (CELL_SIZE + MARGIN)
        color = COLOR_RED if self.team == 'red' else COLOR_BLUE
        pygame.draw.rect(surface, color, (px, py, CELL_SIZE, CELL_SIZE))
        # Tegn HP-bar
        bar_width = CELL_SIZE
        bar_height = 4
        hp_frac = max(self.hp / INIT_HP, 0)
        pygame.draw.rect(surface, COLOR_HP_BG, (px, py + CELL_SIZE - bar_height, bar_width, bar_height))
        pygame.draw.rect(surface, COLOR_HP, (px, py + CELL_SIZE - bar_height, bar_width * hp_frac, bar_height))

class Corpse:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = CORPSE_LIFETIME

    def update(self):
        self.timer -= 1
        return self.timer <= 0  # True hvis skal fjernes

    def draw(self, surface):
        px = MARGIN + self.x * (CELL_SIZE + MARGIN)
        py = MARGIN + self.y * (CELL_SIZE + MARGIN)
        pygame.draw.rect(surface, COLOR_CORPSE, (px, py, CELL_SIZE, CELL_SIZE))

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.soldiers = []
        self.corpses = []
        self.cells = [[None for _ in range(height)] for _ in range(width)]

    def add_soldier(self, soldier):
        self.soldiers.append(soldier)
        self.cells[soldier.x][soldier.y] = soldier

    def move_soldier(self, soldier, new_x, new_y):
        self.cells[soldier.x][soldier.y] = None
        soldier.x = new_x
        soldier.y = new_y
        self.cells[new_x][new_y] = soldier

    def add_corpse(self, x, y):
        self.corpses.append(Corpse(x, y))
        self.cells[x][y] = None

    def is_empty(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return self.cells[x][y] is None

    def update(self):
        # Opprett lister for hvert lag
        red = [s for s in self.soldiers if s.team == 'red' and s.alive]
        blue = [s for s in self.soldiers if s.team == 'blue' and s.alive]
        # Oppdater soldater
        for s in self.soldiers:
            if s.alive:
                enemies = blue if s.team == 'red' else red
                s.update(self, enemies)
        # Oppdater lik
        self.corpses = [c for c in self.corpses if not c.update()]

    def draw(self, surface):
        # Bakgrunn
        surface.fill(COLOR_BG)
        # Grid-ruter
        for x in range(self.width):
            for y in range(self.height):
                px = MARGIN + x * (CELL_SIZE + MARGIN)
                py = MARGIN + y * (CELL_SIZE + MARGIN)
                pygame.draw.rect(surface, COLOR_GRID, (px, py, CELL_SIZE, CELL_SIZE))
        # Corpses
        for c in self.corpses:
            c.draw(surface)
        # Soldater
        for s in self.soldiers:
            if s.alive:
                s.draw(surface)

# --- Hovedprogram ---
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Slagsimulering")
    clock = pygame.time.Clock()

    grid = Grid(GRID_WIDTH, GRID_HEIGHT)
    # Plasser soldater
    # Røde
    while len([s for s in grid.soldiers if s.team == 'red']) < NUM_RED:
        x = random.randint(0, GRID_WIDTH//2 - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        if grid.is_empty(x, y):
            grid.add_soldier(Soldier(x, y, 'red'))
    # Blå
    while len([s for s in grid.soldiers if s.team == 'blue']) < NUM_BLUE:
        x = random.randint(GRID_WIDTH//2, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        if grid.is_empty(x, y):
            grid.add_soldier(Soldier(x, y, 'blue'))

    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = not paused

        if not paused:
            grid.update()

        grid.draw(screen)
        # UI-panel
        red_alive = len([s for s in grid.soldiers if s.team == 'red' and s.alive])
        blue_alive = len([s for s in grid.soldiers if s.team == 'blue' and s.alive])
        text = font.render(f"Rød: {red_alive}    Blå: {blue_alive}    {'PAUSED' if paused else ''}", True, COLOR_TEXT)
        screen.blit(text, (10, SCREEN_HEIGHT - 80))
        instr = font.render("SPACE: pause/unpause    Q or close window to quit", True, COLOR_TEXT)
        screen.blit(instr, (10, SCREEN_HEIGHT - 50))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
