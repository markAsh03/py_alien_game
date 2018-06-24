class Settings():
    """ 存储所有的设置类"""

    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        """设置背景颜色"""
        self.bg_color = (230, 230, 230)
        """飞船速度"""
        self.ship_speed_factor = 1.5
        # 飞船数量
        self.ship_limit = 3

        """子弹设置"""
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed_factor = 10
        self.bullet_color = 60, 60, 60
        # 子弹数量
        self.bullets_allowed = 30

        """外星人设置"""
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

