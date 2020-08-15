import pygame

size = [800, 600]

displaygame = pygame.display.set_mode(size)

pygame.display.set_caption("My game")

close = True

clock = pygame.time.Clock()

while close:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			close = False

	print(event)
	clock.tick(60)
