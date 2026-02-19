import pygame

print("setup started")
pygame.init()
pygame.init()
window = pygame.display.set_mode((800, 600))
print("setup finished")

print("Loop Started")
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # cLose window
            quit() # end pygame
