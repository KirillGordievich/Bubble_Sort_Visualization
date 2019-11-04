import pygame
from random import randint


def create_list(n, x0, xn):
    # create list (x0, x1, ... , xn)
    list = []
    for i in range(n):
        x = randint(x0, xn + 1)
        while x in list:
            x = randint(x0, xn + 1)
        list.append(x)
    return list


def swap(list, i, j):
    # swap two elements in a list
    list[i], list[j] = list[j], list[i]
    return list


def buble_sort(list, i, delay):
    # a single iteration of buble sort
    if list[i - 1] > list[i]:
        list = swap(list, i - 1, i)
        flag = False
    else:
        flag = True
    pygame.time.delay(delay)
    return list, flag


def text(surface, fontFace, size, x, y, text, colour):
    font = pygame.font.Font(fontFace, size)
    text = font.render(text, 1, colour)
    surface.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
