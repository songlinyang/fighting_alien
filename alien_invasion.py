"""
开始游戏的主逻辑
"""
import sys
import pygame
from setting import Setting
from ship import Ship
from game_functions import check_event,update_screen
from bullet import Bullet
from pygame.sprite import Sprite,Group

def run_game():
    #初始化银河系背景

    #创建setting类
    game_setting = Setting()

    pygame.init()
    screen = pygame.display.set_mode((game_setting.screen_width,game_setting.screen_height))
    pygame.display.set_caption("外星人入侵")

    #创建飞船
    ship = Ship(screen)

    #创建子弹
    bullet = Bullet(game_setting,screen,ship)

    #创建子弹精灵组
    bullets = Group()

    #开始游戏主循环
    while True:

        #监听鼠标键盘输入
        check_event(ship=ship,game_setting=game_setting,screen=screen,bullets=bullets)

        # 飞船切换成自定义飞行模式
        ship.update(speed=game_setting.ship_speed_factor)
        # 子弹的飞行轨迹
        bullets.update()

        #删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            print(len(bullets))


        #每次循环时都重绘屏幕
        update_screen(screen=screen,game_setting=game_setting,ship=ship,bullets=bullets)








run_game()