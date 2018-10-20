"""
开始游戏的主逻辑
"""
import sys
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from bullet import Bullet
from pygame.sprite import Group
from alien import Alien

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
    #bullet = Bullet(game_setting,screen,ship)

    #创建子弹精灵组
    bullets = Group()

    #创建外星人精灵组
    aliens = Group()

    #创建外星人
    #alien = Alien(game_setting,screen)

    # 加入外星人群
    gf.create_fleet(game_setting=game_setting, screen=screen, aliens=aliens, ship=ship)
    #开始游戏主循环
    while True:

        #监听鼠标键盘输入
        gf.check_event(ship=ship,game_setting=game_setting,screen=screen,bullets=bullets)
        # 飞船切换成自定义飞行模式
        ship.update(speed=game_setting.ship_speed_factor)
        #更新子弹飞行轨迹
        gf.update_bullets(bullets=bullets)
        #更新外星人的移动轨迹
        gf.update_aliens(game_setting=game_setting,aliens=aliens)
        #每次循环时都重绘屏幕
        gf.update_screen(screen=screen,game_setting=game_setting,ship=ship,bullets=bullets,aliens=aliens)

if __name__ == '__main__':
    run_game()