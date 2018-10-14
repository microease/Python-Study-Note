import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主程序"""

    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()

    def __create_sprites(self):
        pass

    def start_game(self):
        print("游戏开始")
        while True:
            # 防止崩溃
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            pass


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
