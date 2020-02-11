import pygame

"""
图片缓存，dict，字典
key：图片路径
value：pygame.Surface
"""
__images = {}

def get_image(path):
    if path in __images.keys():
        print('使用缓存')
        return __images[path]

    img = pygame.image.load(path)

    # 存储到缓存中
    __images[path] = img
    return img