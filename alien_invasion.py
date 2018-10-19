"""
开始游戏的主逻辑
"""
import sys
import pygame
from setting import Setting
from ship import Ship
from game_functions import check_event,update_screen

def run_game():
    #初始化银河系背景

    #创建setting类
    game_setting = Setting()

    pygame.init()
    screen = pygame.display.set_mode((game_setting.screen_width,game_setting.screen_height))
    pygame.display.set_caption("外星人入侵")

    #创建飞船
    ship = Ship(screen)

    #开始游戏主循环
    while True:

        #监听鼠标键盘输入
        check_event(ship=ship)

        #每次循环时都重绘屏幕
        update_screen(screen=screen,game_setting=game_setting,ship=ship)








run_game()