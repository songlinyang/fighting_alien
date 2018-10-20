"""
创建外星人对象
"""
import pygame
from setting import Setting
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,game_setting:Setting,screen):
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

    #更新外星人的位置
    def update(self):
        """向右移动外星人"""
        self.x = float(self.rect.x)
        self.x += (self.game_setting.alien_speed_factor*self.game_setting.fleet_direction)
        self.rect.x = int(self.x)

    #检查外星人驾驶的飞船是否碰到边缘
    def check_edges(self):
        """如果外星人位于屏幕边缘，就放回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
