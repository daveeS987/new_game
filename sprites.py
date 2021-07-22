import pygame, math, random

from pygame import key
from config import *

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
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

        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        
        self.rect.x += self.x_change
        # call collide block x after x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        # call collide block y after y_changepython 
        self.collide_blocks('y')
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
    
    # add block method, what direction we are moving so we can compare where to collide
    def collide_blocks(self, direction):
        # which direction we moving in, left to right
        if direction == "x":
            # check if rect of one sprite is inside the rect of another
            # comparing if players rect is any other rects in blocks, False checks to see if we want to delete the sprite when collide
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            # if there is a collission
            if hits:
                # if moving right
                if self.x_change > 0:
                    # places the top left corner of both rectangles to the same spot, then subtracts the width of a rectangle so find the points they touch
                    self.rect.x = hits[0].rect.left - self.rect.width
                # if moving left
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        # up and down
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                # moving down
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                # moving up
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

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

            self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)

            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

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