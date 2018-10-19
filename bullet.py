"""
创建子弹类
"""
from pygame.sprite import Sprite
import pygame
class Bullet(Sprite):
    def __init__(self,game_setting,screen,ship):
        super().__init__()
        self.screen = screen

        #在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        #确定子弹形状
        self.rect = pygame.Rect(0,0,5,10)
        #确定子弹位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        #定制子弹的颜色
        self.color = (60,60,60)
        #定制子弹的速度
        self.speed_factor = 1

    #绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


    #射击子弹
    def update(self):
        """子弹向上移动"""
        self.y -= self.speed_factor
        self.rect.y = self.y
