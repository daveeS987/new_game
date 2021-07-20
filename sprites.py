import pygame, math, random
from config import *

# class for making player sprites
class Player(pygame.sprite.Sprite):
    # initialize, pass in game class and x (left <-> right)latitude, y (up <-> down)longitude coordinates
    def __init__(self, game, x, y):
        self.game = game
        # layer of screen we want player to appear
        self.player = PLAYER_LAYER
        # add player to the all sprites group
        self.groups = self.game.all_sprites
        # call init method for inherited class
        pygame.sprite.Sprite.__init__(self, self.groups)

        # tile size of player and location rectangles
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # creates an image of a rectangle thats 32 pixels wide and 32 pixels tall
        self.image = pygame.Surface((self.width, self.height))
        # fills the rectangle with the color red
        self.image.fill(RED)

        # rect sets the size of the rectangle or hit box to be the same as the sprites image
        self.rect = self.image.get_rect()
        # x and y coordinates of the sprite rectangle/hit box
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass