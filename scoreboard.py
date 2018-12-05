#coding=utf-8
import pygame.font
from pygame.sprite import Group

from ship import *

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # Font settings for scoring information.
        self.text_color = (130, 30, 130)
        self.font = pygame.font.Font("arial.ttf",23)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        text_score=u'得分:'
        self.text_score_obj=self.font.render(text_score, True, self.text_color)
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top
        
        self.text_score_rect = self.text_score_obj.get_rect()
        self.text_score_rect.right = self.screen_rect.right - 110
        self.text_score_rect.top = self.screen_rect.top

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        text_high_score=u'最高分:'
        self.text_high_score_obj=self.font.render(text_high_score, True,
            self.text_color)

        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)

        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color)
                
        # Center the high score at the top of the screen.
        self.text_high_score_rect=self.text_high_score_obj.get_rect()
        self.text_high_score_rect.centerx = self.screen_rect.centerx-70
        self.text_high_score_rect.top = self.score_rect.top
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True,
                self.text_color)
        
        text_level=u'难度等级:'
        self.text_level_obj=self.font.render(text_level, True, self.text_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 7
        
        self.text_level_rect = self.text_level_obj.get_rect()
        self.text_level_rect.right = self.score_rect.right-50
        self.text_level_rect.top = self.score_rect.bottom + 7
    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ships_left(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.text_score_obj,self.text_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.text_high_score_obj, self.text_high_score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.text_level_obj, self.text_level_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships.
        self.ships.draw(self.screen)

    def save_records(self):
        filename='High_Records.txt'
        with open(filename,'w') as file_object:
            file_object.write(str(round(self.stats.high_score, -1)))
