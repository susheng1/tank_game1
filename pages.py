from pygame.locals import *
import pygame
from abc import *

from locals import *
from fragment import *
from res import *

"""
当前显示的页面
"""
__current = None


def go(page):
    """进入某个页面"""
    if page is not None and isinstance(page, Page):
        global __current
        __current = page


def render():
    """渲染页面"""
    if __current is not None and isinstance(__current, Page):
        __current.render()


def key_down(key):
    """键盘按下事件"""
    if __current is not None and isinstance(__current, Page):
        __current.key_down(key)


def key_up(key):
    """键盘抬起事件"""
    if __current is not None and isinstance(__current, Page):
        __current.key_up(key)


def key_pressed(keys):
    """键盘长按事件"""
    if __current is not None and isinstance(__current, Page):
        __current.key_pressed(keys)


class Page(metaclass=ABCMeta):
    """
    页面对象，如果要创造新的页面，需要继承我
    需要把Page，做成抽象类，abstract class
    抽象类起到制定规范作用，自己不可实例化，规范的是子类。
    from abc import *
    """

    def __init__(self, surface):
        if isinstance(surface, pygame.Surface):
            self.surface = surface

    @abstractmethod
    def render(self):
        """
        负责渲染页面的，是所有子类必须实现的，定义为抽象方法
        :return:
        """
        pass

    def key_down(self, key):
        """
        键盘按下事件, 非必须，不用定义成抽象方法。
        如果子类想用到键盘按下事件，覆写次方法
        :param key: 按下的键
        :return:
        """
        pass

    def key_up(self, key):
        pass

    def key_pressed(self, keys):
        pass


class HomePage(Page):

    def __init__(self, surface):
        super().__init__(surface)

        self.bg = get_image("img/bg.png")
        self.bg_w = self.bg.get_width()
        self.bg_h = self.bg.get_height()
        self.bg_x = (WINDOW_WIDTH - self.bg_w) / 2
        self.bg_y = (WINDOW_HEIGHT - self.bg_h) / 2 - 50

        # 当前的选项
        self.index = 0
        self.positions = [368, 368 + 64, 368 + 2 * 64, 368 + 3 * 64]
        self.pointer = get_image("img/pointer.png")
        self.p_x = 400
        self.p_y = self.positions[self.index]

    def render(self):
        # 重绘页面
        self.surface.fill((0, 0, 0))
        # 显示背景
        self.surface.blit(self.bg, (self.bg_x, self.bg_y))
        # 显示选择指针
        self.surface.blit(self.pointer, (self.p_x, self.p_y))

    def key_down(self, key):
        if key == K_DOWN:
            # 移动选项
            self.index += 1
            if self.index >= len(self.positions):
                self.index = 0
            self.p_y = self.positions[self.index]
        if key == K_UP:
            self.index -= 1
            if self.index < 0:
                self.index = len(self.positions) - 1
            self.p_y = self.positions[self.index]

    def key_up(self, key):
        if key == K_RETURN:
            # 页面跳转
            if self.index == 0:
                go(GamePage(self.surface))


class GamePage(Page):

    def __init__(self, surface):
        super().__init__(surface)

        # 地图区
        self.map_surface = pygame.Surface(MAP_SIZE)
        self.map = MapFragment(self.map_surface)

        # 信息区
        self.info_surface = pygame.Surface(INFO_SIZE)
        self.info = InfoFragment(self.info_surface)

    def render(self):
        # 刷新页面
        self.surface.fill((0x88, 0x88, 0x88))

        # 显示地图区
        self.surface.blit(self.map_surface, MAP_POS)
        self.map.render()

        # 显示信息区
        self.surface.blit(self.info_surface, INFO_POS)
        self.info.render()

    def key_pressed(self, keys):
        self.map.key_pressed(keys)

