# Character.py
from MyLibrary import MySprite
import pygame


class Character:
    def __init__(self, hp, atk, deff, gold, exp):
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.gold = gold
        self.exp = exp


class Hero(Character, MySprite):
    def __init__(self, hp, atk, deff, speed, gold, exp):
        MySprite.__init__(self)
        self.level = 1
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.speed = speed
        self.gold = gold
        self.exp = exp
        self.moving = False
        self.isTalking = False
        self.isFighting = False
        self.isShopping = False

    def attack(self, enemy):
        damage = self.atk - enemy.deff
        return '普通攻击', damage


fairy_dialogue = {1: [('我是仙女，被困在这里', '我需要你的帮助'), ('我的十字架在第8层', ''),
                      ('请你取回我的十字架', '我可以增强强你的实力')],
                  2: [('我的十字架在第8层', '请你赶快取回来')]}
thief_dialogue = {1: [('我是盗贼，偶然来到这里', '我被这些该死的怪物困住'), ('我发现这里有一条密道', '如果你帮我取回我的镐头'),
                      ('我可以帮你打通密道', '我的镐头遗落在13层')],
                  2: [('我的镐头在13层', '加油老铁')]}
wise_dialogue = {1: [('小伙子，你怎么来这的', '这里非常的危险'), ('有一个魔王统治着这座塔', '这里的怪物都是他的小弟'),
                     ('这些怪物随着层数的提升', '会逐渐变强'), ('你要多加小心', '')],
                 2: [('注意各项属性的全面提升', '祝你好运')]}


class Npc:
    def __init__(self, dialogue):
        self.meet = 0
        self.dialogue = dialogue
        self.talk_status = False
        self.talk_num = 0

    def conversation(self):
        if self.meet == 1:
            talk = self.dialogue[1]
        else:
            talk = self.dialogue[2]
        return talk


class Merchant():
    def __init__(self, itemList):
        self.commodity = itemList


merchant01 = Merchant([('攻击', 25, 4), ('防御', 25, 4), ('生命', 10, 100), ('速度', 20, 1)])

npc_fairy = Npc(fairy_dialogue)
npc_thief = Npc(thief_dialogue)
npc_wise = Npc(wise_dialogue)
characterDict = {61: npc_fairy, 62: merchant01, 63: npc_thief, 64: npc_wise}


class Enemy:
    def __init__(self, name, hp, atk, deff, speed, exp, gold):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.speed = speed
        self.exp = exp
        self.gold = gold
        self.data = hp

    def attack(self, player):
        damage = self.atk - player.deff
        return '普通攻击', damage

    def refresh(self):
        self.hp = self.data


enemy_gSlime = Enemy('绿史莱姆', 50, 20, 1, 1, 1, 1)
enemy_rSlime = Enemy('红史莱姆', 70, 15, 2, 2, 2, 2)
enemy_lBat = Enemy('小蝙蝠', 100, 20, 5, 3, 3, 3)
enemy_skSoldier = Enemy('初级骷髅兵', 120, 28, 6, 4, 4, 4)
enemy_bSlime = Enemy('大史莱姆', 200, 35, 16, 5, 6, 5)
enemy_skCaptain = Enemy('骷髅队长', 180, 45, 24, 7, 8, 6)
enemy_bMagician = Enemy('蓝衣法师', 160, 52, 28, 8, 11, 8)
enemy_bBat = Enemy('大蝙蝠', 185, 65, 30, 9, 13, 8)
enemy_orc = Enemy('兽人', 360, 80, 50, 10, 16, 10)
enemy_lGuard = Enemy('初级卫兵', 480, 160, 90, 12, 26, 16)
enemy_rBat = Enemy('红蝙蝠', 600, 168, 96, 15, 20, 18)
enemy_skElite = Enemy('骷髅精英', 720, 160, 110, 16, 36, 22)

enemyDict = {101: enemy_gSlime, 102: enemy_rSlime, 103: enemy_lBat, 104: enemy_skSoldier, 105: enemy_bSlime,
             106: enemy_skCaptain, 107: enemy_bMagician, 108: enemy_bBat, 109: enemy_orc, 110: enemy_lGuard,
             111: enemy_rBat,
             112: enemy_skElite}
