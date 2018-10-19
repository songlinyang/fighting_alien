"""
重构主运行方法的主逻辑
"""
import pygame

"""
处理按钮，键盘事件
:return 
"""
import pygame
import sys

def check_keydown(event,ship):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True

def check_keyup(event,ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def check_event(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #键盘按下
        check_keydown(event,ship)


        #键盘松开
        check_keyup(event,ship)


"""
处理绘制
:return
"""
def update_screen(screen,ship,game_setting,bullet):
    # 绘制银河系H234行星轨迹
    screen.fill(game_setting.bg_color)
    # 绘制飞船
    ship.bliteme()

    # 飞船切换成自定义飞行模式
    ship.update(speed=game_setting.ship_speed_factor)

    # 飞船加载加农炮
    bullet.draw_bullet()
    bullet.update()

    # 让绘制显示
    pygame.display.flip()