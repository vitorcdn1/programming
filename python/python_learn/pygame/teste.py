import pygame

pygame.init()

size = [800,800]
screen = pygame.display.set_mode(size)

opn = True

while opn:
	
	for event in pygame.event.get():
		print(event)
		
		if event == pygame.QUIT:
			opn = False

	
