import pygame
import math

pygame.display.init()

screen = pygame.display.set_mode( (640, 480) )
pygame.display.set_caption("Asteroids!!!")

done = False
clock = pygame.time.Clock()

class Ship:
	def __init__(self):
		self.x = 640/2
		self.y = 480/2
		self.angle = 0
	
	def logic(self):
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_LEFT]:
			self.angle = self.angle - 3
	
		if keys[pygame.K_RIGHT]:
			self.angle = self.angle + 3
	
	def make_point(self, x, y):
		r = math.sqrt(x**2 + y**2)
		a = math.atan2(y, x) + math.radians(self.angle)
		
		return (self.x + r * math.cos(a), self.y + r * math.sin(a))
		
	def make_polygon(self):
		list = [
			self.make_point(-20, -10),
			self.make_point(20, 0),
			self.make_point(-20, 10)
		]
		
		return list
	
	def render(self):
		points = self.make_polygon()
		pygame.draw.polygon(screen, (255, 255, 255), points)

class Asteroid:
	def __init__(self, x, y, velx, vely, size):
		self.x = x
		self.y = y
		self.velx = velx
		self.vely = vely
		self.size = size
	
	def logic(self):
		self.x = self.x + self.velx
		self.y = self.y + self.vely
		
	
	def render(self):
		pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.size)
		

ship = Ship()
asteroid = Asteroid(300, 300, 2, 2, 20)

def event():
    global done

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # dem bootins

def logic():
    # logic stuff
    ship.logic()
    asteroid.logic()

    None

def render():
    screen.fill( (255, 0, 0) )

    # render code goes here
    ship.render()
    asteroid.render()
    
    pygame.display.flip()

while not done:
    event()
    logic()
    render()

    clock.tick(60)

pygame.quit()
