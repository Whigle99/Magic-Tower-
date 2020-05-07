# LoadImage.py

import pygame
from pygame.locals import *
from MyLibrary import MySprite

# create sprite groups

# player_status
icon_group = pygame.sprite.Group()
dialog_group = pygame.sprite.Group()
battle_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
trade_group = pygame.sprite.Group()
# scenery
wall_group = pygame.sprite.Group()
ground_group = pygame.sprite.Group()
starrySky_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
upstairs_group = pygame.sprite.Group()
downstairs_group = pygame.sprite.Group()

# items: doors and keys
redDoor_group = pygame.sprite.Group()
blueDoor_group = pygame.sprite.Group()
yellowDoor_group = pygame.sprite.Group()
redKey_group = pygame.sprite.Group()
blueKey_group = pygame.sprite.Group()
yellowKey_group = pygame.sprite.Group()

# items: medicament and gems
redBlood_group = pygame.sprite.Group()
blueBlood_group = pygame.sprite.Group()
redGem_group = pygame.sprite.Group()
blueGem_group = pygame.sprite.Group()
greenGem_group = pygame.sprite.Group()
aSword_group = pygame.sprite.Group()
aShield_group = pygame.sprite.Group()

# npc
fairy_group = pygame.sprite.Group()
merchant01_group = pygame.sprite.Group()
thief_group = pygame.sprite.Group()
wise_group = pygame.sprite.Group()

# enemies
gSlime_group = pygame.sprite.Group()
rSlime_group = pygame.sprite.Group()
lBat_group = pygame.sprite.Group()
skSoldier_group = pygame.sprite.Group()
bSlime_group = pygame.sprite.Group()
bMagician_group = pygame.sprite.Group()
skCaptain_group = pygame.sprite.Group()
bBat_group = pygame.sprite.Group()
orc_group = pygame.sprite.Group()
lGuard_group = pygame.sprite.Group()
rBat_group = pygame.sprite.Group()
skElite_group = pygame.sprite.Group()

# icon
icon = MySprite()
icon.load('../Graphics/Scenery/player01icon.png', 32, 32, 1, False)
icon.position = 40, 40
icon_group.add(icon)


def load_scenery(i, ni, nj):
    if i == 0:
        star = MySprite()
        star.load('../Graphics/Scenery/starry sky.png', 32, 32, 4)
        star.position = ni * 32, nj * 32
        starrySky_group.add(star)
    elif i == 1:
        wall = MySprite()
        wall.load('../Graphics/Scenery/wall.png', 32, 32, 1)
        wall.position = ni * 32, nj * 32
        wall_group.add(wall)
    elif i == 2:
        ground = MySprite()
        ground.load('../Graphics/Scenery/ground.png', 32, 32, 1)
        ground.position = ni * 32, nj * 32
        ground_group.add(ground)
    elif i == 3:
        lava = MySprite()
        lava.load('../Graphics/Scenery/lava.png', 32, 32, 4)
        lava.position = ni * 32, nj * 32
        lava_group.add(lava)
    elif i == 4:
        block = MySprite()
        block.load('../Graphics/Scenery/block.png', 32, 32, 1)
        block.position = ni * 32, nj * 32
        block_group.add(block)
    elif i == 11:
        up = MySprite()
        up.load('../Graphics/Scenery/upstairs.png', 32, 32, 1)
        up.position = ni * 32, nj * 32
        upstairs_group.add(up)
    elif i == 12:
        down = MySprite()
        down.load('../Graphics/Scenery/downstairs.png', 32, 32, 1)
        down.position = ni * 32, nj * 32
        downstairs_group.add(down)


def load_basic(player):
    player.load('../Graphics/Character/hero01.png', 32, 32, 4)
    player.position = 11 * 32, 32 * 11
    player.direction = 0
    player_group.add(player)
    # dialog box
    dialog_box = MySprite()
    dialog_box.load('../Graphics/Scenery/dialog box.png', 224, 72, 1)
    dialog_box.position = 150, 150
    # battle background
    battle_bg = MySprite()
    battle_bg.load('../Graphics/Animations/bg2.JPG', 448, 280, 1, alpha=False)
    battle_bg.position = 152, 64
    # trade background
    trade_bg = MySprite()
    trade_bg.load('../Graphics/Animations/trade.jpg', 300, 168, 1)
    trade_bg.position = 152, 64

    return player, dialog_box, battle_bg, trade_bg


def load_items(i, ni, nj):
    if i == 41:
        rHP = MySprite()
        rHP.load('../Graphics/Items/红血瓶.png', 32, 32, 1)
        rHP.position = ni * 32, nj * 32
        redBlood_group.add(rHP)
    elif i == 42:
        bHP = MySprite()
        bHP.load('../Graphics/Items/蓝血瓶.png', 32, 32, 1)
        bHP.position = ni * 32, nj * 32
        blueBlood_group.add(bHP)
    elif i == 45:
        rGem = MySprite()
        rGem.load('../Graphics/Items/红宝石.png', 32, 32, 1)
        rGem.position = ni * 32, nj * 32
        redGem_group.add(rGem)
    elif i == 46:
        bGem = MySprite()
        bGem.load('../Graphics/Items/蓝宝石.png', 32, 32, 1)
        bGem.position = ni * 32, nj * 32
        blueGem_group.add(bGem)
    elif i == 47:
        gGem = MySprite()
        gGem.load('../Graphics/Items/绿宝石.png', 32, 32, 1)
        gGem.position = ni * 32, nj * 32
        greenGem_group.add(gGem)
    elif i == 91:
        aSword = MySprite()
        aSword.load('../Graphics/Items/Equipment/sword01.png', 32, 32, 1)
        aSword.position = ni * 32, nj * 32
        aSword_group.add(aSword)
    elif i == 92:
        aShield = MySprite()
        aShield.load('../Graphics/Items/Equipment/shield01.png', 32, 32, 1)
        aShield.position = ni * 32, nj * 32
        aShield_group.add(aShield)


def load_npc(i, ni, nj):
    if i == 61:
        fairy = MySprite()
        fairy.load('../Graphics/Character/fairy.png', 32, 32, 4)
        fairy.position = ni * 32, nj * 32
        fairy_group.add(fairy)
    elif i == 62:
        merchant01 = MySprite()
        merchant01.load('../Graphics/Character/merchant01.png', 32, 32, 4)
        merchant01.position = ni * 32, nj * 32
        merchant01_group.add(merchant01)
    elif i == 63:
        thief = MySprite()
        thief.load('../Graphics/Character/thief.png', 32, 32, 4)
        thief.position = ni * 32, nj * 32
        thief_group.add(thief)
    elif i == 64:
        wise = MySprite()
        wise.load('../Graphics/Character/wise.png', 32, 32, 4)
        wise.position = ni * 32, nj * 32
        wise_group.add(wise)


def load_enemies(i, ni, nj):
    if i == 101:
        gSlime = MySprite()
        gSlime.load('../Graphics/Character/Green Slime.png', 32, 32, 4)
        gSlime.position = ni * 32, nj * 32
        gSlime_group.add(gSlime)
    elif i == 102:
        rSlime = MySprite()
        rSlime.load('../Graphics/Character/Red Slime.png', 32, 32, 4)
        rSlime.position = ni * 32, nj * 32
        rSlime_group.add(rSlime)
    elif i == 103:
        lBat = MySprite()
        lBat.load('../Graphics/Character/Little Bat.png', 32, 32, 4)
        lBat.position = ni * 32, nj * 32
        lBat_group.add(lBat)
    elif i == 104:
        skSoldier = MySprite()
        skSoldier.load('../Graphics/Character/Skeleton Soldier.png', 32, 32, 4)
        skSoldier.position = ni * 32, nj * 32
        skSoldier_group.add(skSoldier)
    elif i == 105:
        bSlime = MySprite()
        bSlime.load('../Graphics/Character/Big Slime.png', 32, 32, 4)
        bSlime.position = ni * 32, nj * 32
        bSlime_group.add(bSlime)
    elif i == 106:
        bMagician = MySprite()
        bMagician.load('../Graphics/Character/Blue Magician.png', 32, 32, 4)
        bMagician.position = ni * 32, nj * 32
        bMagician_group.add(bMagician)
    elif i == 107:
        skCaptain = MySprite()
        skCaptain.load('../Graphics/Character/Skeleton Captain.png', 32, 32, 4)
        skCaptain.position = ni * 32, nj * 32
        skCaptain_group.add(skCaptain)
    elif i == 108:
        bBat = MySprite()
        bBat.load('../Graphics/Character/Big Bat.png', 32, 32, 4)
        bBat.position = ni * 32, nj * 32
        bBat_group.add(bBat)
    elif i == 109:
        orc = MySprite()
        orc.load('../Graphics/Character/Orc.png', 32, 32, 4)
        orc.position = ni * 32, nj * 32
        orc_group.add(orc)
    elif i == 110:
        lGuard = MySprite()
        lGuard.load('../Graphics/Character/Low Guard.png', 32, 32, 4)
        lGuard.position = ni * 32, nj * 32
        lGuard_group.add(lGuard)
    elif i == 111:
        rBat = MySprite()
        rBat.load('../Graphics/Character/Red Bat.png', 32, 32, 4)
        rBat.position = ni * 32, nj * 32
        rBat_group.add(rBat)
    elif i == 112:
        skElite = MySprite()
        skElite.load('../Graphics/Character/Skeleton Elite.png', 32, 32, 4)
        skElite.position = ni * 32, nj * 32
        skElite_group.add(skElite)


def load_map(graph):
    nj = -1
    for j in graph:
        ni = -1
        nj += 1
        for i in j:
            ni += 1
            load_scenery(i, ni, nj)


def load_ine(level, ineList):
    for ine in ineList:
        i, ni, nj = ine[0], ine[1], ine[2]
        load_items(i, ni, nj)
        load_npc(i, ni, nj)
        load_enemies(i, ni, nj)


# update groups
def groups_update(ticks):
    delay = 120
    starrySky_group.update(ticks, delay)
    wall_group.update(ticks, delay)
    ground_group.update(ticks, delay)
    lava_group.update(ticks, delay)
    block_group.update(ticks, delay)
    upstairs_group.update(ticks, delay)
    downstairs_group.update(ticks, delay)

    redBlood_group.update(ticks, delay)
    blueBlood_group.update(ticks, delay)
    redGem_group.update(ticks, delay)
    blueGem_group.update(ticks, delay)
    greenGem_group.update(ticks, delay)
    aSword_group.update(ticks, delay)
    aShield_group.update(ticks, delay)

    icon_group.update(ticks, delay)
    dialog_group.update(ticks, delay)
    battle_group.update(ticks, delay)
    player_group.update(ticks, delay)
    trade_group.update(ticks, delay)

    # npc update
    fairy_group.update(ticks, delay)
    merchant01_group.update(ticks, delay)
    thief_group.update(ticks,delay)
    wise_group.update(ticks,delay)

    # enemy update
    gSlime_group.update(ticks, delay)
    rSlime_group.update(ticks, delay)
    lBat_group.update(ticks, delay)
    skSoldier_group.update(ticks, delay)
    bSlime_group.update(ticks, delay)
    bMagician_group.update(ticks, delay)
    skCaptain_group.update(ticks, delay)
    bBat_group.update(ticks, delay)
    orc_group.update(ticks, delay)
    lGuard_group.update(ticks,delay)
    rBat_group.update(ticks,delay)
    skElite_group.update(ticks,delay)


def groups_draw(screen):
    starrySky_group.draw(screen)
    wall_group.draw(screen)
    ground_group.draw(screen)
    lava_group.draw(screen)
    block_group.draw(screen)
    upstairs_group.draw(screen)
    downstairs_group.draw(screen)

    redBlood_group.draw(screen)
    blueBlood_group.draw(screen)
    redGem_group.draw(screen)
    blueGem_group.draw(screen)
    greenGem_group.draw(screen)
    aSword_group.draw(screen)
    aShield_group.draw(screen)

    player_group.draw(screen)

    # npc draw
    fairy_group.draw(screen)
    merchant01_group.draw(screen)
    thief_group.draw(screen)
    wise_group.draw(screen)

    # enemy draw
    gSlime_group.draw(screen)
    rSlime_group.draw(screen)
    lBat_group.draw(screen)
    skSoldier_group.draw(screen)
    bSlime_group.draw(screen)
    bMagician_group.draw(screen)
    skCaptain_group.draw(screen)
    bBat_group.draw(screen)
    orc_group.draw(screen)
    lGuard_group.draw(screen)
    rBat_group.draw(screen)
    skElite_group.draw(screen)

    battle_group.draw(screen)
    icon_group.draw(screen)
    dialog_group.draw(screen)
    trade_group.draw(screen)


def groups_clear():
    starrySky_group.empty()
    wall_group.empty()
    ground_group.empty()
    lava_group.empty()
    block_group.empty()
    upstairs_group.empty()
    downstairs_group.empty()

    redBlood_group.empty()
    blueBlood_group.empty()
    redGem_group.empty()
    blueGem_group.empty()
    greenGem_group.empty()
    aSword_group.empty()
    aShield_group.empty()

    # npc clear
    fairy_group.empty()
    merchant01_group.empty()
    thief_group.empty()
    wise_group.empty()

    # enemy clear
    gSlime_group.empty()
    rSlime_group.empty()
    lBat_group.empty()
    skSoldier_group.empty()
    bSlime_group.empty()
    bMagician_group.empty()
    skCaptain_group.empty()
    bBat_group.empty()
    orc_group.empty()
    lGuard_group.empty()
    rBat_group.empty()
    skElite_group.empty()
