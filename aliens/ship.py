# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:41:12 2018

@author: lzm
"""

import pygame

class Ship():
    
    def __init__(self,ai_settings,screen):
        
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 将飞船放在底部
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.center = float(self.rect.centerx)
        
        # self.rect.centery = self.sreeen_rect.centery
        
        #移动标志
        self.moving_right = False
        self.moving_left = False
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
        
    def update(self):
        """ 根据标志调整飞船位置 """
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        
    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
         