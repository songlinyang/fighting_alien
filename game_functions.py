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
from bullet import Bullet

def check_keydown_event(event,game_setting,screen,ship,bullets):
    #判断用户按下键盘
    if event.type == pygame.KEYDOWN:
        #按下右方向->
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        # 按下左方向<-
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        #按下空格键
        elif event.key == pygame.K_SPACE:
            #按一次，新增新子弹
            new_bullet = Bullet(game_setting,screen,ship)
            bullets.add(new_bullet)





def check_keyup_event(event,ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def check_event(game_setting,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #键盘按下
        check_keydown_event(event,game_setting,screen,ship,bullets)


        #键盘松开
        check_keyup_event(event,ship)


"""
处理绘制
:return
"""
def update_screen(screen,ship,game_setting,bullets):
    # 绘制银河系H234行星轨迹
    screen.fill(game_setting.bg_color)
    # 绘制飞船
    ship.bliteme()


    # bullet.draw_bullet()

    # 绘制飞船的加农炮子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()



    #让绘制显示
    pygame.display.flip()
