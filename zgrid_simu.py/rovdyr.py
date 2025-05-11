import pygame
import random
import itertools

# --- Konfigurasjon ---
GRID_WIDTH = 25
GRID_HEIGHT = 25
CELL_SIZE = 20
MARGIN = 2

SCREEN_WIDTH = GRID_WIDTH * (CELL_SIZE + MARGIN) + MARGIN
SCREEN_HEIGHT = GRID_HEIGHT * (CELL_SIZE + MARGIN) + 100  # plass til UI
FPS = 10

# Initielle antall
INITIAL_PLANTS = 50
INITIAL_PREY = 20
INITIAL_PREDATORS = 5

# Tidsparametre (runder)
PLANT_REPRODUCE_TIME = 2
PREY_REPRODUCE_TIME = 3
PREDATOR_REPRODUCE_TIME = 2
PREY_STARVE_TIME = 3
PREDATOR_STARVE_TIME = 10

# Farger (R, G, B)
COLOR_BG        = (30, 30, 30)
COLOR_GRID      = (50, 50, 50)
COLOR_PLANT     = (34, 139, 34)   # grønn for planter
COLOR_PREY      = (255, 215, 0)   # gul for byttedyr
COLOR_PREDATOR  = (200, 50, 50)   # rød for rovdyr
COLOR_EMPTY     = (139, 69, 19)   # brun for tomt
COLOR_TEXT      = (220, 220, 220)

pygame.init()
font = pygame.font.SysFont(None, 24)

class Prey:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reproduce_timer = 0
        self.hunger_timer = 0
        self.alive = True

    def update(self, grid):
        if not self.alive:
            return
        # Beveg: prioriter planter i nabolag
        neighbors = grid.get_neighbors(self.x, self.y)
        plant_neighbors = [pos for pos in neighbors if pos in grid.plant_set]
        if plant_neighbors:
            target = random.choice(plant_neighbors)
        else:
            free_neighbors = [pos for pos in neighbors if grid.is_passable(pos)]
            target = random.choice(free_neighbors) if free_neighbors else (self.x, self.y)
        grid.move_occupant(self, target)
        # Spis plante
        if (self.x, self.y) in grid.plant_set:
            grid.remove_plant(self.x, self.y)
            self.hunger_timer = 0
        else:
            self.hunger_timer += 1
        # Formering
        self.reproduce_timer += 1
        if self.reproduce_timer >= PREY_REPRODUCE_TIME:
            empty = [pos for pos in neighbors if grid.is_passable(pos)]
            if empty:
                x_new, y_new = random.choice(empty)
                grid.add_prey(Prey(x_new, y_new))
            self.reproduce_timer = 0
        # Sulter
        if self.hunger_timer >= PREY_STARVE_TIME:
            grid.remove_prey(self)

    def draw(self, surface):
        px = MARGIN + self.x * (CELL_SIZE + MARGIN)
        py = MARGIN + self.y * (CELL_SIZE + MARGIN)
        pygame.draw.rect(surface, COLOR_PREY, (px, py, CELL_SIZE, CELL_SIZE))

class Predator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reproduce_timer = 0
        self.hunger_timer = 0
        self.alive = True

    def update(self, grid):
        if not self.alive:
            return
        # Sjekk nabodyttedyr
        neighbors = grid.get_neighbors(self.x, self.y)
        prey_neighbors = [pos for pos in neighbors if grid.occupant[pos[0]][pos[1]] and isinstance(grid.occupant[pos[0]][pos[1]], Prey)]
        if prey_neighbors:
            target = random.choice(prey_neighbors)
        else:
            # Finn nærmeste byttedyr
            if grid.prey_list:
                nearest = min(grid.prey_list, key=lambda p: abs(p.x-self.x)+abs(p.y-self.y))
                dx = nearest.x - self.x
                dy = nearest.y - self.y
                step_x = 0 if dx==0 else (1 if dx>0 else -1)
                step_y = 0 if dy==0 else (1 if dy>0 else -1)
                target = (self.x+step_x, self.y+step_y)
            else:
                free_neighbors = [pos for pos in neighbors if grid.is_passable(pos)]
                target = random.choice(free_neighbors) if free_neighbors else (self.x, self.y)
        grid.move_occupant(self, target)
        # Spis byttedyr
        occ = grid.occupant[self.x][self.y]
        if isinstance(occ, Prey):
            grid.remove_prey(occ)
            self.hunger_timer = 0
        else:
            self.hunger_timer += 1
        # Formering
        self.reproduce_timer += 1
        if self.reproduce_timer >= PREDATOR_REPRODUCE_TIME:
            empty = [pos for pos in neighbors if grid.is_passable(pos)]
            if empty:
                x_new, y_new = random.choice(empty)
                grid.add_predator(Predator(x_new, y_new))
            self.reproduce_timer = 0
        # Sulter
        if self.hunger_timer >= PREDATOR_STARVE_TIME:
            grid.remove_predator(self)

    def draw(self, surface):
        px = MARGIN + self.x * (CELL_SIZE + MARGIN)
        py = MARGIN + self.y * (CELL_SIZE + MARGIN)
        pygame.draw.rect(surface, COLOR_PREDATOR, (px, py, CELL_SIZE, CELL_SIZE))

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.plant_set = set()
        self.plant_timer = {}
        self.prey_list = []
        self.predator_list = []
        self.occupant = [[None for _ in range(height)] for _ in range(width)]
        # Init planter
        while len(self.plant_set) < INITIAL_PLANTS:
            x, y = random.randrange(width), random.randrange(height)
            self.add_plant(x, y)
        # Init byttedyr
        while len(self.prey_list) < INITIAL_PREY:
            x, y = random.randrange(width), random.randrange(height)
            if self.occupant[x][y] is None:
                self.add_prey(Prey(x, y))
        # Init rovdyr
        while len(self.predator_list) < INITIAL_PREDATORS:
            x, y = random.randrange(width), random.randrange(height)
            if self.occupant[x][y] is None:
                self.add_predator(Predator(x, y))

    def get_neighbors(self, x, y, diag=False):
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        if diag:
            dirs += [(-1,-1),(-1,1),(1,-1),(1,1)]
        result = []
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                result.append((nx, ny))
        return result

    def is_passable(self, pos):
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height and self.occupant[x][y] is None

    def add_plant(self, x, y):
        if (x, y) not in self.plant_set:
            self.plant_set.add((x, y))
            self.plant_timer[(x, y)] = 0

    def remove_plant(self, x, y):
        self.plant_set.discard((x, y))
        self.plant_timer.pop((x, y), None)

    def add_prey(self, prey):
        self.prey_list.append(prey)
        self.occupant[prey.x][prey.y] = prey

    def remove_prey(self, prey):
        prey.alive = False
        self.occupant[prey.x][prey.y] = None
        if prey in self.prey_list:
            self.prey_list.remove(prey)

    def add_predator(self, predator):
        self.predator_list.append(predator)
        self.occupant[predator.x][predator.y] = predator

    def remove_predator(self, predator):
        predator.alive = False
        self.occupant[predator.x][predator.y] = None
        if predator in self.predator_list:
            self.predator_list.remove(predator)

    def move_occupant(self, entity, target):
        self.occupant[entity.x][entity.y] = None
        entity.x, entity.y = target
        self.occupant[target[0]][target[1]] = entity

    def update(self):
        # Planter sprer seg
        to_add = []
        for pos in list(self.plant_set):
            self.plant_timer[pos] += 1
            if self.plant_timer[pos] >= PLANT_REPRODUCE_TIME:
                neighbors = self.get_neighbors(pos[0], pos[1])
                empty = [n for n in neighbors if n not in self.plant_set and self.occupant[n[0]][n[1]] is None]
                if empty:
                    to_add.append(random.choice(empty))
                self.plant_timer[pos] = 0
        for x, y in to_add:
            self.add_plant(x, y)
        # Oppdater dyr
        for prey in list(self.prey_list):
            prey.update(self)
        for predator in list(self.predator_list):
            predator.update(self)

    def draw(self, surface):
        surface.fill(COLOR_BG)
        # Tegn celler
        for x in range(self.width):
            for y in range(self.height):
                px = MARGIN + x*(CELL_SIZE + MARGIN)
                py = MARGIN + y*(CELL_SIZE + MARGIN)
                if (x, y) in self.plant_set:
                    color = COLOR_PLANT
                elif self.occupant[x][y] is None:
                    color = COLOR_EMPTY
                elif isinstance(self.occupant[x][y], Prey):
                    color = COLOR_PREY
                else:
                    color = COLOR_PREDATOR
                pygame.draw.rect(surface, color, (px, py, CELL_SIZE, CELL_SIZE))
        # Tegn dyr
        for prey in self.prey_list:
            prey.draw(surface)
        for predator in self.predator_list:
            predator.draw(surface)
        # Tegn UI
        total_plants = len(self.plant_set)
        total_prey   = len(self.prey_list)
        total_pred   = len(self.predator_list)
        info = font.render(f"Planter: {total_plants}   Byttedyr: {total_prey}   Rovdyr: {total_pred}   ", True, COLOR_TEXT)
        surface.blit(info, (10, SCREEN_HEIGHT - 80))
        inst = font.render("SPACE: pause/unpause    Lukk vindu for å avslutte", True, COLOR_TEXT)
        surface.blit(inst, (10, SCREEN_HEIGHT - 50))


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Økosystem-simulering")
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
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()