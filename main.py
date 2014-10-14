import pygame
import math
import random

pygame.display.init()
pygame.font.init()

screen = pygame.display.set_mode( (640, 480) )
pygame.display.set_caption("Asteroids!!!")

done = False
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 20)

asteroids = []
bullets = []

class Bullet:
	def __init__(self, x, y, angle):
		self.x = x
		self.y = y
		self.angle = angle
		self.vel = 2
	
	def logic(self):
		a = math.radians(self.angle)
		self.x = self.x + self.vel * math.cos(a)
		self.y = self.y + self.vel * math.sin(a)
	
	def render(self):
		rect = (self.x - 3, self.y - 3, 6, 6)
		pygame.draw.rect(screen, (0, 255, 0), rect)

class Ship:
	def __init__(self):
		self.x = 640/2
		self.y = 480/2
		self.angle = 0
		self.radius = 10
		self.has_shot = False
		self.alive = True
	
	def logic(self):
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_LEFT]:
			self.angle = self.angle - 3
	
		if keys[pygame.K_RIGHT]:
			self.angle = self.angle + 3
		
		if keys[pygame.K_SPACE] and not self.has_shot:
			bullets.append( Bullet(self.x, self.y, self.angle) )
			
		self.has_shot = keys[pygame.K_SPACE]
	
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
		
		if self.x < -self.size:
			self.x = self.x + 640 + 2 * self.size
		
		if self.x > 640 + self.size:
			self.x = self.x - 640 - 2 * self.size
		
		if self.y < -self.size:
			self.y = self.y + 480 + 2 * self.size
		
		if self.y > 480 + self.size:
			self.y = self.y - 480 - 2 * self.size
	
	def render(self):
		pygame.draw.circle(screen, (127, 127, 127), (int(self.x), int(self.y)), self.size)

def random_pos():
	while True:
		x = random.randint(0, 640)
		y = random.randint(0, 480)
		
		if not ((100 < x < 540) or (80 < y < 400)):
			break
	
	return x, y

def random_vel():
	a = math.radians(random.randint(0, 360))
	r = 1.5
	
	return (r * math.cos(a)), (r * math.sin(a))

def random_size():
	return random.randint(16, 24)

def check_collision_ship_asteroid(ship, asteroid):
	r = ship.radius + asteroid.size
	d = math.sqrt((asteroid.x - ship.x)**2 + (asteroid.y - ship.y)**2)
	
	return d < r

def check_collision_bullet_asteroid(bullet, asteroid):
	r = 3 + asteroid.size
	d = math.sqrt((asteroid.x - bullet.x)**2 + (asteroid.y - bullet.y)**2)
	
	return d < r

ship = Ship()

for i in range(6):
	x, y = random_pos()
	velx, vely = random_vel()
	size = random_size()
	asteroids.append(Asteroid(x, y, velx, vely, size))

def event():
	global done

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		# dem bootins

def logic():
	# logic stuff
	if ship.alive:
		ship.logic()
		for asteroid in asteroids:
			asteroid.logic()
		
		removed_bullets = []
		for bullet in bullets:
			bullet.logic()
			
			if bullet.x < 0 or bullet.x > 640 or bullet.y < 0 or bullet.y > 480:
				removed_bullets.append(bullet)
		
		removed_asteroids = []
		for asteroid in asteroids:
			if check_collision_ship_asteroid(ship, asteroid):
				print 'DEAD!!!'
				ship.alive = False
			
			for bullet in bullets:
				if check_collision_bullet_asteroid(bullet, asteroid):
					removed_asteroids.append(asteroid)
					removed_bullets.append(bullet)
					
					if asteroid.size > 8:
						x = asteroid.x
						y = asteroid.y
						
						n = 2
						size = int(asteroid.size / n)
						for _ in range(n):
							velx, vely = random_vel()
							asteroids.append(Asteroid(x, y, velx, vely, size))
		 
		for asteroid in removed_asteroids:
			asteroids.remove(asteroid)
		
		for bullet in removed_bullets:
			bullets.remove(bullet)
	
	else:
		# game over
		None

def render():
	if ship.alive:
		screen.fill((0, 0, 0))
	
		# render code goes here
		ship.render()
		for asteroid in asteroids:
			asteroid.render() 
			
		for bullet in bullets:
			bullet.render()
	
	else:
		# game over; draw game over screen
		screen.fill( (255, 0, 0) )
		
		gameOverText = font.render("You are dead! no big surprise", False, (0,0,0))
		screen.blit(gameOverText, (320 - gameOverText.get_width()/2, 240 - gameOverText.get_height()/2))
			
	pygame.display.flip()	

while not done:
	event()
	logic()
	render()

	clock.tick(60)

pygame.quit()
