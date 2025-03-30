import random
import time
import pygame
import sys
from pygame.locals import *


pygame.init()

# Set frames per second
FPS = 60
FramePerSec = pygame.time.Clock()

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions and game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0

# Fonts for text rendering
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Set up display surface
SCREEN = pygame.display.set_mode((400, 600))
SCREEN.fill(WHITE)
pygame.display.set_caption("Game")

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")  
        self.rect = self.image.get_rect()  # Get rectangle for positioning
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Random starting position

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  
        if self.rect.top > 600:  # Reset position if it moves off-screen (safecheck)
            SCORE += 1  # Increment score
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")  # Load player image
        self.rect = self.image.get_rect()  # Get rectangle for positioning
        self.rect.center = (160, 520)  # Set initial position

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # Get pressed keys
        if self.rect.left > 0:  # Move left if within bounds
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:  # Move right if within bounds
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)

    def collect_coin(self, coins):
        collisions = pygame.sprite.spritecollide(self, coins, True)  
        for coin in collisions:
            return True  # Coin Collected Behavior
        return False

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png") 
        self.rect = self.image.get_rect()  
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Random starting position

    def move(self):
        self.rect.move_ip(0, SPEED)  # Move coin downwards
        if self.rect.top > 600:  # Reset position if it moves off-screen
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Create player, enemy, and coin objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Create sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Event for increasing speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Trigger every second


done = False

# Main game 
while not done:
    for event in pygame.event.get():
        if event.type == INC_SPEED:  # Increase speed event
            SPEED += 0.5
        if event.type == pygame.QUIT:  # Quit event
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # Check for ESC key to exit
            if event.key == pygame.K_ESCAPE:
                done = True

    # Draw background and scores
    SCREEN.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coin_scores = font_small.render(f"Coins: {COIN_SCORE}", True, BLACK)
    SCREEN.blit(scores, (10, 10))
    SCREEN.blit(coin_scores, (300, 10))

    # Update and draw all sprites
    for entity in all_sprites:
        SCREEN.blit(entity.image, entity.rect)
        entity.move()

    # Check for coin collection
    if P1.collect_coin(coins):
        pygame.mixer.Sound("GetCoin.mp3").play()  # Play coin collection sound
        COIN_SCORE += 1  # Increment coin score
        new_coin = Coin()  # Create a new coin
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # Check for collision with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()  
        time.sleep(0.5)  
        SCREEN.fill(RED)  
        SCREEN.blit(game_over, (30, 250))  # Display "Game Over" text
        pygame.display.update()
        for entity in all_sprites:  # Remove all sprites
            entity.kill()
        time.sleep(2)  
        pygame.quit()
        sys.exit()

    # Update display and control frame rate
    pygame.display.update()
    FramePerSec.tick(FPS)
