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

bkg = pygame.image.load('assets/bkg.png')
bkg_rect = bkg.get_rect(topleft = (0,0))

time = 0
dx = 0
dy = 0


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
			
			temp_x = mouse_pos[0]
			temp_y = mouse_pos[1]
			
			mouse_press = pygame.mouse.get_pressed(num_buttons = 3)
			mouse_pos = pygame.mouse.get_pos()

			dx = (mouse_pos[0] - temp_x)*0.1
			dy = (mouse_pos[1] - temp_y)*0.1
			
			ball_rect.x = mouse_pos[0]
			ball_rect.y = mouse_pos[1]
			time = 0
			
			# Colisão da bola com o chão
			if ball_rect.colliderect(ground_rect) == 1:
				ball_rect.y = 490
			# Colisão da bola com a parede à direita
			if ball_rect.x > 740:
				ball_rect.x = 740
			
			screen.blit(bkg, bkg_rect)
			screen.blit(ball, ball_rect)
			screen.blit(ground, ground_rect)
			
			pygame.display.update()
			clock.tick(30)
	
	# Física
	if ball_rect.colliderect(ground_rect) == 1:
		time = 0
	else:
		time = time + 0.1
		ball_rect.y = ball_rect.y + dy*time + 4.9*(time**2)
		ball_rect.x = ball_rect.x + dx*time
		
		# O valor tem que ser 491 para ela colidir com o ground
		if ball_rect.y >= 491: ball_rect.y = 491
		if ball_rect.x >= 740: ball_rect.x = 0
		if ball_rect.x < 0: ball_rect.x = 740
	
	# Render
	screen.blit(bkg, bkg_rect)
	screen.blit(ball, ball_rect)
	screen.blit(ground, ground_rect)
	
	pygame.display.update()
	clock.tick(30)
