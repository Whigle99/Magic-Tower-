# Map.py
import copy


def list_add(l, l2):
    l1 = copy.deepcopy(l)
    for j1, j2 in zip(l1, l2):
        j1.reverse()
        for i in j1:
            j2.insert(0, i)


# starrySky=0,wall=1,ground=2,lava=3,block=4
u = 11  # up
d = 12  # down
rD = 21  # red blue yellow doors
bD = 23
yD = 25
rK = 22  # red blue yellow keys
bK = 24
yK = 26
rHP = 41
bHP = 42
ATK = 45
DEF = 46
SP = 47
aSword = 91
aShield = 92
item_list = [rD, bD, yD, rHP, bHP, ATK, DEF, SP, aSword, aShield]
# npc
fairy = 61
merchant01 = 62
thief = 63
wise = 64
# enemies
gSlime = 101
rSlime = 102
lBat = 103
skSoldier = 104
bSlime = 105
bMagician = 106
skCaptain = 107
bBat = 108
orc = 109
lGuard = 110
rBat = 111
skElite = 112

# bgd
status_bgd = [[4, 4, 4, 4, 4],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 4, 4, 4, 4]]
level0_bgd = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [4, 1, 0, 0, 0, 0, u, 0, 0, 0, 0, 1, 4],
              [4, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 4],
              [4, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 4],
              [4, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 4],
              [4, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 4],
              [4, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 4],
              [4, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 4],
              [4, 1, 1, 0, 0, 0, 2, 0, 0, 0, 1, 1, 4],
              [4, 1, 3, 3, 1, 2, 2, 2, 1, 3, 3, 1, 4],
              [4, 1, 3, 3, 3, 1, 2, 1, 3, 3, 3, 1, 4],
              [4, 1, 3, 3, 3, 1, 2, 1, 3, 3, 3, 1, 4],
              [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]
level1_bgd = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [4, u, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4],
              [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4],
              [4, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 4],
              [4, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 4],
              [4, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 4],
              [4, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 4],
              [4, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 2, 4],
              [4, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 4],
              [4, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1, 4],
              [4, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 4],
              [4, 2, 2, 2, 1, 2, d, 2, 1, 2, 2, 2, 4],
              [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]
level2_bgd = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [4, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 4],
              [4, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 4],
              [4, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 4],
              [4, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 2, 4],
              [4, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 4],
              [4, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 4],
              [4, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 4],
              [4, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 4],
              [4, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 4],
              [4, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 4],
              [4, d, 2, 1, 1, 1, 1, 2, 2, 2, 1, u, 4],
              [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]
level3_bgd = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [4, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 4],
              [4, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 4],
              [4, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 4],
              [4, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 4],
              [4, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 4],
              [4, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 4],
              [4, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 4],
              [4, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 4],
              [4, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 4],
              [4, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 4],
              [4, u, 1, 2, 2, 2, 2, 2, 2, 2, 1, d, 4],
              [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]
level4_bgd = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [4, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 4],
              [4, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 4],
              [4, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 4],
              [4, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 4],
              [4, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 4],
              [4, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4],
              [4, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 4],
              [4, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 4],
              [4, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
              [4, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 4],
              [4, d, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 4],
              [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]

maps = [level0_bgd, level1_bgd, level2_bgd, level3_bgd, level4_bgd]
for map in maps:
    list_add(status_bgd, map)

# items npc enemies --- ine
# left top:(6,1) right bottom:(16,11)
ine0 = [(fairy, 10, 9)]
ine1 = [(rHP, 6, 3), (ATK, 8, 4), (DEF, 6, 7), (rHP, 7, 10), (rHP, 6, 10), (rHP, 6, 11), (SP, 8, 11), (bHP, 14, 3),
        (rHP, 14, 4),
        (gSlime, 9, 1), (gSlime, 11, 1), (rSlime, 10, 1), (skSoldier, 8, 3), (skSoldier, 7, 4), (skCaptain, 7, 6),
        (skCaptain, 7, 7), (rHP, 8, 7), (bMagician, 7, 11), (skCaptain, 8, 10)
    , (skCaptain, 7, 9), (bMagician, 12, 6), (skCaptain, 13, 6), (bSlime, 14, 6), (bSlime, 14, 5), (orc, 13, 4),
        (orc, 13, 3),
        (orc, 15, 10), (skCaptain, 14, 10), (skCaptain, 16, 10), (orc, 15, 11), (ATK, 14, 11), (DEF, 16, 11),
        (SP, 12, 3)]
ine2 = [(lBat, 10, 10), (gSlime, 6, 6), (gSlime, 6, 7), (lBat, 9, 6), (rSlime, 10, 6), (lBat, 11, 6),
        (rSlime, 12, 9), (rSlime, 14, 9), (lBat, 13, 10), (skSoldier, 7, 3), (lBat, 6, 2), (lBat, 7, 1), (gSlime, 6, 3),
        (gSlime, 8, 1), (skSoldier, 11, 4), (rSlime, 14, 5), (lBat, 14, 4), (lBat, 14, 3),
        (lBat, 7, 2), (skSoldier, 11, 2), (lBat, 16, 3), (skSoldier, 16, 5), (lBat, 16, 7),
        (DEF, 12, 10), (ATK, 12, 11), (bHP, 13, 11), (aSword, 6, 1), (merchant01, 11, 1)]
ine3 = [(skSoldier, 16, 8), (bSlime, 16, 6), (skSoldier, 16, 4), (skCaptain, 14, 4), (rHP, 14, 6), (rHP, 14, 8),
        (bSlime, 13, 11), (bSlime, 9, 11), (rHP, 8, 8), (rHP, 8, 6), (skCaptain, 8, 4), (skSoldier, 6, 8),
        (bSlime, 6, 6), (skSoldier, 6, 4), (orc, 11, 10), (rHP, 11, 8), (orc, 10, 8), (orc, 12, 8), (ATK, 10, 7),
        (ATK, 12, 7), (lGuard, 11, 7), (bBat, 11, 5), (DEF, 10, 5), (DEF, 12, 5), (bBat, 10, 4), (bBat, 12, 4),
        (rBat, 11, 4), (thief, 11, 1)]
ine4 = [(wise, 7, 8), (DEF, 6, 7), (bBat, 6, 5), (bBat, 6, 3), (SP, 6, 1), (skSoldier, 8, 11), (bSlime, 9, 9),
        (bSlime, 9, 8), (skCaptain, 8, 4), (bMagician, 8, 2), (ATK, 8, 1), (orc, 13, 8), (lGuard, 15, 8),
        (skElite, 13, 11), (skElite, 15, 11), (orc, 14, 4), (skCaptain, 15, 1), (skCaptain, 15, 2), (bHP, 16, 1),
        (aShield, 10, 4),
        (bMagician, 10, 3), (bMagician, 11, 4), (bBat, 10, 2), (ATK, 10, 1), (bBat, 11, 1), (bBat, 12, 2),
        (bBat, 13, 1), (bBat, 14, 2)]
INE = [ine0, ine1, ine2, ine3, ine4]


def get_item(pos, ineList, player):
    x = int(pos[0] / 32)
    y = int(pos[1] / 32)
    item = -1
    index = ()
    for ine in ineList:
        if (x, y) == (ine[1], ine[2]) and ine[0] in item_list:
            item = ine[0]
            index = ine
            break
    if item == 41:
        player.hp += 200
    elif item == 42:
        player.hp += 500
    elif item == 45:
        player.atk += 3
    elif item == 46:
        player.deff += 3
    elif item == 47:
        player.speed += 1
    elif item == 91:
        player.atk += 10
    elif item == 92:
        player.deff += 10
    else:
        pass
    if item != -1 and index != None:
        ineList.remove(index)
        return True
    else:
        return False


def kill_enemy(enemy, ineList):
    for ine in ineList:
        if enemy[0] == ine[0] and enemy[1] == ine[1] and enemy[2] == ine[2]:
            ineList.remove(ine)
            break
