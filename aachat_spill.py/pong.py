import pygame
import sys
import random

# Configuration
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 10
PADDLE_SPEED = 7
BALL_SPEED = 5
FPS = 60

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Paddle:
    def __init__(self, x_pos):
        self.rect = pygame.Rect(
            x_pos,
            (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2,
            PADDLE_WIDTH,
            PADDLE_HEIGHT
        )
        self.speed = PADDLE_SPEED

    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        # Keep paddle on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(
            (SCREEN_WIDTH - BALL_SIZE) // 2,
            (SCREEN_HEIGHT - BALL_SIZE) // 2,
            BALL_SIZE,
            BALL_SIZE
        )
        self.speed_x = BALL_SPEED * random.choice((1, -1))
        self.speed_y = BALL_SPEED * random.choice((1, -1))

    def update(self, paddle1, paddle2):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Bounce top/bottom
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1
        # Bounce off paddles
        if self.rect.colliderect(paddle1.rect) and self.speed_x < 0:
            self.speed_x *= -1
        if self.rect.colliderect(paddle2.rect) and self.speed_x > 0:
            self.speed_x *= -1

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x = BALL_SPEED * random.choice((1, -1))
        self.speed_y = BALL_SPEED * random.choice((1, -1))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pong')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 48)
        self.reset()

    def reset(self):
        self.paddle1 = Paddle(10)
        self.paddle2 = Paddle(SCREEN_WIDTH - PADDLE_WIDTH - 10)
        self.ball = Ball()
        self.score1 = 0
        self.score2 = 0
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_over:
                if event.key == pygame.K_r:
                    self.reset()

    def update(self):
        if not self.game_over:
            keys = pygame.key.get_pressed()
            # Player 1: W/S
            if keys[pygame.K_w]:
                self.paddle1.move(up=True)
            if keys[pygame.K_s]:
                self.paddle1.move(up=False)
            # Player 2: Up/Down arrows
            if keys[pygame.K_UP]:
                self.paddle2.move(up=True)
            if keys[pygame.K_DOWN]:
                self.paddle2.move(up=False)

            self.ball.update(self.paddle1, self.paddle2)
            # Check scoring
            if self.ball.rect.left <= 0:
                self.score2 += 1
                self.ball.reset()
            if self.ball.rect.right >= SCREEN_WIDTH:
                self.score1 += 1
                self.ball.reset()
            # Check victory (first to 5)
            if self.score1 >= 5 or self.score2 >= 5:
                self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)
        # Middle dashed line
        for y in range(0, SCREEN_HEIGHT, 20):
            pygame.draw.rect(
                self.screen,
                WHITE,
                (SCREEN_WIDTH // 2 - 1, y, 2, 10)
            )
        # Draw paddles and ball
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        self.ball.draw(self.screen)
        # Draw scores
        score_surf1 = self.font.render(str(self.score1), True, WHITE)
        score_surf2 = self.font.render(str(self.score2), True, WHITE)
        self.screen.blit(
            score_surf1,
            (SCREEN_WIDTH // 4 - score_surf1.get_width() // 2, 20)
        )
        self.screen.blit(
            score_surf2,
            (3 * SCREEN_WIDTH // 4 - score_surf2.get_width() // 2, 20)
        )
        # Game over message
        if self.game_over:
            winner = 'Spiller 1 vant!' if self.score1 > self.score2 else 'Spiller 2 vant!'
            over_surf = self.font.render(winner, True, WHITE)
            over_rect = over_surf.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)
            )
            self.screen.blit(over_surf, over_rect)
            instr_surf = self.font.render('Trykk R for ny runde', True, WHITE)
            instr_rect = instr_surf.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)
            )
            self.screen.blit(instr_surf, instr_rect)
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
