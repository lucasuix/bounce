import pygame

# Física para qualquer objeto
def fall(obj, time):
		
		obj.pos.x = obj.pos.x + obj.dx*time
		obj.pos.y = obj.pos.y + obj.dy*time + 4.9*(time**2)
		
		if obj.pos.y >= 491: obj.pos.y = 491
		if obj.pos.x > 740: obj.pos.x = 0
		if obj.pos.x < 0: obj.pos.x = 740

# Drag para qualquer objeto
def drag(obj, mouse_x, mouse_y, delta_x, delta_y):
		
		obj.pos.x = mouse_x
		obj.pos.y = mouse_y
		
		obj.dx = delta_x
		obj.dy = delta_y

class Scene_Obj:
	
	def __init__(self, img, rect):
		
		self.img = img
		self.pos = rect
		
		self.dx = 0
		self.dy = 0

# Carrega os objetos de forma mais prática, o "image" deve ser o nome da imagem do objeto e a classe qual tipo de objeto, xy é a posição inicial
def loadObj(image, classe, xy):
	object_img = pygame.image.load('assets/'+image)
	object_rect = object_img.get_rect(center = xy)
	
	return classe(object_img, object_rect)
