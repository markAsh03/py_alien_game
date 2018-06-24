class Settings():
    """ 存储所有的设置类"""

    def __init__(self):
        """初始化游戏静态设置"""
        self.screen_width = 1200
        self.screen_height = 800
        """设置背景颜色"""
        self.bg_color = (230, 230, 230)

        # 飞船数量
        self.ship_limit = 3

        """子弹设置"""
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 子弹数量
        self.bullets_allowed = 30

        """外星人设置"""
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1

        # 外星人点数的提高倍数
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化动态参数设置"""
        self.alien_speed_factor = 1
        """飞船速度"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        # 向右 向左
        self.fleet_direction = 1
        # 积分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)