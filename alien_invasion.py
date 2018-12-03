#coding=utf-8
import sys
import pygame
from ship import Ship
from alien import *
import game_functions as gf
from Settings import *
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	pygame.init()
	ai_setting=Settings()
	screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
	image_bg=pygame.image.load('images/stars3.jpg').convert_alpha()
	pygame.display.set_caption("Alien Invasion")
	play_button=Button(ai_setting,screen,"Play")
	ship=Ship(ai_setting,screen)
	bullets=pygame.sprite.Group()
	aliens=pygame.sprite.LayeredUpdates()
	aliens_bullets=pygame.sprite.Group()#史汉林添加
	gf.create_fleet(ai_setting,screen,ship,aliens)
	stats=GameStats(ai_setting)
	sb=Scoreboard(ai_setting,screen,stats)
	while True:
		gf.check_events(ai_setting,screen,stats,sb,play_button,ship,bullets,aliens)
		if stats.game_active:
			gf.clock_click(ai_setting)
			ship.update()
			gf.update_bullets(ai_setting,screen,stats,sb,ship,bullets,aliens)
			gf.fire_alien_bullet(ai_setting,screen,aliens,aliens_bullets)
			gf.update_alien_bullets(ai_setting,screen,stats,sb,ship,aliens,bullets,aliens_bullets)
			gf.update_aliens(ai_setting,stats,sb,screen,ship,aliens,bullets)
		gf.update_screen(image_bg,ai_setting,screen,stats,sb,ship,bullets,aliens,play_button,aliens_bullets)
run_game()