#!/usr/bin/env python3
"""A simple skiing game.
"""
import pygame


BOARD_SIZE = BOARD_WIDTH, BOARD_HEIGHT = 600, 800
FRAME_RATE = 20

pygame.init()

BOARD = pygame.display.set_mode(BOARD_SIZE)
CLOCK = pygame.time.Clock()

player_x = 50
player_y = 50

player_image = pygame.image.load('images/kiiro.png')

BOARD_WIDTH, BOARD_HEIGHT = 600, 800
import random
tree_image = pygame.image.load('images/tree.png')
tree_width, tree_height = tree_image.get_size()
tree_x = random.randint(0, BOARD_WIDTH - tree_width)
tree_y = random.randint(0, BOARD_HEIGHT)
DOWNHILL_SPEED = 4
tree_y_inc = -DOWNHILL_SPEED

# 2: challenge 2 - create more trees
tree_x2 = random.randint(0, BOARD_WIDTH - tree_width)
tree_y2 = random.randint(0, BOARD_HEIGHT)
tree_x3 = random.randint(0, BOARD_WIDTH - tree_width)
tree_y3 = random.randint(0, BOARD_HEIGHT)

game_on = True
while game_on:
    BOARD.fill((255, 255, 255))
    BOARD.blit(player_image, (player_x, player_y))
    BOARD.blit(tree_image, (tree_x, tree_y))
    # 2: challenge 2 - display more trees
    BOARD.blit(tree_image, (tree_x2, tree_y2))
    BOARD.blit(tree_image, (tree_x3, tree_y3))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False
            elif event.key == pygame.K_LEFT:
                player_x = player_x - 1
            elif event.key == pygame.K_RIGHT:
                player_x = player_x + 1
            elif event.key == pygame.K_UP:
                player_y = player_y - 1
            elif event.key == pygame.K_DOWN:
                player_y = player_y + 1
                
    tree_y = tree_y + tree_y_inc
    if tree_y < -tree_height:
        tree_y = BOARD_HEIGHT
    # 2: challenge 2 - update y coordinates
    tree_y2 = tree_y2 + tree_y_inc
    if tree_y2 < -tree_height:
        tree_y2 = BOARD_HEIGHT
    tree_y3 = tree_y3 + tree_y_inc
    if tree_y3 < -tree_height:
        tree_y3 = BOARD_HEIGHT

    pygame.display.flip()
    CLOCK.tick(FRAME_RATE)

pygame.quit()
