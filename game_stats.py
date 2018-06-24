class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """初始统计信息"""
        self.ai_setting= ai_settings
        self.reset_stats()
        # 游戏启动时处于活动状态
        self.game_active = False

        # 分数
        self.score = 0
        # 最高得分
        self.high_score = 0
        # 等级
        self.level = 1

    def reset_stats(self):
        """统计可能变化的信息"""
        self.ship_left = self.ai_setting.ship_limit