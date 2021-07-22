import pygame, math, random

from pygame import key
from config import *

# loads in all of the sprite images
class Spritesheet:
    def __init__(self, file):
        # loads in an image and converts it, convert makes it faster
        self.sheet = pygame.image.load(file).convert()

    # gets each individual sprite from the specified sprite sheet
    # takes an x, y, width and height x/y are the location and width and height are the size of the image
    def get_sprite(self, x, y, width, height):
        # create a surface that is this size 
        sprite = pygame.Surface([width, height])
        # draws the loaded image at the location, second parameter specifies the location, shape and size to cutout on the sprite sheet
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'

        # draw image from sprite sheet onto player class
        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
        # # image that we want to load onto the player sprite
        # image_to_load = pygame.image.load("img/single.png")
        # self.image = pygame.Surface((self.width, self.height))
        # # set_colorkey makes the specified color transparent, hides the background in the character image
        # self.image.set_colorkey(BLACK)
        # # blit is a function that draws the loaded image onto a surface/tilemap
        # # pass in the image and the location to load
        # self.image.blit(image_to_load, (0,0))

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

class  Block(pygame.sprite.Sprite):
        def __init__(self, game, x, y):
            self.game = game
            self._layer = BLOCK_LAYER
            self.groups = self.game.all_sprites, self.game.blocks
            pygame.sprite.Sprite.__init__(self, self.groups)

            self.x = x * TILESIZE
            self.y = y * TILESIZE
            self.width = TILESIZE
            self.height = TILESIZE

            # location on spritesheet and size to cut out
            self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)
            # self.image = pygame.Surface([self.width, self.height])
            # self.image.fill(BLUE)

            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

# create the ground/walkable terrain layer
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(64, 352, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y