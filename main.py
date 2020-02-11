import pygame
from pygame.locals import *
import sys

from pages import *
from res import *

import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

if __name__ == '__main__':
    # 初始化
    pygame.init()

    window = pygame.display.set_mode(REAL_SIZE)
    pygame.display.set_caption(APP_NAME)
    pygame.display.set_icon(get_image("img/logo.png"))

    fps = 0

    surface = pygame.Surface(WINDOW_SIZE)

    go(GamePage(surface))

    while True:
        start = time.time()

        scale = pygame.transform.scale(surface, REAL_SIZE)
        window.blit(scale, (0, 0))
        render()

        pygame.display.flip()

        events = pygame.event.get()
        for event in events:
            # 窗体关闭事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                key_down(event.key)
            if event.type == KEYUP:
                key_up(event.key)

        keys = pygame.key.get_pressed()
        key_pressed(keys)

        end = time.time()

        cost = end - start

        if cost < DEFAULT_DELAY:
            sleep = DEFAULT_DELAY - cost
        else:
            sleep = 0
        time.sleep(sleep)

        end = time.time()
        fps = 1.0 / (end - start)




