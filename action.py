from abc import *
import pygame
from enum import Enum

class Direction(Enum):
    NONE = -1
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Display:

    def __init__(self,surface):
        if isinstance(surface,pygame.Surface):
            self.surface = surface

    @abstractmethod
    def display(self):
        pass