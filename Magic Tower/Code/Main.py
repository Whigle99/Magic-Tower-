# Main.py
# 18 * 13
import itertools, sys, time, random, math, pygame
from pygame.locals import *
from Code.MyLibrary import *
from Code.Map import INE, maps, get_item, kill_enemy
from Code.LoadImage import *
from Code.Character import *
from Code.ColorTable import *


def init():
    pygame.init()
    screen = pygame.display.set_mode((32 * 18, 32 * 13))
    pygame.display.set_caption('Magic Tower')
    timer = pygame.time.Clock()

    return screen, timer


# main program begins
screen, timer = init()
# fonts
font11 = pygame.font.Font('../Fonts/STXINGKA.TTF', 32)
font12 = pygame.font.Font('../Fonts/STXINGKA.TTF', 18)
font2 = pygame.font.Font('../Fonts/AdobeSongStd-Light.otf', 32)
font3 = pygame.font.Font('../Fonts/ariali.ttf', 18)
font32 = pygame.font.Font('../Fonts/Dengl.ttf', 18)
font42 = pygame.font.Font('../Fonts/Dengl.ttf', 12)


def print_info(screen, player):
    print_text(screen, font11, 120, 46, '级')
    print_text(screen, font2, 90, 46, str(player.level))

    print_text(screen, font12, 38, 84, '生命', Green, shadow=False)
    print_text(screen, font3, 96, 85, str(player.hp))
    print_text(screen, font12, 38, 104, '攻击', color=Orangered, shadow=False)
    print_text(screen, font3, 96, 105, str(player.atk))
    print_text(screen, font12, 38, 124, '防御', color=DeepSkyBlue, shadow=False)
    print_text(screen, font3, 96, 125, str(player.deff))
    print_text(screen, font12, 38, 144, '速度', color=Green, shadow=False)
    print_text(screen, font3, 96, 145, str(player.speed))
    print_text(screen, font12, 38, 184, '金币', color=Yellow, shadow=False)
    print_text(screen, font3, 96, 185, str(player.gold))
    print_text(screen, font12, 38, 204, '经验', color=Yellow, shadow=False)
    print_text(screen, font3, 96, 205, str(player.exp))

    print_text(screen, font12, 38, 224, '帮助', shadow=False)
    print_text(screen, font32, 96, 224, 'H', shadow=False)

    print_text(screen, font12, 64, 320, '第')
    print_text(screen, font12, 88, 320, str(level))
    print_text(screen, font12, 104, 320, '层')


graph = maps[0]
level = maps.index(graph)
# create the map of current level
load_map(graph)
load_ine(level, INE[level])

if __name__ == "__main__":
    # init player
    player = Hero(1000, 10, 10, 5, 0, 0)
    player, dialog_box, battle_bg, trade_bg = load_basic(player)
    next_talk = 0
    textList = []
    fight_delay = 0
    keyboard_delay = 0
    atk_info = ''
    last_turn = 0
    last_tick = - 80
    # main loop
    while True:
        timer.tick(30)
        ticks = pygame.time.get_ticks()

        # events detecting------keyboard
        directionFlag = 0
        for event in pygame.event.get():
            keyboard_delay += 1
            if event.type == QUIT:
                sys.exit()
            keys = pygame.key.get_pressed()

            if player.isTalking:
                if keys[K_SPACE]:
                    next_talk += 1
                    if next_talk == len(textList):
                        dialog_group.empty()
                        next_talk = 0
                        player.velocity = reverse_velocity(player.velocity)
                        player.isTalking = False
            elif player.isShopping:
                if keys[K_1]:
                    itemBought = 1
                elif keys[K_2]:
                    itemBought = 2
                elif keys[K_3]:
                    itemBought = 3
                elif keys[K_4]:
                    itemBought = 4
                elif keys[K_0]:
                    player.isShopping = False
            else:
                itemBought = 0
                if keys[K_h]:
                    game_help()
        # detecting keyboard---↑↓←→
        if not (player.isTalking or player.isFighting or player.isShopping):

            if ticks - last_tick >= 80:
                if keys[K_UP]:
                    player.direction = 3
                    player.moving = True
                    last_tick = ticks
                elif keys[K_RIGHT]:
                    player.direction = 2
                    player.moving = True
                    last_tick = ticks
                elif keys[K_DOWN]:
                    player.direction = 0
                    player.moving = True
                    last_tick = ticks
                elif keys[K_LEFT]:
                    player.direction = 1
                    player.moving = True
                    last_tick = ticks
            else:
                player.moving = False

        # select frame of player sprite
        player.first_frame = player.direction * player.columns
        player.last_frame = player.first_frame + player.columns - 1
        if player.frame < player.first_frame:
            player.frame = player.first_frame

        # if the player is moving
        if not player.moving:
            # stop animating when player is not pressing a key
            player.frame = player.first_frame = player.last_frame
        else:
            # move player in direction
            player.velocity = calc_velocity(player.direction, 1)
            player.velocity.x *= 32
            player.velocity.y *= 32

        # collision detection
        tempX = int((player.X + player.velocity.x) / 32)
        tempY = int((player.Y + player.velocity.y) / 32)
        if (collision_detection(tempY, tempX, graph)):
            player.moving = False

        # conversation detection
        npcNum = talk_detection(tempY, tempX, INE[level])
        if not player.isTalking:
            try:
                npc = characterDict[npcNum]
                npc.meet += 1
                player.isTalking = True
                player.moving = False
                textList = npc.conversation()
                dialog_group.add(dialog_box)
            except Exception:
                player.isTalking = False
                dialog_group.empty()

        # trade detection
        merchantNum = trade_detection(tempY, tempX, INE[level])
        if not player.isShopping:
            try:
                merchant = characterDict[merchantNum]
                player.isShopping = True
                player.moving = False
                trade_group.add(trade_bg)

            except Exception:
                player.isShopping = False
                trade_group.empty()

        # battle detection
        if not player.isFighting:
            enemyNum = battle_detection(tempY, tempX, INE[level])
            try:
                enemy = enemyDict[enemyNum[0]]
                player.isFighting = True
                player.moving = False
                battle_group.add(battle_bg)
            except Exception:
                player.isFighting = False
                battle_group.empty()

        # if get an item
        if get_item(player.position, INE[level], player):
            groups_clear()
            load_map(graph)
            load_ine(level, INE[level])

        # manually move the player
        if player.moving:
            player.X += player.velocity.x
            player.Y += player.velocity.y
            player.moving = False

        # up or down
        old_level = level
        level = go(player.X, player.Y, graph, level)
        if old_level != level:
            if old_level < level:
                go_flag = 1  # go upstairs
            else:
                go_flag = 0  # go downstairs
            graph = maps[level]
            groups_clear()
            load_map(graph)
            load_ine(level, INE[level])
            player.position = new_map_position(level, go_flag)

        player.velocity.x = 0
        player.velocity.y = 0

        # update groups
        groups_update(ticks)

        # draw groups
        screen.fill((0, 0, 0))
        groups_draw(screen)

        # print player info
        print_info(screen, player)

        # print conversation
        if player.isTalking:
            try:
                text = textList[next_talk]
                print_text(screen, font12, 160, 155, text[0])
                print_text(screen, font12, 160, 175, text[1])
                print_text(screen, font42, 230, 195, '--space--')
            except Exception:
                # player.isTalking = False
                pass

        if player.isShopping:
            try:
                itemBought = shopping(screen, font12, player, merchant, itemBought)
            except Exception:
                pass

        # x->152,y->64
        # fight
        if player.isFighting:
            attack_delay = 8
            fight_delay += 1
            fight_turn = round(fight_delay / attack_delay)
            deltaY = (fight_turn - 1) * 18

            print_text(screen, font12, 300, 80, enemy.name)
            print_text(screen, font12, 160, 85, '攻击', color=(255, 0, 0))
            print_text(screen, font3, 200, 85, str(enemy.atk))
            print_text(screen, font12, 160, 100, '防御', color=(0, 0, 255))
            print_text(screen, font3, 200, 100, str(enemy.deff))
            print_text(screen, font12, 160, 115, '速度', color=(0, 255, 0))
            print_text(screen, font3, 200, 115, str(enemy.speed))

            print_text(screen, font12, 240, 110, '玩家剩余生命', color=Green)
            print_text(screen, font3, 360, 110, str(player.hp))
            print_text(screen, font12, 240, 130, '敌人当前生命', color=(0, 0, 255))
            print_text(screen, font3, 360, 130, str(enemy.hp))

            if fight_delay % attack_delay == 0:
                if player.speed >= enemy.speed:
                    if fight_turn % 2 != 0:
                        skill, damage = player.attack(enemy)
                        enemy.hp -= damage
                        if enemy.hp < 0:
                            enemy.hp = 0
                        atk_info = '玩家使用' + skill + '造成伤害:' + str(damage)

                    if fight_turn % 2 == 0 and enemy.hp > 0:
                        skill, damage = enemy.attack(player)
                        player.hp -= damage
                        if player.hp < 0:
                            player.hp = 0
                        atk_info = '敌人使用' + skill + '造成伤害:' + str(damage)
                else:
                    if fight_turn % 2 != 0 and enemy.hp > 0:
                        skill, damage = enemy.attack(player)
                        player.hp -= damage
                        if player.hp < 0:
                            player.hp = 0
                        atk_info = '敌人使用' + skill + '造成伤害:' + str(damage)

                    if fight_turn % 2 == 0:
                        skill, damage = player.attack(enemy)
                        enemy.hp -= damage
                        if enemy.hp < 0:
                            enemy.hp = 0
                        atk_info = '玩家使用' + skill + '造成伤害:' + str(damage)
            if player.hp <= 0:
                if last_turn == 0:
                    last_turn = fight_turn
                atk_info = '一首凉凉送给你~~~'
                if fight_turn - last_turn >= 1:
                    sys.exit()
            if enemy.hp <= 0:
                if last_turn == 0:
                    last_turn = fight_turn
                atk_info = '战斗胜利'
                if fight_turn - last_turn >= 1:
                    player.isFighting = False
                    player.gold += enemy.gold
                    player.exp += enemy.exp

                    battle_group.empty()
                    fight_delay = 0
                    atk_info = ''
                    last_turn = 0
                    kill_enemy(enemyNum, INE[level])
                    groups_clear()
                    load_map(graph)
                    load_ine(level, INE[level])
                    enemy.refresh()

            if enemy.hp > 0 and player.hp > 0:
                print_text(screen, font12, 220, 200, atk_info)
            else:
                print_text(screen, font11, 220, 200, atk_info)

        # if level up
        level_up(player)

        pygame.display.update()
