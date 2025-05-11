import pygame
import sys
import random

# --- Konfigurasjon ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
ROAD_Y = SCREEN_HEIGHT // 2
ROAD_HEIGHT = 60
CAR_WIDTH, CAR_HEIGHT = 40, 20
SPAWN_INTERVAL_RANGE = (2000, 4000)  # ms
MAX_SPEED = 2.0       # pixels per frame
ACCELERATION = 0.02   # pixels per frame^2
DECELERATION = 0.05   # pixels per frame^2
SAFE_DISTANCE = 50    # pixels
LIGHT_POSITION = (SCREEN_WIDTH // 2, ROAD_Y)
LIGHT_CYCLE = [  # (color, duration_ms)
    ((0, 255, 0), 5000),   # Green
    ((255, 255, 0), 2000), # Yellow
    ((255, 0, 0), 5000)    # Red
]

class TrafficLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y - 20
        self.state_index = 0
        self.timer = 0
        self.color, self.duration = LIGHT_CYCLE[self.state_index]

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.duration:
            self.timer -= self.duration
            self.state_index = (self.state_index + 1) % len(LIGHT_CYCLE)
            self.color, self.duration = LIGHT_CYCLE[self.state_index]

    def draw(self, surface):
        # draw pole
        pygame.draw.rect(surface, (50, 50, 50), (self.x - 5, self.y - 40, 10, 40))
        # draw light
        pygame.draw.circle(surface, self.color, (self.x, self.y), 10)

    def is_red(self):
        return self.color == (255, 0, 0)

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0.0
        self.width = CAR_WIDTH
        self.height = CAR_HEIGHT
        self.color = (0, 0, 255)
        self.stopped = False

    def update(self, dt, cars, light):
        # Determine distance to next obstacle (car or red light)
        obstacle_dist = float('inf')
        # check next car
        for other in cars:
            if other is not self and other.x > self.x:
                dist = other.x - self.x - self.width
                if dist < obstacle_dist:
                    obstacle_dist = dist
        # check red light
        if light.is_red() and light.x > self.x:
            dist_to_light = light.x - self.x - self.width
            if dist_to_light < obstacle_dist:
                obstacle_dist = dist_to_light

        # Adjust speed
        if obstacle_dist < SAFE_DISTANCE:
            # decelerate or stop
            self.speed = max(0.0, self.speed - DECELERATION)
        else:
            # accelerate up to max
            self.speed = min(MAX_SPEED, self.speed + ACCELERATION)

        # update position
        self.x += self.speed * (dt / (1000 / FPS))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (int(self.x), int(self.y - self.height//2), self.width, self.height))

class TrafficSimulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Trafikksimulering")
        self.clock = pygame.time.Clock()
        self.light = TrafficLight(*LIGHT_POSITION)
        self.cars = []
        self.spawn_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.spawn_event, random.randint(*SPAWN_INTERVAL_RANGE))

    def spawn_car(self):
        # spawn at left edge, centered on road
        car = Car(-CAR_WIDTH, ROAD_Y + ROAD_HEIGHT//4)
        self.cars.append(car)

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == self.spawn_event:
                    self.spawn_car()
                    pygame.time.set_timer(self.spawn_event, random.randint(*SPAWN_INTERVAL_RANGE))

            # update
            self.light.update(dt)
            for car in list(self.cars):
                car.update(dt, self.cars, self.light)
                # remove cars that have left the screen
                if car.x > SCREEN_WIDTH:
                    self.cars.remove(car)

            # draw
            self.screen.fill((135, 206, 235))  # sky blue
            # draw road
            pygame.draw.rect(self.screen, (50, 50, 50), (0, ROAD_Y - ROAD_HEIGHT//2, SCREEN_WIDTH, ROAD_HEIGHT))
            self.light.draw(self.screen)
            for car in self.cars:
                car.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    sim = TrafficSimulation()
    sim.run()
