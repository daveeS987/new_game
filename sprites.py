import pygame, math, random

from pygame import key
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.player = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

# creates walls or barrier
class  Block(pygame.sprite.Sprite):
    # pass in game and the x and y coordinates
        def __init__(self, game, x, y):
            self.game = game
            # layer that blocks are built on
            self._layer = BLOCK_LAYER
            # adds to all sprites and block groups
            self.groups = self.game.all_sprites, self.game.blocks
            # call init method of inherited class of py.sprite.Sprite
            pygame.sprite.Sprite.__init__(self, self.groups)

            # x and y position of each block * the size of each tile
            self.x = x * TILESIZE
            self.y = y * TILESIZE
            # size of each sprite,makes each sprite a square with dimensions 32 pixels by 32 pixels
            self.width = TILESIZE
            self.height = TILESIZE

            # gives the sprite a image that fits into a 32 by 32 pixel square
            self.image = pygame.Surface([self.width, self.height])
            # fill the image square with a color
            self.image.fill(BLUE)

            # create rectangle/hit box and set it to the size of the image
            self.rect = self.image.get_rect()
            # sets position of rectangle
            self.rect.x = self.x
            self.rect.y = self.y