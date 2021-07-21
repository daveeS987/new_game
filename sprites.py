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

        # temporary variables that store change in movement during one loop, adds to the x and y variables
        self.x_change = 0
        self.y_change = 0

        #direction your character is facing
        self.facing = 'down'

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        # call functions
        self.movement()
        
        # add x_change onto the x value, move left to right
        self.rect.x += self.x_change
        # add y_change onto the y value, move up and down
        self.rect.y += self.y_change
        # set the temporary x_change and y_change
        self.x_change = 0
        self.y_change = 0

    # moves the player
    def movement(self):
        # X is the win_width or 640 pixels and Y is the win_height or 480 pixels
        # stores all the keyboard keys
        keys = pygame.key.get_pressed()
        # K = Keyboard LEFT = left arrow key
        if keys[pygame.K_LEFT]:
            # taking away from x moves left on the x axis
            self.x_change -= PLAYER_SPEED
            # change direction character facing 
            self.facing = 'left'
        # K = Keyboard RIGHT = right arrow key
        if keys[pygame.K_RIGHT]:
            # add to x to move right
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
            # move character up take away from y to move up
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
            # move character down add to y to move down
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'