import pygame
from res import *
from action import *
import time


class Wall(Display):
    def __init__(self, surface, x, y):
        super().__init__(surface)

        self.img = get_image("img/walls.gif")
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = x
        self.y = y

    def display(self):
        self.surface.blit(self.img, (self.x, self.y))


class Steel(Display):
    def __init__(self, surface, x, y):
        super().__init__(surface)
        self.img = get_image("img/steels.gif")
        self.x = x
        self.y = y

    def display(self):
        self.surface.blit(self.img, (self.x, self.y))


class PlayerTank(Display):
    def __init__(self, surface, x, y):
        super().__init__(surface)
        # 坦克的方向
        self.direction = Direction.UP
        # 图片
        self.images = [
            get_image("img/p1tankU.gif"),
            get_image("img/p1tankD.gif"),
            get_image("img/p1tankL.gif"),
            get_image("img/p1tankR.gif")
        ]
        self.width = self.images[0].get_width()
        self.height = self.images[0].get_height()
        self.x = x
        self.y = y
        self.speed = 4

        self.bad_direction = Direction.NONE

        self.__move_time = 0
        self.__move_delay = 0

    def display(self):

        img = self.images[0]
        if self.direction == Direction.UP:
            img = self.images[0]
        elif self.direction == Direction.DOWN:
            img = self.images[1]
        elif self.direction == Direction.LEFT:
            img = self.images[2]
        elif self.direction == Direction.RIGHT:
            img = self.images[3]

        self.surface.blit(img, (self.x, self.y))

    def move(self, direction):
        # 当前准备去的方向和不能去的方向一致
        if direction == self.bad_direction:
            print("不可以走")
            return

        now = time.time()
        if now - self.__move_time < self.__move_delay:
            return
        self.__move_time = now

        if self.direction != direction:
            # 转向
            self.direction = direction
        else:
            if self.direction == Direction.UP:
                self.y -= self.speed
            elif self.direction == Direction.DOWN:
                self.y += self.speed
            elif self.direction == Direction.LEFT:
                self.x -= self.speed
            elif self.direction == Direction.RIGHT:
                self.x += self.speed

    def is_blocked(self, wall):
        # 需要判断的是下一次会不会碰撞，
        # 而不是碰上了，再去确定
        next_x = self.x
        next_y = self.y

        if self.direction == Direction.UP:
            next_y -= self.speed
        elif self.direction == Direction.DOWN:
            next_y += self.speed
        elif self.direction == Direction.LEFT:
            next_x -= self.speed
        elif self.direction == Direction.RIGHT:
            next_x += self.speed

        player_rect = pygame.Rect(next_x, next_y, self.width, self.height)
        wall_rect = pygame.Rect(wall.x, wall.y, wall.width, wall.height)
        collide = pygame.Rect.colliderect(player_rect, wall_rect)
        if collide:
            self.bad_direction = self.direction
        else:
            self.bad_direction = Direction.NONE
        return collide