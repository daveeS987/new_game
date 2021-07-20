import pygame, sys
from sprites import *
from config import *


# main game class
class Game:
    def __init__(self):
        # initialize the game
        pygame.init()
        # create the window
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # set game frame rate
        self.clock = pygame.time.Clock()
        # game font
        # self.font = pygame.font.Font('Arial', 32)
        # game is actually running
        self.running = True

    def new(self):
        # new game starts
        self.playing = True

        # contains all the sprites in the game, use to update everything at once
        self.all_sprites = pygame.sprite.LayeredUpdates()
        # all barriers/walls in the game
        self.blocks = pygame.sprite.LayeredUpdates()
        # all enemies in the game
        self.enemies = pygame.sprite.LayeredUpdates()
        # all attack animations in the game
        self.attacks = pygame.sprite.LayeredUpdates()
        # player in game and location it spawns on map 1 = x and 2 = y.  they are then multipled by TILESIZE or 32. 1 = 32 and 2 = 64

        self.player = Player(self, 1, 2)

    def events(self):
        # game loop events, loops over every event in pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if game hits quit we stop playing and running
                self.playing = False
                self.running = False

    def update(self):
        # game loop updates
        # find the update method in every sprite and update them.
        self.all_sprites.update()

    def draw(self):
        # game loop draw
        # fills the screen with the color BLACK
        self.screen.fill(BLACK)
        # finds every sprite in the game and their rectangle and draws them on the screen.
        self.all_sprites.draw(self.screen)
        # how often we update the screen
        self.clock.tick(FPS)
        # updates the screen
        pygame.display.update()

    def main(self):
        # main game loop, while running the game is playing
        while self.playing:
            # key press events
            self.events()
            # update the game so it is not a static image
            self.update()
            # draws images on the screen
            self.draw()
        self.running = False
    
    def game_over(self):
        pass

    def intro_screen(self):
        pass


# create game object
g = Game()
# run intro screen, skips if no intro screen
g.intro_screen()
# makes playing True and creates all the game objects/sprites
g.new()
while g.running is True:
    g.main()
    # ends game, not current in
    g.game_over()

pygame.quit()
sys.exit()
