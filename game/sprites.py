import pygame, math, random

from pygame import key
from game.config import *


class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite


class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font("Arial.ttf", fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width / 2, self.height / 2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False


class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE

        self.animation_loop = 0

        self.image = self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.animate()
        self.collide()

        # where the attack collides, passes in the attack, the enemies and if True kills the enemy

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)

    def animate(self):
        direction = self.game.player.facing

        right_animations = [
            self.game.attack_spritesheet.get_sprite(0, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(32, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(64, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(96, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 64, self.width, self.height),
        ]

        down_animations = [
            self.game.attack_spritesheet.get_sprite(0, 32, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(32, 32, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(64, 32, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(96, 32, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 32, self.width, self.height),
        ]

        left_animations = [
            self.game.attack_spritesheet.get_sprite(0, 96, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(32, 96, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(64, 96, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(96, 96, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 96, self.width, self.height),
        ]

        up_animations = [
            self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(32, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(96, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height),
        ]

        if direction == "up":
            self.image = up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()

        if direction == "down":
            self.image = down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()

        if direction == "left":
            self.image = left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()

        if direction == "right":
            self.image = right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
