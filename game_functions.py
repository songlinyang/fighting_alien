"""
重构主运行方法的主逻辑
"""
from setting import Setting
from alien import Alien
from pygame.sprite import Group
"""
处理按钮，键盘事件
:return 
"""
import pygame
import sys
from bullet import Bullet

def check_keydown_event(event,game_setting:Setting,screen,ship,bullets):
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
            fire_bullet(bullets,game_setting,screen,ship)
        elif event.key == pygame.K_q:
            sys.exit()


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
def update_screen(screen,ship,game_setting,bullets,aliens:Group):
    # 绘制银河系H234行星轨迹
    screen.fill(game_setting.bg_color)
    # 绘制飞船
    ship.blitme()
    # 绘制一个外星人
    aliens.draw(screen)

    # 绘制飞船的加农炮子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #让绘制显示
    pygame.display.flip()

"""
创建一群外星人
"""
def create_fleet(game_setting:Setting,screen,aliens):
    alien = Alien(game_setting,screen)
    alien_width = alien.rect.width
    alien_number = get_number_aliens(game_setting,alien_width)

    for alien_number in range(alien_number):
        create_alien(game_setting,screen,alien_number,aliens)

"""
计算出外星人个数
:return 外星人个数
"""
def get_number_aliens(game_setting,alien_width):
    # 计算出可用的空间，来计算出一行可以放多少外星人
    usable_space = game_setting.screen_width - (alien_width * 2)
    alien_number = int(usable_space / (alien_width * 2))
    return alien_number


def create_alien(game_setting,screen,alien_number,aliens):
    alien = Alien(game_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


"""
更新处理子弹移动轨迹
:return
"""
def update_bullets(bullets):
    # 子弹的飞行轨迹
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))

"""
填充子弹，射击
:return
"""
def fire_bullet(bullets,game_setting,screen,ship):
    if len(bullets) < game_setting.bullets_allowed:
        # 按一次，新增新子弹
        new_bullet = Bullet(game_setting, screen, ship)
        bullets.add(new_bullet)