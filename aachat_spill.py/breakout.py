import pygame
import sys
import random

# Configuration
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Paddle settings
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
PADDLE_SPEED = 8

# Ball settings
BALL_SIZE = 10
BALL_SPEED = 5

# Brick settings
BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_PADDING = 5
TOP_OFFSET = 60
BRICK_WIDTH = (SCREEN_WIDTH - (BRICK_COLS + 1) * BRICK_PADDING) // BRICK_COLS
BRICK_HEIGHT = 20

# Colors
BLACK  = (0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
ORANGE = (255, 165,   0)
YELLOW = (255, 255,   0)
GREEN  = (0,   255,   0)
CYAN   = (0,   255, 255)
COLORS = [RED, ORANGE, YELLOW, GREEN, CYAN]

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(
            (SCREEN_WIDTH - PADDLE_WIDTH) // 2,
            SCREEN_HEIGHT - PADDLE_HEIGHT - 10,
            PADDLE_WIDTH,
            PADDLE_HEIGHT
        )
        self.speed = PADDLE_SPEED

    def move(self, direction):
        if direction == 'left':
            self.rect.x -= self.speed
        elif direction == 'right':
            self.rect.x += self.speed
        # Boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(
            SCREEN_WIDTH // 2 - BALL_SIZE // 2,
            SCREEN_HEIGHT // 2 - BALL_SIZE // 2,
            BALL_SIZE,
            BALL_SIZE
        )
        self.reset()

    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        # Random initial direction
        self.speed_x = BALL_SPEED * random.choice([-1, 1])
        self.speed_y = -BALL_SPEED

    def update(self, paddle, bricks):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Wall collisions
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1

        # Paddle collision
        if self.rect.colliderect(paddle.rect) and self.speed_y > 0:
            self.speed_y *= -1
            # adjust x based on where it hit the paddle
            offset = (self.rect.centerx - paddle.rect.centerx) / (PADDLE_WIDTH // 2)
            self.speed_x = BALL_SPEED * offset

        # Brick collisions
        for brick in bricks:
            if brick.alive and self.rect.colliderect(brick.rect):
                brick.alive = False
                self.speed_y *= -1
                return 10  # score per brick
        return 0

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

class Brick:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.color = color
        self.alive = True

    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(surface, self.color, self.rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Breakout')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.reset()

    def reset(self):
        self.paddle = Paddle()
        self.balls = [Ball()]
        self.lives = 3
        self.score = 0
        self.game_over = False
        # Create bricks
        self.bricks = []
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x = BRICK_PADDING + col * (BRICK_WIDTH + BRICK_PADDING)
                y = TOP_OFFSET + BRICK_PADDING + row * (BRICK_HEIGHT + BRICK_PADDING)
                color = COLORS[min(row, len(COLORS)-1)]
                self.bricks.append(Brick(x, y, color))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset()
            if not self.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    # Add a new ball
                    self.balls.append(Ball())

    def update(self):
        if self.game_over:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move('left')
        if keys[pygame.K_RIGHT]:
            self.paddle.move('right')

        # Update each ball
        for ball in list(self.balls):
            gained = ball.update(self.paddle, self.bricks)
            self.score += gained
            # Check ball lost
            if ball.rect.top > SCREEN_HEIGHT:
                self.balls.remove(ball)
                self.lives -= 1
                if self.lives > 0:
                    # Reset a new ball
                    self.balls.append(Ball())
                else:
                    self.game_over = True

        # Check win
        if all(not b.alive for b in self.bricks):
            self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)
        # Draw bricks
        for brick in self.bricks:
            brick.draw(self.screen)
        # Draw paddle and balls
        self.paddle.draw(self.screen)
        for ball in self.balls:
            ball.draw(self.screen)
        # Draw UI
        score_surf = self.font.render(f'Score: {self.score}', True, WHITE)
        lives_surf = self.font.render(f'Lives: {self.lives}', True, WHITE)
        multi_surf = self.font.render('Press B for extra ball', True, WHITE)
        self.screen.blit(score_surf, (5, 5))
        self.screen.blit(lives_surf, (SCREEN_WIDTH - 200, 5))
        self.screen.blit(multi_surf, (5, SCREEN_HEIGHT - 35))
        if self.game_over:
            msg = 'You Win!' if all(not b.alive for b in self.bricks) else 'Game Over'
            over_surf = self.font.render(msg + ' Press R to Restart', True, WHITE)
            rect = over_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(over_surf, rect)
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
