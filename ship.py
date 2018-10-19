"""
初始化飞船
"""
import pygame

class Ship():

    def __init__(self,screen):
        """初始化飞船并设置其初始位置"""
        #制定飞船要出现在银河系H234行星轨迹上
        self.screen = screen

        #创建飞船
        self.image = pygame.image.load('images/ship.bmp')
        #获取飞船位置对象
        self.rect = self.image.get_rect()
        #获取背景位置对象
        self.screen_rect = self.screen.get_rect()

        #设置飞船所处的位置(放在屏幕底部中央)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #添加飞船向左、向右属性
        self.moving_left = False
        self.moving_right = False


        #优化rect飞船对象的centerx不能存小数的问题
        self.center = float(self.rect.centerx)





    #绘制飞船
    def bliteme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)


    #控制飞船的动作
    def update(self,speed=1):
        if self.moving_left and self.rect.left > 0:
            self.center -=speed


        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center +=speed

        self.rect.centerx = self.center
