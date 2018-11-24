# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:31:48 2018

@author: lzm
"""
class Settings():
    """ 存储《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """ 初始化游戏的设置 """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        #self.bg_color = (135,206,250)
         
        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 4
        
        
        self.aliens_width = 30
        self.aliens_height = 40
        self.aliens_color = (128,0,128)
        self.aliens_speed_factor = 1
        self.fleet_drop_speed = 15
        # 当self.fleet_direction =1 表示向右移动，反之
        self.fleet_direction = 1