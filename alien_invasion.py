import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

def run_game():
    # 初始化游戏创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()
    # 设置屏幕宽高
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 用于存储统计信息的实例
    stats = GameStats(ai_settings)
    # 创建飞船
    ship = Ship(ai_settings, screen)
    # 创建记分牌
    sb = ScoreBoard(ai_settings, screen, stats)

    # 创建存储子弹的编组
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    """开始游戏"""
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, stats, screen, ship, aliens, bullets, play_button, sb)

        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)
            gf.update_bullets(ai_settings, stats, screen, ship, aliens, bullets, sb)

        gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button, sb)


run_game()
