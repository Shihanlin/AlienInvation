#coding=utf-8
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		super(Ship,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		self.image=pygame.image.load('images/ship.png')
		#self.image_scale=pygame.transform.scale(self.image,(40,40))
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.centerx=self.screen_rect.centerx
		# self.rect.centery=self.screen_rect.centery #test
		self.rect.bottom=self.screen_rect.bottom
		self.center=float(self.rect.centerx)
		self.moving_right=False
		self.moving_left=False
		self.x=float(self.rect.x)
		self.y=float(self.rect.y)
		self.width=self.image.get_width()
		self.height=self.image.get_height()

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def update(self):
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
			self.x += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			self.center -= self.ai_settings.ship_speed_factor
			self.x -= self.ai_settings.ship_speed_factor
		self.rect.centerx=self.center

	def center_ship(self):
		self.center=self.screen_rect.centerx


class Ships_left(Sprite):
	"""docstring for Ships_left"""
	def __init__(self,ai_settings,screen):
		super(Ships_left, self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		self.image=pygame.image.load('images/ship_icon.bmp')
		self.rect=self.image.get_rect()


		

