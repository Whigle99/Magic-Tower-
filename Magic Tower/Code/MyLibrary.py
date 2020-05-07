# MyLibrary.py

import sys, time, random, math, pygame
from pygame.locals import *
import os


# prints text using the supplied font
def print_text(screen, font, x, y, text, color=(255, 255, 255), shadow=True):
    if shadow:
        imgText = font.render(text, True, (20, 20, 20))
        screen.blit(imgText, (x - 1, y - 1))
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


# MySprite class extends pygame.sprite.Sprite
class MySprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # extend the base Sprite class
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.direction = 0
        self.velocity = Point(0.0, 0.0)

        # X property

    def _getx(self):
        return self.rect.x

    def _setx(self, value):
        self.rect.x = value

    X = property(_getx, _setx)

    # Y property
    def _gety(self):
        return self.rect.y

    def _sety(self, value):
        self.rect.y = value

    Y = property(_gety, _sety)

    # position property
    def _getpos(self):
        return self.rect.topleft

    def _setpos(self, pos):
        self.rect.topleft = pos

    position = property(_getpos, _setpos)

    def load(self, filename, width, height, columns, alpha=True):
        if alpha:
            self.master_image = pygame.image.load(filename).convert_alpha()
        else:
            self.master_image = pygame.image.load(filename)
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0, 0, width, height)
        self.columns = columns
        # try to auto-calculate total frames
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=50):
        # update animation frame number
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        # build current frame only if it changed
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + \
               "," + str(self.last_frame) + "," + str(self.frame_width) + \
               "," + str(self.frame_height) + "," + str(self.columns) + \
               "," + str(self.rect)


# Point class
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # X property
    def getx(self): return self.__x

    def setx(self, x): self.__x = x

    x = property(getx, setx)

    # Y property
    def gety(self): return self.__y

    def sety(self, y): self.__y = y

    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + \
               ",Y:" + "{:.0f}".format(self.__y) + "}"


def calc_velocity(direction, vel=1.0):
    velocity = Point(0, 0)
    if direction == 3:  # north
        velocity.y = -vel
    elif direction == 2:  # east
        velocity.x = vel
    elif direction == 0:  # south
        velocity.y = vel
    elif direction == 1:  # west
        velocity.x = -vel
    return velocity


def reverse_velocity(direction, vel=32):
    velocity = Point(0, 0)
    if direction == 3:  # north
        velocity.y = vel
    elif direction == 2:  # east
        velocity.x = -vel
    elif direction == 0:  # south
        velocity.y = -vel
    elif direction == 1:  # west
        velocity.x = vel
    return velocity


def collision_detection(x, y, map):
    if map[x][y] in [0, 1, 3, 4]:
        return True
    else:
        return False


def talk_detection(x, y, ineList):
    for ine in ineList:
        if (y, x) == (ine[1], ine[2]) and ine[0] in [61,63,64]:
            return ine[0]
    return 0


def trade_detection(x, y, ineList):
    for ine in ineList:
        if (y, x) == (ine[1], ine[2]) and ine[0] in [62]:
            return ine[0]
    return 0


def battle_detection(x, y, ineList):
    for ine in ineList:
        if (y, x) == (ine[1], ine[2]) and ine[0] > 100:
            return ine[0], y, x
    return 0


def go(x, y, map, level):
    x = int(x / 32)
    y = int(y / 32)
    x, y = y, x
    if map[x][y] == 11:  # go upstairs
        level += 1
    elif map[x][y] == 12:  # go downstairs
        level -= 1
    else:
        pass
    return level


# 1--up 0--down
def new_map_position(level, flag):  # get init pos of the new map
    pos_list = [((11, 2), (11, 2)),
                ((7, 1), (11, 10)),
                ((16, 10), (7, 11)),
                ((7, 10), (16, 10)),
                ((15,10),(7,10))]
    pos = pos_list[level][flag]
    return pos[0] * 32, pos[1] * 32


def game_help():
    os.startfile('../Code/help.txt')


def level_up(player):
    coef = 1
    base = 10
    if player.level < 4:
        if player.exp > base + coef * (player.level - 1):
            player.exp -= base + coef * (player.level - 1)
            player.level += 1
            player.atk += 1
            player.deff += 1
            player.hp += 100
            if player.level == 4:
                base += 10
                coef += 1
                player.speed += 1
    elif player.level < 8:
        if player.exp > base + coef * (player.level - 1):
            player.exp -= base + coef * (player.level - 1)
            player.level += 1
            player.atk += 2
            player.deff += 2
            player.hp += 150
            if player.level % 2 == 0:
                player.speed += 1
            if player.level == 8:
                base += 10
                coef += 1
    else:
        if player.exp > base + coef * (player.level - 1):
            player.exp -= base + coef * (player.level - 1)
            player.level += 1
            player.atk += 3
            player.deff += 3
            player.hp += 200
            player.speed += 1
            base += player.level


def shopping(screen, font, player, merchant, item):
    items = merchant.commodity

    print_text(screen, font, 160, 80,
               items[0][0] + str(items[0][2]) + '    价格:' + str(items[0][1]) + '金币', color=(0, 0, 0))
    print_text(screen, font, 360, 80, '按 1 购买', color=(0, 0, 0))
    print_text(screen, font, 160, 110,
               items[1][0] + str(items[1][2]) + '    价格:' + str(items[1][1]) + '金币', color=(0, 0, 0))
    print_text(screen, font, 360, 110, '按 2 购买', color=(0, 0, 0))
    print_text(screen, font, 160, 140,
               items[2][0] + str(items[2][2]) + '    价格:' + str(items[2][1]) + '金币', color=(0, 0, 0))
    print_text(screen, font, 360, 140, '按 3 购买', color=(0, 0, 0))
    print_text(screen, font, 160, 170,
               items[3][0] + str(items[3][2]) + '    价格:' + str(items[3][1]) + '金币', color=(0, 0, 0))
    print_text(screen, font, 360, 170, '按 3 购买', color=(0, 0, 0))
    print_text(screen, font, 300, 200, '按 0 退出', color=(0, 0, 0))

    if item == 1:
        if player.gold >= items[0][1]:
            player.gold -= items[0][1]
            player.atk += 4
    elif item == 2:
        if player.gold >= items[1][1]:
            player.gold -= items[1][1]
            player.deff += 4
    elif item == 3:
        if player.gold >= items[2][1]:
            player.gold -= items[2][1]
            player.hp += 100

    item = 0
