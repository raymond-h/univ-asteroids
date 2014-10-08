import pygame

pygame.display.init()

screen = pygame.display.set_mode( (640, 480) )
pygame.display.set_caption("Asteroids!!!")

done = False
clock = pygame.time.Clock()

def event():
    global done

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # dem bootins

def logic():
    # logic stuff

    None

def render():
    screen.fill( (255, 0, 0) )

    # render code goes here

    pygame.display.flip()

while not done:
    event()
    logic()
    render()

    clock.tick(60)

pygame.quit()
