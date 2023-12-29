import pygame

# Initialize Pygame
pygame.init()

# Define screen size
screen_width, screen_height = 1200, 10

# Create the screen with NOFRAME flag
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)

# Set the window caption (optional)
pygame.display.set_caption("Borderless Black Screen")

# Fill the screen with black color
screen.fill((0, 0, 0))

# Update the display to show the black screen
pygame.display.flip()

# Run the main loop
running = True
while running:
    # Handle events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw additional things here if needed, otherwise the screen stays black

    # Update the display again
    pygame.display.flip()

# Quit Pygame
pygame.quit()
