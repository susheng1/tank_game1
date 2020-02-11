from abc import *
import pygame
from views import *
from locals import *
from pygame.locals import *

class Fragment(metaclass=ABCMeta):
    def __init__(self,surface):
        if isinstance(surface,pygame.Surface):
            self.surface = surface
    @abstractmethod
    def render(self):
        pass
    def key_pressed(self, keys):
        pass

class MapFragment(Fragment):

    def __init__(self, surface):
        super().__init__(surface)

        self.views = []
        self.player = None
        self._load_map()


        # for i in range(8):
        #     self.views.append(Wall(self.surface,120+i*60,300))
        #     self.views.append(Steel(self.surface,120+i*60,420))

    def _load_map(self):
        file = open("map/0.map", "r", encoding="utf-8")

        for row, line in enumerate(file):
            texts = str(line).strip("")
            for column, text in enumerate(texts):
                # print("{} ({}, {})".format(text, row, column))
                x = column * BLOCK
                y = row * BLOCK
                if text == "砖":
                    self.views.append(Wall(self.surface, x, y))
                elif text == "铁":
                    self.views.append(Steel(self.surface, x, y))
                elif text == "我":
                    self.player = PlayerTank(self.surface, x, y)
                    self.views.append(self.player)


    def render(self):
        self.surface.fill((0, 0, 0))

        # 显示
        for view in self.views:
            view.display()
        for view in self.views:
            if isinstance(view, Wall):
                if self.player.is_blocked(view):
                    # print("碰撞了")
                    break

    def key_pressed(self, keys):
        if self.player is not None and isinstance(self.player, PlayerTank):
            if keys[K_UP]:
                self.player.move(Direction.UP)
            if keys[K_DOWN]:
                self.player.move(Direction.DOWN)
            if keys[K_LEFT]:
                self.player.move(Direction.LEFT)
            if keys[K_RIGHT]:
                self.player.move(Direction.RIGHT)

class InfoFragment(Fragment):

    def __init__(self,surface):
        super().__init__(surface)


    def render(self):
        self.surface.fill((0,0xff,0))

