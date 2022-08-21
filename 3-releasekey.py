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
player_x_inc = 0    # 3: increment of x increment
player_y_inc = 0    # 3: increment of y increment
player_image = pygame.image.load('images/kiiro.png')
PLAYER_SPEED = 5

BOARD_WIDTH, BOARD_HEIGHT = 600, 800
import random
tree_image = pygame.image.load('images/tree.png')
tree_width, tree_height = tree_image.get_size()
tree_x = random.randint(0, BOARD_WIDTH - tree_width)
tree_y = random.randint(0, BOARD_HEIGHT)
DOWNHILL_SPEED = 4
tree_y_inc = -DOWNHILL_SPEED

tree_x2 = random.randint(0, BOARD_WIDTH - tree_width)
tree_y2 = random.randint(0, BOARD_HEIGHT)
tree_x3 = random.randint(0, BOARD_WIDTH - tree_width)
tree_y3 = random.randint(0, BOARD_HEIGHT)

game_on = True
while game_on:
    BOARD.fill((255, 255, 255))
    BOARD.blit(player_image, (player_x, player_y))
    BOARD.blit(tree_image, (tree_x, tree_y))
    BOARD.blit(tree_image, (tree_x2, tree_y2))
    BOARD.blit(tree_image, (tree_x3, tree_y3))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False
            elif event.key == pygame.K_LEFT:
                player_x_inc = -PLAYER_SPEED  # 3: moving to the left
            elif event.key == pygame.K_RIGHT:
                player_x_inc = PLAYER_SPEED   # 3: moving to the right
            elif event.key == pygame.K_UP:
                player_y_inc = -PLAYER_SPEED  # 3: moving to the up side
            elif event.key == pygame.K_DOWN:
                player_y_inc = PLAYER_SPEED   # 3: moving to the down side
        # 3: keep moving until releasing key buttons
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_x_inc = 0    # 3: stop moving
            elif event.key == pygame.K_RIGHT:
                player_x_inc = 0    # 3: stop moving
            elif event.key == pygame.K_UP:
                player_y_inc = 0    # 3: stop moving
            elif event.key == pygame.K_DOWN:
                player_y_inc = 0    # 3: stop moving
    player_x = player_x + player_x_inc  # 3: change the x coordinate of player
    player_y = player_y + player_y_inc  # 3: change the y coordinate of player
                
    tree_y = tree_y + tree_y_inc
    if tree_y < -tree_height:
        tree_y = BOARD_HEIGHT
    tree_y2 = tree_y2 + tree_y_inc
    if tree_y2 < -tree_height:
        tree_y2 = BOARD_HEIGHT
    tree_y3 = tree_y3 + tree_y_inc
    if tree_y3 < -tree_height:
        tree_y3 = BOARD_HEIGHT

    pygame.display.flip()
    CLOCK.tick(FRAME_RATE)

pygame.quit()
