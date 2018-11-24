# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:01:48 2018

@author: lzm
"""
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    """初始化，设置和屏幕对象"""
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    #alien = Alien(ai_settings,screen)
    
    bullets = Group()
    aliens = Group()
    
    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #开始游戏的循环
    while True:
        gf.check_event(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_aliens(ai_settings,aliens)
        gf.update_bullets(aliens,bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()
    
    