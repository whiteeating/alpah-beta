# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 13:20:51 2018

@author: lzm
"""

import sys
import pygame
from bullet import Bullet
from alien import Alien
                
    
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """ 响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
        
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    """ 响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_event(ai_settings,screen,ship,bullets):
    """ 响应按键和鼠标事件 """
    # 监听键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,aliens,bullets):
     # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    
    
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    aliens.draw(screen)
     # 让最近绘制的屏幕可见
    pygame.display.flip()
def update_bullets(aliens,bullets):
    #更新子弹的位置
    bullets.update()
    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

def update_aliens(ai_settings,aliens):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    
def fire_bullet(ai_settings,screen,ship,bullets):
    
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship) 
        bullets.add(new_bullet)

# 创建外星人群
def get_aliens_number(ai_settings,alien_width):
    
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
  
    alien.x = alien_width + 2*alien.rect.width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number

    aliens.add(alien)
    
def get_aliens_row(ai_settings,alien_height,ship_height):
    
    available_space_y = ai_settings.screen_height - 3*alien_height -ship_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows
   
def create_fleet(ai_settings,screen,ship,aliens):
    
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_aliens_number(ai_settings,alien.rect.width)
    number_rows = get_aliens_row(ai_settings,alien.rect.height,ship.rect.height)
    print(number_rows)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
            
def check_fleet_edges(ai_settings,aliens):
    """有外星人到达边缘采取相应措施 """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        
    ai_settings.fleet_direction *= -1 


 
    
    
        