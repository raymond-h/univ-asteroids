import pygame

pygame.display.init()

screen = pygame.display.set_mode( (640, 480) )
pygame.display.set_caption("Asteroids!!!")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill( (255, 0, 0) )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
