class Settings(object):
    """存储外星人入侵的所有设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞机速度设置
        self.ship_speed_factor = 15
        self.ship_limit = 3
        # 子弹速度设置
        self.bullet_speed_factor = 30
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
