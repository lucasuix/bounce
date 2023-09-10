import pygame
import bounce
from sys import exit


pygame.init()
pygame.display.set_caption("Bounce")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 640))


mouse_pos = (0,0)
mouse_press = (0,0,0)

ball = bounce.loadObj("ball.png", bounce.Scene_Obj, (100, 100))
ground = bounce.loadObj("ground_novo.png", bounce.Scene_Obj, (400, 600))
bkg = bounce.loadObj("bkg_novo.png", bounce.Scene_Obj, (400, 320))

time = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	mouse_pos = pygame.mouse.get_pos()
	mouse_press = pygame.mouse.get_pressed(num_buttons = 3)
	mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 8, 8)
	
	# Drag ball
	if mouse_rect.colliderect(ball.pos) == 1:
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

			bounce.drag(ball, mouse_pos[0], mouse_pos[1], dx, dy)
			
			time = 0
			
			# Colisão da bola com o chão
			if ball.pos.colliderect(ground.pos) == 1:
				ball.pos.y = 490
			# Colisão da bola com a parede à direita
			if ball.pos.x > 740:
				ball.pos.x = 740
			
			screen.blit(bkg.img, bkg.pos)
			screen.blit(ball.img, ball.pos)
			screen.blit(ground.img, ground.pos)
			
			pygame.display.update()
			clock.tick(30)
	
	# Física
	if ball.pos.colliderect(ground.pos) == 1:
		time = 0
	else:
		time = time + 0.1
		bounce.fall(ball, time)
	
	# Render
	screen.blit(bkg.img, bkg.pos)
	screen.blit(ball.img, ball.pos)
	screen.blit(ground.img, ground.pos)
	
	pygame.display.update()
	clock.tick(30)
