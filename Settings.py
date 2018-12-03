#coding=utf-8
import pygame

class Settings():
	def __init__(self):
		'''for the bg'''
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(0,0,0)
		self.bg_music_file=r'Muisc/Escala-Escala-Palladio-128.mp3'

		'''for the ship'''
		self.ship_limit=3
		self.ship_boom_file=r'Muisc/Ship_Boom.wav'
		'''for the bullet'''
		self.bullet_width=3
		self.bullet_height=11
		self.bullet_color=243,81,12
		self.bullets_allowed=20

		'''for the aliens'''
		self.fleet_drop_speed=12
		self.alien_bullet_width=10
		self.alien_bullet_height=5
		self.alien_bullet_color=111,254,106
		self.alien_bullets_allowed=10
		self.alien_boom_file=r'Muisc/Aliens_Boom.wav'

		self.speedup_scale=1.2
		self.score_scale=1.5
		self.ticks=0
		self.frequency=20
		self.frame_rate=100

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed_factor=2.5
		self.bullet_speed_factor=4
		self.bullet_alien_factor=2
		self.alien_speed_factor=2
		self.fleet_direction=1
		self.alien_points=5
		self.high_score=0
		
	def increase_speed(self):
		self.ship_speed_factor *=self.speedup_scale
		self.bullet_alien_factor *=self.speedup_scale
		self.bullet_speed_factor *=self.speedup_scale
		self.alien_speed_factor *=self.speedup_scale
		self.frequency*=0.8
		self.alien_points=int(self.alien_points*self.score_scale)

