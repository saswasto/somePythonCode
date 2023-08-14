import pygame
import random

# Initialize pygame
pygame.init()

# Set the screen size
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the clock
clock = pygame.time.Clock()

# Load the bird image
bird_image = pygame.image.load("bird.png").convert_alpha()

# Set the bird position and velocity
bird_x = SCREEN_WIDTH // 2 - bird_image.get_width() // 2
bird_y = SCREEN_HEIGHT // 2 - bird_image.get_height() // 2
bird_vel = 0

# Load the pipe image
pipe_image = pygame.image.load("pipe.png").convert_alpha()

# Create a list to hold the pipes
pipes = []

# Set the pipe properties
PIPE_WIDTH = 60
PIPE_HEIGHT = 400
PIPE_GAP = 200
pipe_x = SCREEN_WIDTH

# Set the game over flag
game_over = False

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = -10

    # Move the bird
    bird_vel += 1
    bird_y += bird_vel

    # Draw the bird
    screen.blit(bird_image, (bird_x, bird_y))

    # Move the pipes
    for pipe in pipes:
        pipe["x"] -= 5

    # Add a new pipe if necessary
    if len(pipes) == 0 or pipes[-1]["x"] < SCREEN_WIDTH - PIPE_GAP:
        pipe_y = random.randint(PIPE_HEIGHT, SCREEN_HEIGHT - PIPE_HEIGHT)
        pipes.append({"x": SCREEN_WIDTH, "y": pipe_y})

    # Draw the pipes
    for pipe in pipes:
        top_pipe_rect = pygame.Rect(pipe["x"], 0, PIPE_WIDTH, pipe["y"] - PIPE_GAP // 2)
        bottom_pipe_rect = pygame.Rect(pipe["x"], pipe["y"] + PIPE_GAP // 2, PIPE_WIDTH,
                                       SCREEN_HEIGHT - (pipe["y"] + PIPE_GAP // 2))
        pygame.draw.rect(screen, (0, 255, 0), top_pipe_rect)
        pygame.draw.rect(screen, (0, 255, 0), bottom_pipe_rect)
        screen.blit(pipe_image, (pipe["x"], pipe["y"] - PIPE_HEIGHT))
        screen.blit(pipe_image, (pipe["x"], pipe["y"] + PIPE_GAP // 2))

    # Check for collisions
    for pipe in pipes:
        top_pipe_rect = pygame.Rect(pipe["x"], 0, PIPE_WIDTH, pipe["y"] - PIPE_GAP // 2)
        bottom_pipe_rect = pygame.Rect(pipe["x"], pipe["y"] + PIPE_GAP // 2, PIPE_WIDTH,
                                       SCREEN_HEIGHT - (pipe["y"] + PIPE_GAP // 2))
        if top_pipe_rect.colliderect(pygame.Rect(bird_x, bird_y, bird_image.get_width(),
                                                 bird_image.get_height())) or bottom_pipe_rect.colliderect(
                pygame.Rect(bird_x, bird_y, bird_image.get_width(), bird_image.get_height())):
            game_over = True

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()