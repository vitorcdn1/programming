import pygame

pygame.init()

size = (800,800)

display_game = pygame.display.set_mode(size)

pygame.display.set_caption("Vitor")

close = True
while close:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			close = False


	print(event)

		

	
