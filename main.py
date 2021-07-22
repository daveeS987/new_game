import pygame, sys
from sprites import *
from config import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        # import fonts for the game
        self.font = pygame.font.Font('arial.ttf', 32)
        self.running = True

        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.enemy_spritesheet = Spritesheet('img/enemy.png')
        self.intro_background = pygame.image.load('img/introbackground.png')

    def create_tile_map(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "P":
                    Player(self, j, i)

    def new(self):

        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

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
        intro = True

        # create title, content, antialiasing, color
        title = self.font.render('The game', True, BLACK)
        # position rectangle
        title_rect = title.get_rect(x=10, y=10)
        # create a button object
        play_button = Button(10, 50, 100, 50, WHITE, BLACK, 'Play', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            # get mouse position
            mouse_pos = pygame.mouse.get_pos()
            # check list if mouse button pressed left button = [0], right button = [1]
            mouse_pressed = pygame.mouse.get_pressed()

            # check if left button pressed
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            
            # display background, text and buttons
            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            # refresh every 60 frames per second
            self.clock.tick(FPS)
            pygame.display.update()


g = Game()
g.intro_screen()
g.new()
while g.running is True:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
