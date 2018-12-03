#coding=utf-8
import os
class GameStats():
	def __init__(self,ai_settings):
		self.ai_settings=ai_settings
		self.reset_stats()
		self.game_active=False
		self.filename='High_Records.txt'
		self.high_score=self.read_high_score()

	def reset_stats(self):
		self.ships_left=self.ai_settings.ship_limit
		self.score=0
		self.level=1

	def read_high_score(self):
		if os.path.isfile(self.filename):
			file_list=open(self.filename).readlines()
			high_score=float(file_list[0])
			return high_score
