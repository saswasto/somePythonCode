import pygame

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")

# Set up the car
car_image = pygame.image.load("car.png")
car_width = 50
car_height = 100
car_x = (screen_width - car_width) / 2
car_y = screen_height - car_height - 10
car_speed = 5

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < screen_width - car_width:
        car_x += car_speed

    # Draw the car and update the screen
    screen.fill((255, 255, 255))
    screen.blit(car_image, (car_x, car_y))
    pygame.display.update()

# Quit Pygame
pygame.quit()
