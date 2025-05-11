import pygame
import sys
import os

# Enkel sjakk med bilder for ekte utseende
# Krever en mappe "images" med PNG-filer for hver brikke:
# wP.png, wR.png, wN.png, wB.png, wQ.png, wK.png
# bP.png, bR.png, bN.png, bB.png, bQ.png, bK.png
# Installer Pygame: pip install pygame

# Skjermkonstanter
WIDTH, HEIGHT = 600, 600
SQ_SIZE = WIDTH // 8
FPS = 30

# Farger
LIGHT_COLOR = (240, 217, 181)
DARK_COLOR = (181, 136, 99)
HIGHLIGHT_COLOR = (0, 255, 0, 100)

# Initial brettoppsett (brikke-notation)
initial_board = [
    ['r','n','b','q','k','b','n','r'],
    ['p']*8,
    ['.']*8,
    ['.']*8,
    ['.']*8,
    ['.']*8,
    ['P']*8,
    ['R','N','B','Q','K','B','N','R']
]

class ChessGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sjakkspill")
        self.clock = pygame.time.Clock()

        # Last inn brikkebilder
        self.piece_images = self.load_images()

        # Klargjør brett
        self.board = [row.copy() for row in initial_board]
        self.selected = None  # valgt rute (rad, kol)
        self.turn = 'white'   # 'white' eller 'black'

    def load_images(self):
        """Laster inn og skalerer bilder fra /images"""
        images = {}
        for color in ('w','b'):
            for piece in ('P','R','N','B','Q','K'):
                filename = f"{color}{piece}.png"
                path = os.path.join('images', filename)
                if not os.path.isfile(path):
                    raise FileNotFoundError(f"Fant ikke bilde: {path}")
                img = pygame.image.load(path)
                images[color + piece] = pygame.transform.scale(img, (SQ_SIZE, SQ_SIZE))
        return images

    def draw_board(self):
        """Tegn ruter og brikker"""
        for r in range(8):
            for c in range(8):
                color = LIGHT_COLOR if (r + c) % 2 == 0 else DARK_COLOR
                rect = pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(self.screen, color, rect)

                piece = self.board[r][c]
                if piece != '.':
                    # Velg riktig bilde
                    color_prefix = 'w' if piece.isupper() else 'b'
                    key = color_prefix + piece.upper()
                    img = self.piece_images[key]
                    self.screen.blit(img, rect.topleft)

    def get_square_under_mouse(self, pos):
        x, y = pos
        c = x // SQ_SIZE
        r = y // SQ_SIZE
        if 0 <= r < 8 and 0 <= c < 8:
            return (r, c)
        return None

    def is_path_clear(self, sr, sc, er, ec):
        dr = er - sr
        dc = ec - sc
        step_r = (dr > 0) - (dr < 0)
        step_c = (dc > 0) - (dc < 0)
        r, c = sr + step_r, sc + step_c
        while (r, c) != (er, ec):
            if self.board[r][c] != '.':
                return False
            r += step_r
            c += step_c
        return True

    def valid_move(self, start, end):
        sr, sc = start
        er, ec = end
        piece = self.board[sr][sc]
        target = self.board[er][ec]
        if piece == '.':
            return False
        # Kan ikke ta egen brikke
        if target != '.' and (piece.isupper() == target.isupper()):
            return False
        dr = er - sr
        dc = ec - sc
        p = piece.lower()
        # bønder
        if p == 'p':
            direction = -1 if piece.isupper() else 1
            start_row = 6 if piece.isupper() else 1
            # ett steg
            if dc == 0 and dr == direction and target == '.':
                return True
            # to steg fra start
            if dc == 0 and dr == 2*direction and sr == start_row and \
               self.board[sr + direction][sc] == '.' and target == '.':
                return True
            # diagonal fangst
            if abs(dc) == 1 and dr == direction and target != '.':
                return True
            return False
        # springer
        if p == 'n':
            return (abs(dr), abs(dc)) in [(2,1),(1,2)]
        # løper
        if p == 'b':
            if abs(dr) == abs(dc):
                return self.is_path_clear(sr, sc, er, ec)
            return False
        # tårn
        if p == 'r':
            if dr == 0 or dc == 0:
                return self.is_path_clear(sr, sc, er, ec)
            return False
        # dronning
        if p == 'q':
            if dr == 0 or dc == 0 or abs(dr)==abs(dc):
                return self.is_path_clear(sr, sc, er, ec)
            return False
        # konge
        if p == 'k':
            return max(abs(dr), abs(dc)) == 1
        return False

    def move_piece(self, start, end):
        if self.valid_move(start, end):
            sr, sc = start
            er, ec = end
            self.board[er][ec] = self.board[sr][sc]
            self.board[sr][sc] = '.'
            # bytt tur
            self.turn = 'black' if self.turn=='white' else 'white'

    def run(self):
        running = True
        while running:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    running = False
                elif ev.type == pygame.MOUSEBUTTONDOWN:
                    sq = self.get_square_under_mouse(ev.pos)
                    if sq:
                        r, c = sq
                        piece = self.board[r][c]
                        # velg egen brikke
                        if not self.selected and piece!='.' and \
                           ((piece.isupper() and self.turn=='white') or (piece.islower() and self.turn=='black')):
                            self.selected = sq
                        # flytt valgt
                        elif self.selected:
                            self.move_piece(self.selected, sq)
                            self.selected = None

            self.draw_board()
            # marker valgt
            if self.selected:
                r, c = self.selected
                surf = pygame.Surface((SQ_SIZE, SQ_SIZE), pygame.SRCALPHA)
                surf.fill(HIGHLIGHT_COLOR)
                self.screen.blit(surf, (c*SQ_SIZE, r*SQ_SIZE))

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    # Bytt til katalogen som inneholder images-mappen
    os.chdir(os.path.dirname(__file__))
    game = ChessGame()
    game.run()