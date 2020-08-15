import pygame

pygame.init()

size = (800, 600)

gameDisplay = pygame.display.set_mode(size)

pygame.display.set_caption("Vitor")

clock = pygame.time.Clock()

crashed = False

while not crashed:
	
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			crashed = True

		print(event)

	pygame.display.update()

	clock.tick(60)


pygame.quit()
