import pygame
import sys
import random

# Configuration
CELL_SIZE = 20    # Size of each grid cell
GRID_WIDTH = 30   # Number of cells horizontally
GRID_HEIGHT = 20  # Number of cells vertically
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10          # Initial game speed (frames per second)

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (40, 40, 40)


class Snake:
    def __init__(self):
        # Start in the center
        x = GRID_WIDTH // 2
        y = GRID_HEIGHT // 2
        self.body = [(x, y), (x - 1, y), (x - 2, y)]
        self.direction = (1, 0)  # moving to the right
        self.grow = False

    def set_direction(self, new_dir):
        # Prevent reversing
        if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
            self.direction = new_dir

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def collide_self(self):
        return self.body[0] in self.body[1:]

    def collide_wall(self):
        x, y = self.body[0]
        return not (0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT)


class Food:
    def __init__(self, snake_body):
        self.position = None
        self.spawn(snake_body)

    def spawn(self, snake_body):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake_body:
                self.position = (x, y)
                return


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)

        self.reset()

    def reset(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.score = 0
        self.game_over = False

    def update(self):
        if self.game_over:
            return
        self.snake.move()
        # Check collisions
        if self.snake.collide_wall() or self.snake.collide_self():
            self.game_over = True
            return
        # Check food
        if self.snake.body[0] == self.food.position:
            self.snake.grow = True
            self.score += 1
            self.food.spawn(self.snake.body)

    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (SCREEN_WIDTH, y))

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid()
        # Draw snake
        for segment in self.snake.body:
            rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, GREEN, rect)
        # Draw food
        fx, fy = self.food.position
        food_rect = pygame.Rect(fx * CELL_SIZE, fy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen, RED, food_rect)
        # Draw score
        score_surf = self.font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(score_surf, (10, 10))
        # Draw game over
        if self.game_over:
            over_surf = self.font.render('Game Over! Press R to restart.', True, WHITE)
            rect = over_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(over_surf, rect)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.set_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.snake.set_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.set_direction((1, 0))
                elif event.key == pygame.K_r and self.game_over:
                    self.reset()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS + self.score // 5)  # Increase speed as score grows


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
