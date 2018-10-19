"""
创建外星人对象
"""
import pygame

from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,game_setting,screen):
        super(Alien,self).__init__()
        self.game_setting = game_setting
        self.screen = screen

        #创建外星人
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #设置外星人的位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的y坐标
        self.y = float(self.rect.y)

    def blitme(self):
        #显示出外星人
        self.screen.blit(self.image,self.rect)