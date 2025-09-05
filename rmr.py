import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen setup
CELL_SIZE = 40
ROWS, COLS = 15, 20
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Maze Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Directions (dx, dy, key)
DIRS = {
    "N": (0, -1, [pygame.K_UP, pygame.K_w]),
    "S": (0, 1, [pygame.K_DOWN, pygame.K_s]),
    "E": (1, 0, [pygame.K_RIGHT, pygame.K_d]),
    "W": (-1, 0, [pygame.K_LEFT, pygame.K_a]),
}

def generate_maze(rows, cols):
    maze = [[{"N": True, "S": True, "E": True, "W": True} for _ in range(cols)] for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]

    def visit(r, c):
        visited[r][c] = True
        directions = list(DIRS.keys())
        random.shuffle(directions)

        for d in directions:
            dx, dy, _ = DIRS[d]
            nr, nc = r + dy, c + dx
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                maze[r][c][d] = False
                opposite = {"N": "S", "S": "N", "E": "W", "W": "E"}
                maze[nr][nc][opposite[d]] = False
                visit(nr, nc)

    visit(0, 0)
    return maze

def draw_maze(maze):
    for r in range(ROWS):
        for c in range(COLS):
            x, y = c * CELL_SIZE, r * CELL_SIZE
            cell = maze[r][c]
            if cell["N"]:
                pygame.draw.line(screen, WHITE, (x, y), (x + CELL_SIZE, y), 2)
            if cell["S"]:
                pygame.draw.line(screen, WHITE, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 2)
            if cell["E"]:
                pygame.draw.line(screen, WHITE, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)
            if cell["W"]:
                pygame.draw.line(screen, WHITE, (x, y), (x, y + CELL_SIZE), 2)

class Player:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.size = CELL_SIZE - 10
        self.speed = 4
        self.x = col * CELL_SIZE + 5
        self.y = row * CELL_SIZE + 5
        self.target_x = self.x
        self.target_y = self.y
        self.moving = False

    def handle_input(self, keys, maze):
        if not self.moving:  # only start a new move if not already moving
            for d, (dx, dy, key_list) in DIRS.items():
                if any(keys[k] for k in key_list):
                    if not maze[self.row][self.col][d]:  # check wall
                        self.row += dy
                        self.col += dx
                        self.target_x = self.col * CELL_SIZE + 5
                        self.target_y = self.row * CELL_SIZE + 5
                        self.moving = True
                        break

    def update(self):
        if self.moving:
            if self.x < self.target_x:
                self.x = min(self.x + self.speed, self.target_x)
            if self.x > self.target_x:
                self.x = max(self.x - self.speed, self.target_x)
            if self.y < self.target_y:
                self.y = min(self.y + self.speed, self.target_y)
            if self.y > self.target_y:
                self.y = max(self.y - self.speed, self.target_y)

            if self.x == self.target_x and self.y == self.target_y:
                self.moving = False  # arrived at target

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.size, self.size))

def game_loop():
    maze = generate_maze(ROWS, COLS)
    player = Player(0, 0)
    start_time = time.time()
    end_row, end_col = ROWS - 1, COLS - 1

    clock = pygame.time.Clock()
    running = True
    win = False
    time_taken = 0

    while running:
        screen.fill(BLACK)
        draw_maze(maze)

        # Draw start & end
        pygame.draw.rect(screen, BLUE, (5, 5, CELL_SIZE - 10, CELL_SIZE - 10))
        pygame.draw.rect(screen, RED, (end_col * CELL_SIZE + 5, end_row * CELL_SIZE + 5, CELL_SIZE - 10, CELL_SIZE - 10))

        keys = pygame.key.get_pressed()
        if not win:
            player.handle_input(keys, maze)
        player.update()
        player.draw()

        # Check win
        if player.row == end_row and player.col == end_col and not win:
            win = True
            time_taken = round(time.time() - start_time, 2)

        # Win screen
        # if win:
        #     font = pygame.font.SysFont(None, 60)
        #     text = font.render(f"You cleared it! Time: {time_taken}s", True, (255, 255, 0))
        #     screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 30))

        if win:
            font_big = pygame.font.SysFont(None, 60)
            font_small = pygame.font.SysFont(None, 40)

            text1 = font_big.render("You cleared it!", True, (255, 255, 0))
            text2 = font_small.render(f"Time: {time_taken}s", True, (255, 255, 0))

            # Calculate total box size
            box_width = max(text1.get_width(), text2.get_width()) + 40
            box_height = text1.get_height() + text2.get_height() + 30
            box_x = WIDTH // 2 - box_width // 2
            box_y = HEIGHT // 2 - box_height // 2

            # Draw semi-transparent background
            overlay = pygame.Surface((box_width, box_height))
            overlay.set_alpha(180)  # transparency (0-255)
            overlay.fill((0, 0, 0))  # black box
            screen.blit(overlay, (box_x, box_y))

            # Draw texts centered inside the box
            screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, box_y + 10))
            screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, box_y + text1.get_height() + 15))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Restart with Ctrl+R
                if event.key == pygame.K_r and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
                    return True  # restart

        pygame.display.flip()
        clock.tick(60)

    return False

# Main loop with restart
restart = True
while restart:
    restart = game_loop()

pygame.quit()
