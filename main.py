import pygame, sys
from sprites import *
from config import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        # self.font = pygame.font.Font('Arial', 32)
        self.running = True

    # method that iterates through our tilemap and builds it
    def create_tile_map(self):
        # i is the value of each item in tilemap list, row is the position of the list
        # iterate through each row, enumerate gets content and position of the item in list
        for i, row in enumerate(tilemap):
            # iterate through each item by row/line/string
            for j, column in enumerate(row):
                if column == "B":
                    # j = x positon and i = y position
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)

    def new(self):

        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

                # call tilemap
        self.create_tile_map()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
    
    def game_over(self):
        pass

    def intro_screen(self):
        pass


g = Game()
g.intro_screen()
g.new()
while g.running is True:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
