import pygame

from sys import exit


pygame.init()
pygame.display.set_caption("Bounce")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 640))


mouse_pos = (0,0)
mouse_press = (0,0,0)


ball = pygame.image.load('assets/ball.png')
ball_rect = ball.get_rect(center = (100, 100))


ground = pygame.image.load('assets/ground.png')
ground_rect = ground.get_rect(center = (400, 600))


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	
	mouse_pos = pygame.mouse.get_pos()
	mouse_press = pygame.mouse.get_pressed(num_buttons = 3)
	mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 8, 8)
	
	# Drag ball
	if mouse_rect.colliderect(ball_rect) == 1:
		while mouse_press[0] == 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
			
			mouse_press = pygame.mouse.get_pressed(num_buttons = 3)
			mouse_pos = pygame.mouse.get_pos()

			ball_rect.x = mouse_pos[0]
			ball_rect.y = mouse_pos[1]
			screen.blit(ball, ball_rect)
			
			pygame.display.update()
			clock.tick(30)
			
	
	# Render
	screen.blit(ball, ball_rect)
	screen.blit(ground, ground_rect)
	
	pygame.display.update()
	clock.tick(30)
